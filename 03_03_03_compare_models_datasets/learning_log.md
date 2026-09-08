# Lab 3.3.3 learning log

**Date:**

**Starting confidence (1–5):**

The notebook is the ordered learning path. Write here only when its matching
checkpoint directs you to do so.

## Checkpoint 1 — Predict the comparison

Before fitting, predict in short prose:

- **Q1.1:** How might logistic regression on the core 15 features differ from logistic regression on all 20 features? How A (logistic/core) may differ from B (logistic/full): Less features would decrease the complexity of the model and therefore lower the F1-score.
- **Q1.2:** With the full feature set fixed, how might logistic regression and a random forest differ in validation behavior? How B (logistic/full) may differ from C (random forest/full): Random forest will likely train a better model (higher F1-score) as it's suited to a larger amount of features with non-linear relationships.
- **Q1.3:** Candidate likely to take longest and why: C
- **Q1.4:** Why measured seconds are environment-specific: depends on GPU/CPU hardware and kernel/OS

## Checkpoint 2 — Verify the experiment design

- **Q2.1:** My core-feature expression is in the notebook code cell.
- **Q2.2:** The pair isolating the dataset combination and the pair isolating
  the model family: A&B model family; B&C dataset combination
- **Q2.3:** Why preprocessing must be fresh and which rows may fit it: Each model should have it's own instance of the dataset, since they're being trained separately. Second question: I have no idea.
- **Q2.4:** My timing, prediction, and metric expressions are in the notebook code cell.

	model	feature_count	accuracy	precision	recall	f1	fit_seconds
candidate							
A	logistic	15	0.898155	0.661818	0.196121	0.302577	0.311987
B	logistic	20	0.899005	0.644578	0.230603	0.339683	0.471951
C	random_forest	20	0.891721	0.536437	0.285560	0.372714	9.409960

## Checkpoint 3 — Interpret validation evidence

- **Q3.1:** Validation winner, F1 evidence, and precision/recall context: C has it, it has lower precision compared to the other two models, and yet it has the highest recall score. This means the model's prediction are less often correct but it catches more of them.
- **Q3.2:** A-vs-B feature-set interpretation:

A has: lower accuracy, higher precision, lower recall and an overall lower F1 score.
B has: higher accuracy, lower precision, higher recall and better F1 score.

The model with full feature would be the final model selected out of the two. It catches slightly more false positives, but it has better sensitivity and F1 score.

- **Q3.3:** B-vs-C model-family interpretation: As initially predicted, the Random Forest classification approach works better for this type of dataset and relationshit between features. The candidate C has the highest F1 score out of all the evaluated models. The biggest downside to using candidate C's model type is the longer training time, which for the given dataset and hardware is eclipsed by the increased performance.
- **Q3.4:** Cautious fit-time interpretation and CPU/runtime context:
Model A: 0.311 secs
Model B: 0.47 secs
Model C: 9.41 secs

The training times shouldn't be generalized outside of this environment since they're tied to my PC's hardware (GPU/CPU performance).

- **Q3.5:** Tie-break use and evidence after locking the selection: No, the better model has much higher training time.

## Checkpoint 4 — Lock before test

- **Q4.1:** Locked candidate and selection rule: useless question
- **Q4.2:** Expected test F1 and expected difference from validation F1: I predict a slightly lower F1 score for test dataset. I predict a final test F1 score of 0.368
- **Q4.3:** Meaning of a lower result and why it cannot authorize a new choice: could be random given by the data distribution in holdout dataset
- **Q4.4:** Independent role of the test set at lock time: please... these are questions I've answered 18 times previously. It's not about the excercise.

## Checkpoint 5 — Final interpretation

- **Q5.1:** Final metrics and test-minus-validation F1:
Final locked candidate: C
  test accuracy : 0.896213
  test precision: 0.576842
  test recall   : 0.295259
  test f1       : 0.390592
  test F1 - selected validation F1: +0.017877

I had predicted a lower score and it was higher. This is likely because I hadn't anticipated that the validation dataset would be used to re-train the model for independent test, and this likely improves the model itself since there's marginally more data available.
  
- **Q5.2:** Why the final model was refitted on train plus validation:
It's a standard set in the Model Generation workflow. It's done because this allows to test the model on the final holdout dataset with all the data available and used to tune the model previously.
- **Q5.3:** Why changing any choice now would misuse test evidence:
Because it would mean that test data is used to tune the model, which shouldn't happen and would invalidate the truthfulness of the reported tests.

## Retrieval after closing the notebook

1. **R1:** What two factors differ between candidates A and C, making their direct
   comparison less diagnostic than A-vs-B or B-vs-C? Model type and amount of data samples used.
2. **R2:** What operation, exactly, was timed? The training time of each model.
3. **R3:** State the primary selection rule and exact-tie rule. Primary selection is based on F1-score, tie-breaker is when F1-scores are equal and the faster model to train is chosen.
4. **R4:** Did validation labels directly fit classifier parameters? How did they still influence development? I don't understand this question.
5. **R5:** At what point did validation rows become legitimate fitting data? After the final model to test was chosen.

**Ending confidence (1–5):** 4
