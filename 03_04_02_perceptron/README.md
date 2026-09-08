# Lab 3.4.2 — Watch a perceptron learn AND

This guided notebook addresses **HO-3.4.2 (H1)**: experience a perceptron
learning a simple function by changing its weights and bias across epochs
until it makes no errors. It takes approximately 25–35 minutes.

Read syllabus sections 3.4 and 3.4.1 first. The notebook teaches the specific
update rule before using it. No Python programming experience, previous lab
artifacts, external data, or additional ML library is required.

## Start

From this directory in PowerShell:

```powershell
.\start_lab.ps1
```

The launcher creates `%LOCALAPPDATA%\CTAIStudy\lab-3-4-2`, installs the pinned
JupyterLab version, and opens `guided_lab.ipynb`. Python must be available as
`python`; internet access is needed for the initial dependency installation.
The notebook itself runs offline. Add `-NoBrowser` to obtain a Jupyter URL
without opening a browser automatically.

An existing Jupyter environment also works: open this notebook with its
working directory set to this folder so `lab_display.py` can be imported.

## Work through the notebook

Run cells in order with Shift+Enter. Follow the first epoch in a table, watch
the error count across epochs, inspect the learned decision boundary, and
try two small changes to the bias. All implementation code is supplied.
The only code edits are an epoch number and a bias shift of 1 or -1.

Write the three short observations directly in their notebook Markdown
cells. Each prompt names the preceding output to use and the expected
response length. There is no separate learning log or retrieval worksheet.
Save your answers and outputs in the notebook for the completion commit.

The model uses all four AND cases. This is a demonstration of learning a
complete binary function, not an evaluation of generalization. It does not
require XOR, deep-network training, coverage metrics, or hyperparameter tuning.

## Baseline

Tag `lab-3.4.2-starter` records the unanswered notebook with cleared outputs.
Later study work should be committed separately without moving this tag.
The helper module only formats tables and SVG diagrams; prediction and
training are visible in the notebook. No artifacts are exchanged with other labs.

## Sources

The primary source is the local CT-AI v2.0 syllabus,
`../../markdown_syllabus/03_machine_learning.md`, sections 3.4–3.4.2.
Section 0.5 of `../../markdown_syllabus/00_introduction.md` defines H1 as a
guided exercise. These files belong to the enclosing study vault and are not
included in this Git repository. Necessary implementation explanations are
included in the notebook. This is personal, unofficial study material.
