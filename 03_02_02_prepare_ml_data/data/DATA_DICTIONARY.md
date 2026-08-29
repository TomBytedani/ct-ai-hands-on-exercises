# `bank-additional-full.csv` data dictionary

This is a concise learning aid derived from UCI's included
`bank-additional-names.txt`. Consult that original file when deciding how to
interpret a field.

The target is `y`: whether the client subscribed to a term deposit (`yes` or
`no`). The exercise defines prediction time as immediately before a scheduled
call begins.

| Group | Columns | Raw type and relevant semantics |
| --- | --- | --- |
| Client | `age` | Numeric age |
| Client | `job`, `marital`, `education` | Categorical; some values are `unknown` |
| Client | `default`, `housing`, `loan` | Categorical yes/no information; some values are `unknown` |
| Current campaign | `contact`, `month`, `day_of_week` | Categorical call context known for a scheduled contact |
| Current campaign | `duration` | Numeric call duration; unavailable before the call and therefore leakage for this task |
| Current campaign | `campaign` | Number of contacts in the current campaign including this contact |
| Previous campaigns | `pdays` | Days since previous contact; `999` means never previously contacted |
| Previous campaigns | `previous` | Number of contacts before the current campaign |
| Previous campaigns | `poutcome` | Previous campaign outcome |
| Economic context | `emp.var.rate` | Quarterly employment-variation rate |
| Economic context | `cons.price.idx` | Monthly consumer-price index |
| Economic context | `cons.conf.idx` | Monthly consumer-confidence index |
| Economic context | `euribor3m` | Daily three-month Euribor rate |
| Economic context | `nr.employed` | Quarterly number-of-employees indicator |

The source contains no client or call identifier. Equality across every
published field therefore does not prove that two rows represent the same
real-world contact.
