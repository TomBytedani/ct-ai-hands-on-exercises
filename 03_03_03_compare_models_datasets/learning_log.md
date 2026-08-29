# Lab 3.3.3 learning log

**Date:**

**Starting confidence (1–5):**

The notebook is the ordered learning path. Write here only when its matching
checkpoint directs you to do so.

## Checkpoint 1 — Predict the comparison

Before fitting, predict in short prose:

- **Q1.1:** How A (logistic/core) may differ from B (logistic/full):
- **Q1.2:** How B (logistic/full) may differ from C (random forest/full):
- **Q1.3:** Candidate likely to take longest and why:
- **Q1.4:** Why measured seconds are environment-specific:

## Checkpoint 2 — Verify the experiment design

- **Q2.1:** My core-feature expression is in the notebook code cell.
- **Q2.2:** The pair isolating the dataset combination and the pair isolating
  the model family:
- **Q2.3:** Why preprocessing must be fresh and which rows may fit it:
- **Q2.4:** My timing, prediction, and metric expressions are in the notebook code cell.

## Checkpoint 3 — Interpret validation evidence

- **Q3.1:** Validation winner, F1 evidence, and precision/recall context:
- **Q3.2:** A-vs-B feature-set interpretation:
- **Q3.3:** B-vs-C model-family interpretation:
- **Q3.4:** Cautious fit-time interpretation and CPU/runtime context:
- **Q3.5:** Tie-break use and evidence after locking the selection:

## Checkpoint 4 — Lock before test

- **Q4.1:** Locked candidate and selection rule:
- **Q4.2:** Expected test F1 and expected difference from validation F1:
- **Q4.3:** Meaning of a lower result and why it cannot authorize a new choice:
- **Q4.4:** Independent role of the test set at lock time:

## Checkpoint 5 — Final interpretation

- **Q5.1:** Final metrics and test-minus-validation F1:
- **Q5.2:** Why the final model was refitted on train plus validation:
- **Q5.3:** Why changing any choice now would misuse test evidence:
- **Q5.4:** One supported conclusion and one unsupported broader claim:

## Retrieval after closing the notebook

1. **R1:** What two factors differ between candidates A and C, making their direct
   comparison less diagnostic than A-vs-B or B-vs-C?
2. **R2:** What operation, exactly, was timed?
3. **R3:** State the primary selection rule and exact-tie rule.
4. **R4:** Did validation labels directly fit classifier parameters? How did they still
   influence development?
5. **R5:** At what point did validation rows become legitimate fitting data?

**Ending confidence (1–5):**

**One-sentence intuition to retain:**
