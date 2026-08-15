# Lab 3.1.3 learning log

**Date:**  
**Starting confidence (1–5):**  

Write before checking hints or running the next cell. Short, concrete answers are better than polished ones.

## 1. Frame the problem

- What is one example?
- What are the features?
- What is the label?
- Why is this supervised learning?
- Why is this classification rather than ML regression?
- What would “useful” mean beyond obtaining a high score on this toy dataset?
- Before seeing results, what provisional accuracy criterion will I use for this lab?
- What additional criteria would real stakeholders need (for example, per-class behavior, speed, or risks of harmful errors)?

## 2. Predict the split

My intended proportions:

- Training:
- Validation:
- Test:

Why should the test portion be isolated before model selection?

What do I expect `stratify=y` to preserve?

## 3. Inspect only the training data

- Which feature pair appears to separate the species most clearly?
- Where do classes overlap?
- Why can a two-dimensional plot not tell me everything a four-feature model will learn?

## 4. First model

Why a decision tree is reasonable under this lab's constraints:  
One alternative classifier and a trade-off it would introduce:  

Chosen initial `max_depth`:  
Reason for choosing it before seeing a score:  

Prediction:

- Training accuracy will be:
- Validation accuracy will be:
- The gap will be about:

Observation:

- Training accuracy was:
- Validation accuracy was:
- What does the gap suggest?

## 5. Tune on validation data

Before running all candidates, predict how increasing depth will affect:

- training accuracy:
- validation accuracy:

Results:

| `max_depth` | Training accuracy | Validation accuracy | My interpretation |
| --- | ---: | ---: | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| unlimited | | | |

Chosen depth:  
Why this choice is supported by validation rather than test evidence:  

If two candidates tie, which would I prefer and why?

## 6. Lock a test prediction

Do this before opening the test vault.

- Expected test accuracy:
- Expected difference `test − validation`:
- A small difference would suggest:
- A large negative difference could suggest:

## 7. Final observation

- Validation accuracy:
- Test accuracy:
- Difference `test − validation`:
- Was my prediction close?
- What can random sampling explain here?
- Why must I not change `max_depth` in response and report a new score from the same test set as if it were independent?

## 8. Teach-back (without notes first)

Complete in 4–6 sentences:

> Training data is used to ...  
> Validation data is used to ...  
> Test data is used to ...  
> In this lab, evaluation/tuning differed from testing because ...  
> The validation and test accuracies were ...  
> This result does / does not establish production readiness because ...

## 9. Retrieval check

Answer without code:

1. If I choose a hyperparameter after looking at test accuracy, what role is that dataset now playing?
2. Does the validation set train the decision tree's learned split thresholds? Distinguish direct fitting from human-guided model selection.
3. Why might a perfectly legitimate test accuracy be higher than validation accuracy?
4. What would I need to change if examples were ordered by time and future predictions were the objective?
5. Where do `fit`, `predict`, evaluation, tuning, and testing appear in the syllabus workflow?

## 10. Close

- One-sentence intuition I want to retain:
- One mistake or surprise worth reviewing:
- One question to revisit in section 3.2 or 3.3:
- Ending confidence (1–5):
