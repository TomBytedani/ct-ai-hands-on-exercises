# Lab 3.1.3 — Create a machine learning model

This guided lab addresses **HO-3.1.3 (H2)** from the CT-AI syllabus:

> Select, train, and test a classification model using supervised learning. Explain the difference between evaluating/tuning and testing by comparing the accuracy achieved with validation and test datasets.

The lab is intentionally not a recipe. It alternates between questions, small coding decisions, observable results, and explanation. Progressive hints are built into the notebook, but there is no complete answer to copy before you have formed a prediction.

## What you will learn

By the end, you should be able to:

- identify the examples, features, labels, and classes in a classification problem;
- justify why a decision tree is a reasonable classifier under the lab's constraints;
- explain what `fit`, `predict`, and an accuracy calculation do in conceptual terms;
- keep training, validation, and test data in distinct roles;
- use validation accuracy to choose a tree-depth hyperparameter;
- use the test set once to obtain an independent performance check;
- explain why similar validation and test scores are reassuring but not proof of production quality.

The lab uses scikit-learn's built-in Iris dataset. It is small, balanced, and available offline after installation, making it suitable for learning mechanics. It is a teaching dataset, not evidence that a workflow is ready for a consequential real-world system.

## Time and prerequisites

- Allow about **60–90 minutes**.
- Study sections 3.1.1 and 3.1.2 first.
- Basic Python familiarity is useful, but the notebook introduces the small part of the scikit-learn API that it uses.

## Start the lab on Windows

From this directory in PowerShell, run:

```powershell
.\start_lab.ps1
```

The script creates an isolated Python environment under `%LOCALAPPDATA%\CTAIStudy\lab-3-1-3`, installs the required packages, and opens `guided_lab.ipynb` in JupyterLab. Keeping the environment outside this deeply nested OneDrive folder also reduces the risk of Windows path-length problems.

If PowerShell's execution policy prevents direct execution, use:

```powershell
powershell -ExecutionPolicy Bypass -File .\start_lab.ps1
```

To start the server without opening a browser automatically:

```powershell
.\start_lab.ps1 -NoBrowser
```

## How to work

1. Open [learning_log.md](./learning_log.md) alongside the notebook.
2. At every **STOP**, write a prediction before running the next code cell.
3. If stuck, open only the first hint. Use the API hint only after making a genuine attempt.
4. Record surprising results and explain them in ordinary language.
5. Do not inspect or score the test set until the notebook opens the test vault.
6. Finish with the teach-back in the learning log. A successful run without an explanation is not completion.

The notebook fixes a random seed so your split is reproducible. This is helpful for discussion; it does not mean the score is a universal property of the algorithm.

## Files

- [guided_lab.ipynb](./guided_lab.ipynb) — experiment and progressive guidance.
- [learning_log.md](./learning_log.md) — predictions, observations, and teach-back.
- [RESOURCES.md](./RESOURCES.md) — curated authoritative sources, each paired with a reading question.
- [requirements.txt](./requirements.txt) — Python dependencies.
- [start_lab.ps1](./start_lab.ps1) — repeatable local setup and launcher.

## Stopping rule

Stop after the final test and explanation. Do not tune again in response to the test score: doing so would silently turn the test set into another validation set. If the result reveals a serious problem, the honest next step is to define a new development cycle and eventually obtain fresh independent test data.
