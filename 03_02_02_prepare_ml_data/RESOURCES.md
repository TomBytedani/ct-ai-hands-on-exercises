# Curated resources for Lab 3.2.2

Use these sources to resolve a specific question rather than reading them from
top to bottom.

## 1. What exactly is the source data?

Read: [UCI — Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing)
and the included `data/raw/bank-additional-names.txt`.

Find the answers to:

- Why is `bank-additional-full.csv` different from the older `bank-full.csv`?
- What does `pdays=999` mean?
- Why does UCI say `duration` should be discarded for a realistic pre-call
  prediction?

## 2. How is the raw file loaded and inspected?

Read: [pandas — `read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html),
[`DataFrame.dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html),
and [`DataFrame.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html).

Ask:

- Why must this file specify `sep=";"`?
- What can exact row equality establish, and what can it not establish without
  a client or contact identifier?

## 3. Why split before learned preparation?

Read: [scikit-learn — common pitfalls and data leakage](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage)
and [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html).

Explain:

- Which preparation steps learn statistics or categories from data?
- Why should validation and test rows not determine those learned values?

## 4. How does one repeatable preprocessing pipeline work?

Read: [scikit-learn — `ColumnTransformer`](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html),
[`SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html),
[`OneHotEncoder`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html),
and [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html).

Map each component to the lab:

- Which columns receive median imputation and scaling?
- Which columns receive categorical encoding?
- What does `handle_unknown="ignore"` protect against?
- Why is saving the whole pipeline safer than saving only the classifier?
