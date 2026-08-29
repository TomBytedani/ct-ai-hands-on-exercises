# Lab 3.2.2 — Prepare data for a machine learning model

This guided lab addresses **HO-3.2.2 (H2)** from the CT-AI v2.0 syllabus:

> For a given set of data, perform the applicable data preparation steps as
> outlined in Section 3.2.1 to produce a dataset that will be used to create a
> classification model using supervised learning.

The assessed work is data preparation: acquisition checks, exploratory data
analysis, preprocessing, and feature engineering. A short supplied handoff at
the end trains one fixed baseline classifier so the prepared data and model can
be reused by HO-3.3.2 and HO-3.3.3. It does not evaluate or tune that model.

## Scenario and source

The task is to predict, immediately before a scheduled marketing call begins,
whether a client will subscribe to a term deposit. The lab uses the
`bank-additional-full.csv` variant of the UCI Bank Marketing dataset: 41,188
historical examples from a Portuguese banking institution, ordered from May
2008 through November 2010.

The raw file is included unchanged under the Creative Commons Attribution 4.0
license. See [data/SOURCE.md](./data/SOURCE.md) for provenance, citation,
license, and integrity hashes. This historical teaching dataset is not evidence
that demographic or financial profiling would be appropriate in a real system.

## What you will learn

By the end, you should be able to:

- map concrete work to data acquisition, preprocessing, feature engineering,
  and EDA;
- identify numerical, categorical, target, and metadata fields;
- use prediction time to identify a leaking feature;
- distinguish missing information and sentinel values from ordinary values;
- justify retaining, removing, transforming, or deferring a data item;
- fit learned preprocessing only from training data;
- produce a reproducible prepared dataset, split assignment, and preparation
  record for downstream work;
- explain why data preparation is iterative and must remain consistent when
  operational data is processed.

## Perimeter

The lab does not calculate model performance, tune hyperparameters, compare
models, test for bias or representativeness, or claim production readiness.
Those topics belong to later objectives. The fixed split and model handoff are
provided scaffolding, not additional learning objectives.

## Time and prerequisites

- Allow about **90–120 minutes**.
- Study sections 3.1.1, 3.1.2, 3.2.1, and 3.2.3 first.
- Completing HO-3.1.3 first is useful but not required.
- Basic Python familiarity is useful; the notebook introduces the required
  pandas and scikit-learn operations.

## Start the lab on Windows

From this directory in PowerShell, run:

```powershell
.\start_lab.ps1
```

The script creates an isolated environment under
`%LOCALAPPDATA%\CTAIStudy\lab-3-2-2`, installs the pinned dependencies, and
opens `guided_lab.ipynb` in JupyterLab.

If PowerShell prevents direct execution, use:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_lab.ps1
```

To start without opening a browser automatically:

```powershell
.\start_lab.ps1 -NoBrowser
```

## How to work

1. Work from top to bottom in `guided_lab.ipynb`; it is the only chronological
   workspace.
2. At each **STOP**, write in the empty answer cell immediately below it before
   running the following code.
3. Open hints progressively and only after making an attempt.
4. Do not inspect validation or test feature values after the split.
5. Let the final supplied section train and save the baseline; do not calculate
   its metrics in this lab.
6. Open `learning_log.md` only when the notebook directs you to complete the
   post-lab retrieval.

## Generated handoff

The final notebook section creates, but the starter does not contain:

- `artifacts/prepared_data.csv`;
- `artifacts/split_assignments.csv`;
- `artifacts/baseline_model.joblib`;
- `artifacts/manifest.json`.

These are intended to be committed with the completed notebook and learning
log on a study branch. Maintainers of the following exercises should use
[HANDOFF_HO_3_3.md](./HANDOFF_HO_3_3.md) as the contract.

## Completion rule

You are finished only when the preparation checks pass, the four artifacts are
created, and you can explain the decisions in the post-lab log. Do not reveal
model metrics or change the fixed classifier in this exercise.
