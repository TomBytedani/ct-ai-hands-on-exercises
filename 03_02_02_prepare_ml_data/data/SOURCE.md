# UCI Bank Marketing dataset source

This directory contains the `bank-additional-full.csv` variant of the Bank
Marketing dataset. The raw files are preserved unchanged so the lab can make
its preparation decisions explicit and reproducible.

## Attribution

- Dataset: Bank Marketing
- Creators: Sérgio Moro, Paulo Rita, and Paulo Cortez
- Publisher: UCI Machine Learning Repository
- DOI: <https://doi.org/10.24432/C5K306>
- Canonical page: <https://archive.ics.uci.edu/dataset/222/bank+marketing>
- Download archive: <https://archive.ics.uci.edu/static/public/222/bank%2Bmarketing.zip>
- Retrieved: 2026-08-29
- License: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

Suggested citation:

> Moro, S., Rita, P., & Cortez, P. (2014). Bank Marketing [Dataset].
> UCI Machine Learning Repository. https://doi.org/10.24432/C5K306

## Included raw files

- `raw/bank-additional-full.csv` -- 41,188 examples, 20 input attributes, and
  the binary target `y`; semicolon-delimited and ordered from May 2008 through
  November 2010.
- `raw/bank-additional-names.txt` -- the field documentation distributed with
  the canonical archive.

The CSV has 36,548 `no` targets and 4,640 `yes` targets.

## Integrity

- UCI outer ZIP SHA-256:
  `E0BF5F5DE5B846E2F18E9D90606637267D46DFA260E0F17BB12E605DB5EFBEB4`
- `bank-additional-full.csv` SHA-256:
  `74ADFC578BF77A7FF4BB1BA4A9F8709D9E3C6907342959C2C8416847E0AFB4D8`

## Important source semantics

- The target `y` records whether the client subscribed to a term deposit.
- Literal `unknown` values represent missing information in several
  categorical attributes.
- `pdays=999` means that the client was not previously contacted.
- `duration` is only known after a call. UCI states that it should be excluded
  when building a realistic model intended to make predictions before a call.

These facts describe the source. The guided exercise will ask the learner to
decide and document the applicable preparation steps rather than silently
altering the raw data.
