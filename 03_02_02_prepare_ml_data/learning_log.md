# Lab 3.2.2 post-lab learning log

**Date:**

**Starting confidence (1–5):**

**Ending confidence (1–5):**

Open this file only after the notebook tells you that the four handoff artifacts
have been created. Answer without reopening hints first.

## 1. Reconstruct the preparation workflow

Give one concrete example from the lab for each activity:

| Activity | What I did | Why it belonged to this activity |
| --- | --- | --- |
| Data acquisition | | |
| Data preprocessing | | |
| Feature engineering | | |
| Exploratory data analysis | | |

Why can these activities be reordered or repeated in a real project?

## 2. Defend the decisions

Complete each explanation in one or two sentences.

- `duration` was removed because:
- Literal `unknown` values were retained as a category because:
- `pdays=999` was transformed rather than treated as 999 elapsed days because:
- `previously_contacted` was added because:
- Exact matching rows were retained because:
- Numerical scaling was performed because:
- Data augmentation and sampling were not performed because:

Which decision would be unsafe to make from a column name alone, without the
source documentation?

## 3. Explain the evidence boundary

- Why was EDA performed on training data rather than validation or test feature
  values?
- Which preprocessing operations learned values from the training data?
- How does the fitted pipeline apply those learned values consistently to later
  operational examples?
- Why is the saved validation set allowed to influence later model comparison,
  while the test set must remain untouched?

## 4. Explain the handoff

In five or six sentences, explain what another practitioner receives from this
exercise: the prepared data, split assignments, fitted model pipeline, and
manifest. Distinguish the semantic dataset from the learned preprocessing
inside the model pipeline. State what has **not** yet been learned about model
quality.

## 5. Retrieval check

1. Is every outlying or repeated row necessarily defective? What evidence is
   needed before removing it?
2. Why would replacing `pdays=999` with zero without an indicator lose
   information?
3. Why can a field be highly predictive and still be invalid for the intended
   model?
4. If a new operational category appears later, what pipeline behavior did the
   lab configure?
5. Name one reason the historical dataset should not be treated as evidence for
   a contemporary production targeting system.

## 6. Close

- One-sentence intuition I want to retain:
- One preparation decision I initially misunderstood:
- One question to revisit before HO-3.3.2:
