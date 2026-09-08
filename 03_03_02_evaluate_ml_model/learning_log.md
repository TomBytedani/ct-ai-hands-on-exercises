# Lab 3.3.2 learning log

**Date:**

**Starting confidence (1–5):** 4

The notebook is the ordered learning path. Write here only when its matching
numbered checkpoint directs you to do so.

## Checkpoint 1 — Predict before model output

- **Q1.1:** My predicted effect of class imbalance on accuracy:
  Even if a very common negative class rather than a more balanced pair I think the accuracy score wouldn't change much. Since the negative class would still be a correct prediction if contained in the True Negative prediction and the TP and TN are added up as the nominator, the distribution itself of where the True predicted values are placed isn't particularly relevant for the Accuracy score calculation.
- **Q1.2:** Approximate accuracy of an always-`no` classifier and my calculation: an always-"no" classifier would find the right answer 88.7% of the time. The calculation doesn't have to utilize the Confusion matrix related formulas but it's simply taken from the distribution of the "subscribed=0" value.
- **Q1.3:** Why that baseline can appear strong while never finding a subscriber: Because the distribution of subscribed=0 (no) is much larger than the 1 (yes) values.
- **Q1.4:** Comparison with the observed majority accuracy:
Validation target counts: {0: 7310, 1: 928}
Always-negative accuracy: 0.887
Always-negative positive-class recall: 0.000

Answer: My answer was correct.

## Checkpoint 2 — Give each error a meaning

In this pre-call scenario, complete one short sentence for each:

- **Q2.1:** True positive, true negative, false positive, and false negative: TP -> `True(y=0)`; TN -> `True(y=0)`; FP -> `False(y=1)`; FN -> `False(y=0)`
- **Q2.2:** The errors exposed by precision and recall: If I understand the question correctly, in Precision formula's denominator false positive are exposed, which in this case would be the model predicting `y=1` when it's actually `0`. In recall the error in the denominator would be false negatives, which would be "predicting `y=0` when in reality it's `1`".
- **Q2.3:** My Boolean-count expressions are in the notebook code cell.

## Checkpoint 3 — Reconstruct the metrics

Write each formula using `TP`, `TN`, `FP`, and `FN`, then state what its
denominator asks about:

- **Q3.1:** Accuracy, precision, recall, and F1 formulas:
Acc=((TP+TN)/(TP+TN+FP+FN))*100
P=((TP)/(TP+FP))*100
R=((TP)/(TP+FN))*100
F1=2*((P R)/(P+R))

- **Q3.2:** What each denominator asks about:
1. Precision asks "out of all the positively predicted values how many were actually positive"; Recall asks "out of all the possible actual positive values, how many did the model predict as positive"?; Accuracy asks "Out of all possible predictions which ones were correctly predicted?"; F1 is a bit more complex to explain just in terms of denominator. Let's just say it's a better way to calculate the mean value out of the previously calculated metrix, without having large values skewing towards an optimistic outcome.

- **Q3.3:** My arithmetic expressions are in the notebook code cell.
- **Q3.4:** My match/mismatch prediction before scikit-learn verification: I don't think there will be any mismatches.

## Checkpoint 4 — Interpret the evidence

- **Q4.1:** (expected: two or three prose sentences): Which metric differs most from accuracy, and which confusion-matrix errors explain the gap?
Recall, and it's because out of all the possible TP or FN, the model only predicted a very small amount.

- **Q4.2:** Why accuracy alone is incomplete: Because it doesn't take into account the wrong predictions and only the right ones.
- **Q4.3:** Meaning of high precision with lower recall:
Initially wrong answer: It means the model is underfitting to the dataset and not generalizing well into how the features predict a positive case (if the dataset allows it).
**Revised answer**: High precision with lower recall means the model’s positive predictions are usually correct, but it misses many actual positive cases. It produces relatively few false positives among its positive predictions, at the cost of more false negatives.

- **Q4.4:**  Explain why fitting, threshold adjustment, or choosing another model now would be a different activity from evaluating the supplied baseline. Why model or threshold changes are outside this evaluation: In this activity we're focusing on evaluating the previously trained model for learning purposes. We are not producing a deployable model. This model would require tuning and attempting to lower the thresholds that predict which values are positive.

- **Q4.5:** Evidence that remains unknown while test is sealed: The test set would be used subsequently after tuning and re-training the model. The final evidence that an independente dataset can give remains unknown during this hypothetical time.

## Retrieval after closing the notebook

1. **R1:** If `subscribed=1` is positive, what actual/predicted combination is an FN? Answer: predicted as 0 but actually 1
2. **R2:** Which denominator distinguishes precision from recall? FP is present in Precision, while FN is present in Recall. TP is present in both denominators.
3. **R3:** Why is F1 called a harmonic balance of precision and recall? Because it uses the harmonic mean equation, which is a less-prone-to-optimistically-skew-towards-larger-values method to calculate the mean between the other metrics.
4. **R4:** Can accuracy be high when a model predicts no positives? Under what data condition? When a large portion of the values of the classification target belong to a specific negative class and the model is trained to always predict that.
5. **R5:** Which dataset role did this lab use, and why did it not use the test set? This lab used the Training and Validation datasets. It would be redundant to explain why the holdout dataset wasn't included at this point, so I'll skip the questions.

**Ending confidence (1–5):** 4.5

**One-sentence intuition to retain:** Do not necessarily think that high precision and low recall needs to belong to either under or over fitting.
