"""Strict loader for the trusted artifacts produced by HO-3.2.2.

The public functions deliberately return only the evidence needed at the
current learning stage.  In particular, the HO-3.3.2 notebook never receives
test rows, and HO-3.3.3 receives them only after its selection is locked.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import os
import platform
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
import sklearn
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.utils.validation import check_is_fitted


SCHEMA_VERSION = "1.0"
SOURCE_FILENAME = "bank-additional-full.csv"
SOURCE_SHA256 = "74ADFC578BF77A7FF4BB1BA4A9F8709D9E3C6907342959C2C8416847E0AFB4D8"
ROW_COUNT = 41_188
TARGET_COLUMN = "subscribed"
METADATA_COLUMNS = ["source_row_id"]
FULL_FEATURES = [
    "age",
    "job",
    "marital",
    "education",
    "default",
    "housing",
    "loan",
    "contact",
    "month",
    "day_of_week",
    "campaign",
    "pdays",
    "previous",
    "poutcome",
    "emp_var_rate",
    "cons_price_idx",
    "cons_conf_idx",
    "euribor3m",
    "nr_employed",
    "previously_contacted",
]
CATEGORICAL_FEATURES = [
    "job",
    "marital",
    "education",
    "default",
    "housing",
    "loan",
    "contact",
    "month",
    "day_of_week",
    "poutcome",
]
NUMERIC_FEATURES = [
    feature for feature in FULL_FEATURES if feature not in CATEGORICAL_FEATURES
]
CORE_FEATURES = [
    feature
    for feature in FULL_FEATURES
    if feature
    not in {
        "emp_var_rate",
        "cons_price_idx",
        "cons_conf_idx",
        "euribor3m",
        "nr_employed",
    }
]
SPLIT_SIZES = {"train": 24_712, "validation": 8_238, "test": 8_238}
ARTIFACT_FILENAMES = (
    "prepared_data.csv",
    "split_assignments.csv",
    "baseline_model.joblib",
    "manifest.json",
)


class ArtifactContractError(RuntimeError):
    """Raised when the upstream handoff is missing, stale, or inconsistent."""


@dataclass(frozen=True)
class ArtifactContext:
    artifact_dir: Path
    hashes: dict[str, str]
    manifest: dict[str, Any]


@dataclass(frozen=True)
class ValidationArtifacts:
    validation: pd.DataFrame
    baseline_model: Pipeline
    context: ArtifactContext


@dataclass(frozen=True)
class DevelopmentArtifacts:
    train: pd.DataFrame
    validation: pd.DataFrame
    context: ArtifactContext


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source_file:
        for block in iter(lambda: source_file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _error(message: str, mode: str) -> ArtifactContractError:
    if mode == "override":
        return ArtifactContractError(
            "Invalid CTAI_HO_3_2_2_ARTIFACTS reference fixture: "
            f"{message} No fallback was attempted."
        )
    return ArtifactContractError(
        "HO-3.2.2 artifacts are missing or invalid: "
        f"{message} Complete or rerun HO-3.2.2, including its final artifact "
        "creation cell, and then restart this notebook."
    )


def _require(condition: bool, message: str, mode: str) -> None:
    if not condition:
        raise _error(message, mode)


def _resolve_artifact_dir(lab_root: Path) -> tuple[Path, str]:
    if "CTAI_HO_3_2_2_ARTIFACTS" in os.environ:
        override = os.environ.get("CTAI_HO_3_2_2_ARTIFACTS", "").strip()
        if not override:
            raise _error("the override is set but empty.", "override")
        artifact_dir = Path(override).expanduser().resolve()
        if not artifact_dir.is_dir():
            raise _error(f"{artifact_dir} is not an existing directory.", "override")
        return artifact_dir, "override"

    artifact_dir = lab_root.resolve().parent / "03_02_02_prepare_ml_data" / "artifacts"
    if not artifact_dir.is_dir():
        raise _error(f"expected directory {artifact_dir} was not found.", "learner")
    return artifact_dir, "learner"


def _validate_manifest(manifest: dict[str, Any], mode: str) -> None:
    _require(
        manifest.get("schema_version") == SCHEMA_VERSION,
        f"unsupported manifest schema_version {manifest.get('schema_version')!r}; expected {SCHEMA_VERSION!r}.",
        mode,
    )
    _require(
        manifest.get("source")
        == {
            "dataset": "UCI Bank Marketing",
            "variant": SOURCE_FILENAME,
            "sha256": SOURCE_SHA256,
            "rows": ROW_COUNT,
        },
        "the manifest source record does not match the canonical UCI source.",
        mode,
    )
    _require(
        manifest.get("prediction_time") == "before_scheduled_call",
        "the prediction boundary is not 'before_scheduled_call'.",
        mode,
    )
    _require(
        manifest.get("target")
        == {
            "column": TARGET_COLUMN,
            "raw_mapping": {"no": 0, "yes": 1},
            "positive_class": 1,
        },
        "the target record or positive-class semantics are invalid.",
        mode,
    )
    _require(
        manifest.get("columns")
        == {
            "metadata": METADATA_COLUMNS,
            "full_features": FULL_FEATURES,
            "categorical_features": CATEGORICAL_FEATURES,
            "numeric_features": NUMERIC_FEATURES,
        },
        "the metadata, feature, categorical, or numeric column list is invalid.",
        mode,
    )

    preparation = manifest.get("preparation", {})
    _require(
        preparation.get("excluded_features")
        == {"duration": "unavailable before the scheduled call"},
        "the duration exclusion record is missing or changed.",
        mode,
    )
    _require(
        preparation.get("unknown_policy") == "explicit_category",
        "the literal-unknown preparation policy is invalid.",
        mode,
    )
    _require(
        preparation.get("pdays_sentinel") == 999,
        "the pdays sentinel record is invalid.",
        mode,
    )
    _require(
        preparation.get("derived_features") == ["previously_contacted"],
        "the derived-feature record is invalid.",
        mode,
    )
    _require(
        preparation.get("exact_matches_retained") is True,
        "the exact-row retention decision is invalid.",
        mode,
    )

    _require(
        manifest.get("split")
        == {
            "method": "two stratified train_test_split calls",
            "seed": 42,
            "proportions": {"train": 0.60, "validation": 0.20, "test": 0.20},
            "sizes": SPLIT_SIZES,
            "roles": {
                "train": "fit preprocessing and model parameters",
                "validation": "evaluate baseline and compare development candidates",
                "test": "one final check after HO-3.3.3 selection",
            },
        },
        "the split strategy, seed, proportions, sizes, or roles are invalid.",
        mode,
    )
    _require(
        manifest.get("baseline_model")
        == {
            "artifact": "baseline_model.joblib",
            "pipeline_steps": ["preprocessor", "classifier"],
            "classifier": "LogisticRegression",
            "parameters": {
                "solver": "lbfgs",
                "C": 1.0,
                "max_iter": 2000,
                "class_weight": None,
            },
            "trained_on": "train",
            "performance_metrics_included": False,
        },
        "the baseline pipeline record is invalid.",
        mode,
    )

    active_versions = {
        "python": platform.python_version(),
        "pandas": pd.__version__,
        "scikit_learn": sklearn.__version__,
        "joblib": joblib.__version__,
    }
    _require(
        manifest.get("versions") == active_versions,
        f"dependency versions differ: manifest={manifest.get('versions')!r}, active={active_versions!r}.",
        mode,
    )


def _expected_split_ids(target: np.ndarray) -> dict[str, set[int]]:
    source_ids = np.arange(1, ROW_COUNT + 1)
    development_ids, test_ids, development_target, _ = train_test_split(
        source_ids,
        target,
        test_size=0.20,
        random_state=42,
        stratify=target,
    )
    train_ids, validation_ids = train_test_split(
        development_ids,
        test_size=0.25,
        random_state=42,
        stratify=development_target,
    )
    return {
        "train": set(train_ids.tolist()),
        "validation": set(validation_ids.tolist()),
        "test": set(test_ids.tolist()),
    }


def _validate_model(model: Any, mode: str) -> Pipeline:
    _require(
        isinstance(model, Pipeline),
        "baseline_model.joblib is not a scikit-learn Pipeline.",
        mode,
    )
    _require(
        list(model.named_steps) == ["preprocessor", "classifier"],
        "the baseline pipeline steps are invalid.",
        mode,
    )
    try:
        check_is_fitted(model)
    except Exception as exc:
        raise _error(f"the baseline pipeline is not fitted ({exc}).", mode) from exc

    preprocessor = model.named_steps["preprocessor"]
    classifier = model.named_steps["classifier"]
    _require(
        isinstance(preprocessor, ColumnTransformer),
        "the preprocessor is not a ColumnTransformer.",
        mode,
    )
    _require(
        isinstance(classifier, LogisticRegression),
        "the baseline classifier is not LogisticRegression.",
        mode,
    )
    _require(
        list(getattr(model, "feature_names_in_", [])) == FULL_FEATURES,
        "the fitted pipeline input feature order is invalid.",
        mode,
    )
    _require(
        list(getattr(preprocessor, "feature_names_in_", [])) == FULL_FEATURES,
        "the fitted preprocessor input feature order is invalid.",
        mode,
    )

    transformers = preprocessor.transformers
    _require(
        len(transformers) == 2,
        "the preprocessor must contain exactly two transformers.",
        mode,
    )
    numeric_name, numeric_pipeline, numeric_columns = transformers[0]
    category_name, category_pipeline, category_columns = transformers[1]
    _require(
        numeric_name == "numeric" and list(numeric_columns) == NUMERIC_FEATURES,
        "the numeric transformer or its feature list is invalid.",
        mode,
    )
    _require(
        category_name == "categorical"
        and list(category_columns) == CATEGORICAL_FEATURES,
        "the categorical transformer or its feature list is invalid.",
        mode,
    )
    _require(
        isinstance(numeric_pipeline, Pipeline)
        and list(numeric_pipeline.named_steps) == ["imputer", "scaler"],
        "the numeric preprocessing pipeline is invalid.",
        mode,
    )
    _require(
        isinstance(numeric_pipeline.named_steps["imputer"], SimpleImputer)
        and numeric_pipeline.named_steps["imputer"].strategy == "median",
        "numeric median imputation is not configured.",
        mode,
    )
    _require(
        isinstance(numeric_pipeline.named_steps["scaler"], StandardScaler),
        "numeric StandardScaler is not configured.",
        mode,
    )
    _require(
        isinstance(category_pipeline, Pipeline)
        and list(category_pipeline.named_steps) == ["imputer", "encoder"],
        "the categorical preprocessing pipeline is invalid.",
        mode,
    )
    categorical_imputer = category_pipeline.named_steps["imputer"]
    encoder = category_pipeline.named_steps["encoder"]
    _require(
        isinstance(categorical_imputer, SimpleImputer)
        and categorical_imputer.strategy == "constant"
        and categorical_imputer.fill_value == "unknown",
        "categorical constant-'unknown' imputation is not configured.",
        mode,
    )
    _require(
        isinstance(encoder, OneHotEncoder) and encoder.handle_unknown == "ignore",
        "OneHotEncoder(handle_unknown='ignore') is not configured.",
        mode,
    )
    _require(
        classifier.solver == "lbfgs"
        and classifier.C == 1.0
        and classifier.max_iter == 2000
        and classifier.class_weight is None,
        "the logistic-regression settings are invalid.",
        mode,
    )
    _require(
        np.array_equal(classifier.classes_, np.array([0, 1])),
        "the fitted classifier classes are not [0, 1].",
        mode,
    )
    return model


def _validate_all(
    lab_root: Path,
) -> tuple[pd.DataFrame, pd.DataFrame, Pipeline, ArtifactContext]:
    artifact_dir, mode = _resolve_artifact_dir(lab_root)
    missing = [
        name for name in ARTIFACT_FILENAMES if not (artifact_dir / name).is_file()
    ]
    _require(not missing, f"required files are missing: {missing}.", mode)

    paths = {name: artifact_dir / name for name in ARTIFACT_FILENAMES}
    hashes = {name: _sha256(path) for name, path in paths.items()}
    try:
        manifest = json.loads(paths["manifest.json"].read_text(encoding="utf-8"))
    except Exception as exc:
        raise _error(f"manifest.json could not be parsed ({exc}).", mode) from exc
    _validate_manifest(manifest, mode)

    upstream_root = lab_root.resolve().parent / "03_02_02_prepare_ml_data"
    raw_source_path = upstream_root / "data" / "raw" / SOURCE_FILENAME
    _require(
        raw_source_path.is_file(),
        f"canonical raw source {raw_source_path} was not found.",
        mode,
    )
    _require(
        _sha256(raw_source_path) == SOURCE_SHA256,
        "the canonical raw-source SHA-256 does not match the manifest.",
        mode,
    )

    try:
        prepared = pd.read_csv(paths["prepared_data.csv"])
        assignments = pd.read_csv(paths["split_assignments.csv"])
        raw = pd.read_csv(raw_source_path, sep=";")
    except Exception as exc:
        raise _error(f"a CSV artifact could not be parsed ({exc}).", mode) from exc

    expected_columns = [*METADATA_COLUMNS, *FULL_FEATURES, TARGET_COLUMN]
    _require(
        "duration" not in prepared.columns,
        "duration leaked into prepared_data.csv even though it is unavailable before the call.",
        mode,
    )
    _require(
        prepared.columns.tolist() == expected_columns,
        f"prepared_data.csv columns do not match the required schema {expected_columns}.",
        mode,
    )
    _require(
        assignments.columns.tolist() == ["source_row_id", "split"],
        "split_assignments.csv must contain only source_row_id and split.",
        mode,
    )
    _require(
        len(prepared) == ROW_COUNT and len(assignments) == ROW_COUNT,
        "artifact row counts are not 41,188.",
        mode,
    )
    expected_ids = list(range(1, ROW_COUNT + 1))
    _require(
        prepared["source_row_id"].tolist() == expected_ids,
        "prepared rows are not unique and in original source order.",
        mode,
    )
    _require(
        assignments["source_row_id"].tolist() == expected_ids,
        "split assignments do not uniquely cover rows in source order.",
        mode,
    )
    _require(
        set(prepared[TARGET_COLUMN].unique()) == {0, 1},
        "the prepared target is not binary 0/1.",
        mode,
    )
    _require(
        "duration" not in prepared.columns
        and not {"duration", "source_row_id", TARGET_COLUMN} & set(FULL_FEATURES)
        and not {"duration", "source_row_id", TARGET_COLUMN} & set(CORE_FEATURES),
        "duration, source_row_id, or subscribed entered model inputs.",
        mode,
    )
    _require(
        len(FULL_FEATURES) == 20 and len(CORE_FEATURES) == 15,
        "the full or core feature list has the wrong size.",
        mode,
    )

    expected_prepared = raw.copy()
    expected_prepared.insert(0, "source_row_id", np.arange(1, len(raw) + 1))
    expected_prepared = expected_prepared.rename(
        columns=lambda name: name.replace(".", "_")
    )
    expected_prepared = expected_prepared.rename(columns={"y": TARGET_COLUMN})
    expected_prepared[TARGET_COLUMN] = expected_prepared[TARGET_COLUMN].map(
        {"no": 0, "yes": 1}
    )
    expected_prepared = expected_prepared.drop(columns=["duration"])
    expected_prepared["previously_contacted"] = (
        expected_prepared["pdays"] != 999
    ).astype("int8")
    expected_prepared["pdays"] = expected_prepared["pdays"].replace(999, np.nan)
    expected_prepared = expected_prepared[expected_columns]
    try:
        pd.testing.assert_frame_equal(prepared, expected_prepared, check_dtype=False)
    except AssertionError as exc:
        raise _error(
            f"prepared_data.csv differs from the canonical semantic transformation ({exc}).",
            mode,
        ) from exc

    _require(
        manifest["preparation"].get("exact_matching_rows_beyond_first")
        == int(raw.duplicated(keep="first").sum()),
        "the exact-matching-row evidence record is invalid.",
        mode,
    )
    _require(
        set(assignments["split"].unique()) == set(SPLIT_SIZES),
        "split labels must be train, validation, and test.",
        mode,
    )
    actual_sizes = assignments["split"].value_counts().to_dict()
    _require(
        actual_sizes == SPLIT_SIZES, f"split sizes are invalid: {actual_sizes}.", mode
    )
    actual_ids = {
        split: set(
            assignments.loc[assignments["split"] == split, "source_row_id"].tolist()
        )
        for split in SPLIT_SIZES
    }
    _require(
        actual_ids["train"].isdisjoint(actual_ids["validation"])
        and actual_ids["train"].isdisjoint(actual_ids["test"])
        and actual_ids["validation"].isdisjoint(actual_ids["test"]),
        "split membership overlaps.",
        mode,
    )
    expected_split_ids = _expected_split_ids(
        expected_prepared[TARGET_COLUMN].to_numpy()
    )
    _require(
        actual_ids == expected_split_ids,
        "split membership differs from the fixed seed-42 stratified assignment.",
        mode,
    )

    # Joblib/pickle loading can execute code.  Load only after validating that
    # this is the normal learner path or an explicitly selected maintainer
    # override and after all non-executable contract checks have passed.
    try:
        model = joblib.load(paths["baseline_model.joblib"])
    except Exception as exc:
        raise _error(
            f"the trusted baseline model could not be loaded ({exc}).", mode
        ) from exc
    model = _validate_model(model, mode)
    _require(
        {name: _sha256(path) for name, path in paths.items()} == hashes,
        "an artifact changed while it was being validated.",
        mode,
    )

    context = ArtifactContext(
        artifact_dir=artifact_dir, hashes=hashes, manifest=manifest
    )
    return prepared, assignments, model, context


def _frame_for_split(
    prepared: pd.DataFrame, assignments: pd.DataFrame, split: str
) -> pd.DataFrame:
    split_ids = assignments.loc[assignments["split"] == split, "source_row_id"]
    indexed = prepared.set_index("source_row_id", drop=False)
    return indexed.loc[split_ids].reset_index(drop=True)


def load_validation_artifacts(lab_root: Path) -> ValidationArtifacts:
    """Validate the handoff and expose only validation rows plus the baseline."""
    prepared, assignments, model, context = _validate_all(Path(lab_root))
    validation = _frame_for_split(prepared, assignments, "validation")
    return ValidationArtifacts(
        validation=validation, baseline_model=model, context=context
    )


def load_development_artifacts(lab_root: Path) -> DevelopmentArtifacts:
    """Validate the handoff and expose training and validation rows, not test."""
    prepared, assignments, _model, context = _validate_all(Path(lab_root))
    train = _frame_for_split(prepared, assignments, "train")
    validation = _frame_for_split(prepared, assignments, "validation")
    return DevelopmentArtifacts(train=train, validation=validation, context=context)


def open_test_frame(
    context: ArtifactContext, *, selection_locked: bool
) -> pd.DataFrame:
    """Open unchanged test rows only after the notebook locks its winner."""
    if selection_locked is not True:
        raise RuntimeError(
            "The test vault remains sealed. Record and lock the validation winner first."
        )
    current_hashes = {
        name: _sha256(context.artifact_dir / name) for name in ARTIFACT_FILENAMES
    }
    if current_hashes != context.hashes:
        raise ArtifactContractError(
            "The HO-3.2.2 artifacts changed after preflight. Restart the notebook and "
            "investigate rather than opening the test set."
        )
    prepared = pd.read_csv(context.artifact_dir / "prepared_data.csv")
    assignments = pd.read_csv(context.artifact_dir / "split_assignments.csv")
    return _frame_for_split(prepared, assignments, "test")
