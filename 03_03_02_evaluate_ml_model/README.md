# Lab 3.3.2 — Evaluate a machine-learning model

This guided lab addresses **HO-3.3.2 (H2)** from the CT-AI v2.0 syllabus:

> Using the classification model trained in the previous exercise, calculate
> and display accuracy, precision, recall, and F1-score. Where applicable, use
> the library functions supplied by the ML development framework.

The lab reuses the fitted baseline pipeline from HO-3.2.2 unchanged. It makes
one set of predictions on validation rows, reconstructs true positives, true
negatives, false positives, and false negatives, and checks hand calculations
against scikit-learn.

## Prerequisite and artifact path

Complete HO-3.2.2 through its final artifact-creation cell first. Normal learner
execution reads:

```text
../03_02_02_prepare_ml_data/artifacts
```

Maintainers and automated tests may set `CTAI_HO_3_2_2_ARTIFACTS` to a trusted
reference-artifact directory. An invalid override fails without falling back.
The preflight verifies source integrity, schema and manifest versions, feature
lists, exact split membership, dependency versions, and the trusted fitted
pipeline before loading it.

Joblib files use pickle-compatible loading and can execute code. Never point
the override at an artifact from an untrusted source.

## Learning perimeter

This exercise:

- evaluates validation rows only and never displays a test metric;
- treats `subscribed=1` as the positive class;
- calculates accuracy, precision, recall, and F1 from confusion-matrix counts;
- connects class imbalance to the limitations of accuracy alone.

It does not fit, tune, threshold-adjust, replace, or save a model. The 2008–2010
Portuguese bank-marketing data is a historical teaching benchmark, not evidence
for contemporary profiling or deployment decisions.

## Start on Windows

From this directory in PowerShell, run:

```powershell
.\start_lab.ps1
```

The launcher creates an isolated pinned environment under
`%LOCALAPPDATA%\CTAIStudy\lab-3-3-2` and opens `guided_lab.ipynb`. To avoid opening
a browser automatically, use `.\start_lab.ps1 -NoBrowser`.

## How to work

1. Follow `guided_lab.ipynb` from top to bottom; it is the chronological path.
2. Answer every numbered question in the notebook before running the next cell.
3. Use the matching checkpoint in `learning_log.md` only when directed; it is a
   short reflection record, not a second set of steps.
4. Stop after interpreting the validation metrics. Leave the test set sealed.

## Files

- `guided_lab.ipynb` — ordered predictions, calculations, checks, and prompts.
- `learning_log.md` — matching checkpoint reflections and final retrieval.
- `artifact_contract.py` — strict, non-negotiable HO-3.2.2 handoff checks.
- `RESOURCES.md` — focused authoritative references.
- `requirements.txt` and `start_lab.ps1` — pinned local environment and launcher.
