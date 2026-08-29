# Curated resources for Lab 3.3.2

Use a source to resolve a specific question after making your own attempt.

## 1. How are the four outcomes arranged?

Read the scikit-learn documentation for
[`confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html).

Check which axis represents actual classes and which represents predicted
classes before unpacking the binary matrix as TN, FP, FN, and TP.

## 2. What does each metric calculate?

Use the official scikit-learn references for
[`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html),
[`precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html),
[`recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html),
and [`f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html).

Map each function back to the formula in syllabus section 3.3.1. Confirm the
positive label and the behavior requested when a denominator is zero.

## 3. Why is accuracy insufficient here?

Review the target-distribution evidence in your completed HO-3.2.2 notebook.
Compare the majority-class proportion with what an always-negative classifier
would do to recall for the positive class.

## 4. What exactly is being reused?

Read `../03_02_02_prepare_ml_data/HANDOFF_HO_3_3.md` and the manifest in your
generated artifact directory. Distinguish the unchanged fitted pipeline from
the validation rows used here to evaluate it.
