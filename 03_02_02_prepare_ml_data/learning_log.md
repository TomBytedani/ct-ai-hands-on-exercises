# Lab 3.2.2 post-lab learning log

**Date:** 2026.09.01

**Starting confidence (1–5):** 2

**Ending confidence (1–5):** 4

Open this file only after the notebook tells you that the four handoff artifacts
have been created. Answer without reopening hints first.

Use your own words. This is a retrieval exercise, not a terminology or exact-
spelling test. If needed, remember that the prediction is made immediately
before the scheduled call starts; no information learned during or after the
call is a valid input.

## 1. Reconstruct the preparation workflow

Give one concrete example from the lab for each activity:

| Activity | What I did | Why it belonged to this activity |
| --- | --- | --- |
| Data acquisition | Downloaded the csv dataset | it just did |
| Data preprocessing | Several things, along OneHotEncoder, StandardSampler, SimpleImputer | |
| Feature engineering | Since 999 was removed from "pdays" column we track wether a client was previously contacted by introducing a new feature "previously_contacted" | |
| Exploratory data analysis | Visualized various plots and data to make informed decisions | |


## 2. Explain why each preparation choice was made

Complete each explanation in one or two sentences.

- `duration` (the completed call length) was removed because: it's recorded after the client calls, which is not predictive for the model we want to train
- Literal `unknown` values were retained as a category because: they may still be useful and we don't have context on the substitutes
- `pdays=999` was transformed rather than treated as 999 elapsed days because
  the source says: it would be treated like the other numerical values and skew the average upwards dramatically
- `previously_contacted` (a new 0/1 field) was added because: 999 was removed
- Exact matching rows were retained because: not enough evidence to mark them as duplicate
- Numerical scaling was performed because: not sure
- Data augmentation and sampling were not performed because: there wasn't the need for it

