# Curated resources for Lab 3.1.3

These are primary or authoritative technical sources. Use them to answer a question, not as pages to read passively from top to bottom.

## 1. Why are there three data subsets?

Read: [Google Machine Learning Crash Course — Dividing the original dataset](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets)

Before reading, predict:

- What information leaks when a test score influences a hyperparameter choice, even if the model never trains directly on the test rows?

After reading, explain:

- In what sense can a validation or test set “wear out”?
- Why is a representative split necessary but not sufficient for real-world performance?

## 2. What do `fit` and `predict` mean?

Read: [scikit-learn — Getting started: estimator basics](https://scikit-learn.org/stable/getting_started.html#fitting-and-predicting-estimator-basics)

Map the API to the workflow:

- What information is supplied to `fit`?
- What has changed inside the estimator after `fit`?
- Why can `predict` accept features but not the correct labels?

## 3. What exactly does the split function control?

Read: [scikit-learn — `train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

Investigate:

- What does an integer `random_state` buy us in a learning experiment?
- What property does `stratify=y` try to preserve?
- If 20% is reserved first and 25% of the remaining 80% is reserved second, what fraction of the original data is in each subset?

## 4. Why must test data remain sealed?

Read: [scikit-learn — Common pitfalls: data leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)

Look for the distinction between:

- applying the same transformation to all subsets; and
- learning the transformation's parameters from all subsets.

Then answer: why is “never call `fit` on the test data” broader than just the classifier's `fit` call?

## 5. What data are we modeling?

Read: [scikit-learn — Iris dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html) and [UCI Machine Learning Repository — Iris](https://archive.ics.uci.edu/dataset/53/iris)

Ask:

- What is one row, one feature, and one label in this dataset?
- Which properties make Iris convenient for this lab?
- Which properties make it too limited to generalize broad claims about machine learning?

Note that scikit-learn documents corrections to two data points relative to the UCI copy. This lab uses the version bundled with scikit-learn.

## 6. What does tree depth change?

Read only the overview, advantages, and disadvantages in [scikit-learn — Decision Trees](https://scikit-learn.org/stable/modules/tree.html).

Predict:

- What patterns can a depth-1 tree express?
- Why can a deeper tree improve training accuracy while making its estimate on new data less reliable?
- When validation scores tie, what argument favors the simpler model?

## 7. What does accuracy count?

Read: [scikit-learn — `accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)

Before calling the function, calculate a tiny example by hand. Then explain why accuracy alone can be misleading when one class is much more common than another. Chapter 3.3 will add more informative classification metrics.
