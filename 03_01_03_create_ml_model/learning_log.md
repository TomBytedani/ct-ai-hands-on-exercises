# Lab 3.1.3 learning log

**Date:** 27/08/2026
**Starting confidence (1–5):** 2

Write before checking hints or running the next cell. Short, concrete answers are better than polished ones.

## 1. Frame the problem

- What is one example? One single, correctly measured iris flower example, with the main characteristics unique to the species defined.
- What are the features?
- What is the label? (rounded, irregular) Petal shape, (blue, purple, other) color texture, (slim, has_buds, curvature) stem characteristic, (color, spikyness, density) pistil feature
- Why is this supervised learning? This is supervised learning because it trains the model from labeled data for a classification task.
- Why is this classification rather than ML regression? ML regression learns to continuosly predict numerical values, in this case we are working with classes.
- What would “useful” mean beyond obtaining a high score on this toy dataset?
- Before seeing results, what provisional accuracy criterion will I use for this lab? 87%
- What additional criteria would real stakeholders need (for example, per-class behavior, speed, or risks of harmful errors)?

## 2. Predict the split

My intended proportions:

- Training: 60%
- Validation: 20%
- Test: 20%

First we take off 20% for the independent test dataset, then to isolate the remaining 20% of validation dataset we divide the remaining by 25% (Let's say 100 is the initial dataset size, after we take 20 off we need to divide it by 4 to get the remaining 20%)

Why should the test portion be isolated before model selection? So that it may remain unseen until the model is ready for independent testing.

What do I expect `stratify=y` to preserve?

## 3. Inspect only the training data

- Which feature pair appears to separate the species most clearly? Petal width separates them more clearly than length
- Where do classes overlap? mostly the Versicolor and Virginica iris classes and mostly on petal length, there's a very small overlap on petal width
- Why can a two-dimensional plot not tell me everything a four-feature model will learn? Because since the four feature model has higher dimensional depth for the data points the two dimensional plot can't exhausively represent it correctly.

## 4. First model

Why a decision tree is reasonable under this lab's constraints:  A decision tree is reasonable because the amount of features is enough for it and it can deduce the thresholds that define each class based on the numerical values of the features themselves on its own.
One alternative classifier and a trade-off it would introduce: a K-Nearest Neighgbor (KNN) supervised learning algorithm may be used, but it would result in lower accuracy if the input data were to have values that are ambiguous or that overlap in multiple classes

Correction after checking: Class overlap can happen with any classifier. KNN's tradeoff would be that it would need feature scaling because of the it's distance-based nature and is also less directly interpretable than a small decision tree

Chosen initial `max_depth`:  2
Reason for choosing it before seeing a score: The space of possible decision depends on sepal length and width and petal length and width, and looking at the dataset it seems that setosa has very small petal sizes, so I think that would fit an initial depth of 1, then the question to classify between versicolor and virginica would then be posed on sepal width? I'm not entirely sure how to think about this properly and this is probably a bad attempt at it.

Prediction:

- Training accuracy will be: idk how it's even quantified, I guess it's a percentage, but I'd say 94%
- Validation accuracy will be: 77%
- The gap will be about: 17%

Observation:

Training accuracy:   0.989
Validation accuracy: 0.900
Gap (train - validation): +0.089
- What does the gap suggest? This suggests that there's a weak generalization capability and some overfit and likely not enough decision tree depth layers were set

## 5. Tune on validation data

Before running all candidates, predict how increasing depth will affect:

- training accuracy: increase
- validation accuracy: increase

Results:

| `max_depth` | Training accuracy | Validation accuracy | My interpretation |
| --- | ---: | ---: | --- |
| 1 | 0.667 | 0.667 | no gap but low scores, likely underfitting |
| 2 | 0.989 | 0.900 | high train-acc but gap present, likely overfitting: not enough depth |
| 3 | 0.989 | 0.900 | high train-acc but gap present, likely overfitting: not enough depth. Three decision layers aren't enough to capture the data |
| 4 | 1.000 | 0.933 | best attempt so far, but there's still some error margin between training and validation|
| unlimited | 1.000 | 0.933 | The unrestricted tree naturally stopped at depth 4, so increasing the limit did not change the result. |

Chosen depth: 4
Why this choice is supported by validation rather than test evidence: Test evidence records how the model predicts the same dataset it has ingested, but the more useful measure for generalization outside of the already-seen data is verifying on the validation set

If two candidates tie, which would I prefer and why? Likely the one that requires less compute to run? I'm not sure, but I think that some additional tests by shuffling the data and re-training the models to see if they remain identical would be necessary.

## 6. Lock a test prediction

Do this before opening the test vault.

- Expected test accuracy: 0.933
- Expected difference `test − validation`: 0
- A small difference would suggest: weaker overfitting (positive thing)
- A large negative difference could suggest: stronger overfitting (negative thing)

## 7. Final observation

Validation accuracy used for selection: 0.933
Independent test accuracy:             0.933
Difference (test - validation):         +0.000
- Was my prediction close? yes
- What can random sampling explain here? I don't understand this question.
- Why must I not change `max_depth` in response and report a new score from the same test set as if it were independent? Again, I don't understand this question

## 8. Teach-back (without notes first)

Complete in 4–6 sentences:

> Training data is used to ...  Train the model to learn from the features in the data
> Validation data is used to ...  Evaluate and tune the model based on data not yet seen during training
> Test data is used to ...  Conduct a final evaluation of the selected hyperparameters and a check for generalization capabilities
> In this lab, evaluation/tuning differed from testing because ...  I don't understand the question, isn't it implicit in the initial text that evaluation was used to tune the model and algorithm while testing was just used to check for generalization?
> The validation and test accuracies were ... identical
> This result does / does not establish production readiness because ... It does establish production readiness, but a larger dataset or attempts with different supervised learning classification methods could be susequently attempted to check for improved performance

## 9. Retrieval check

Answer without code:

1. If I choose a hyperparameter after looking at test accuracy, what role is that dataset now playing? The test set would then become part of the training process and no longer be useful for an indepentent final evaluation.
2. Does the validation set train the decision tree's learned split thresholds? Distinguish direct fitting from human-guided model selection. No. Validation set wasn't used in this lab for training the model itself, but it was useful for tuning the decision tree depth parameter while engineering the model hyperparams.
3. Why might a perfectly legitimate test accuracy be higher than validation accuracy? The samples present in the test set were more similar to the train set.
4. What would I need to change if examples were ordered by time and future predictions were the objective? Include the datetime feature so that it may be useful as an additional decision step.
5. Where do `fit`, `predict`, evaluation, tuning, and testing appear in the syllabus workflow? In the Model Generation, Training & Testing workflow

## 10. Close

- One-sentence intuition I want to retain: The amount of decision tree steps is independent of the number of features, which is not something that this excercise specifically brought up but it's something that I picked up while asking myself questions.
- One mistake or surprise worth reviewing: The fact that I said this result proved production readiness. It is not since a single result doesn't satisfy any business requests or acceptance criteria
- One question to revisit in section 3.2 or 3.3:
- Ending confidence (1–5): 3
