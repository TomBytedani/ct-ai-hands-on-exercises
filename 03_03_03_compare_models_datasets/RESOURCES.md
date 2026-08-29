# Curated resources for Lab 3.3.3

Use these references to answer a focused question after making a prediction.

## 1. How are mixed feature types kept inside each model pipeline?

Read the official scikit-learn documentation for
[`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
and
[`ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html).

Identify which steps learn from training rows and why constructing a fresh
pipeline prevents learned state from leaking between candidates.

## 2. What model configurations are being compared?

Use the official references for
[`LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
and
[`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).

This lab fixes their settings in advance. Read to understand the supplied
parameters, not to start a tuning exercise.

## 3. What does the timer measure?

Read Python's
[`time.perf_counter`](https://docs.python.org/3/library/time.html#time.perf_counter)
documentation. Explain why elapsed fit time depends on hardware, operating
system activity, runtime, and library versions.

## 4. Why lock selection before the final test?

Review syllabus section 3.2.3 and the local
`../03_02_02_prepare_ml_data/HANDOFF_HO_3_3.md`. Distinguish validation-guided
selection from the one final use of independent test evidence.
