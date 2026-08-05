# Profiling the user's data

Goal: understand the uploaded CSV/Excel well enough to build every exercise on
it, and give the user a short friendly summary. Never dump raw profiling output
at the user.

## How to profile

With code execution available, prefer a quick script (Python/pandas or
equivalent). Chat-only: ask for headers + ~20 pasted rows and infer.

Collect:

1. **Shape**: row count, column count, sheet names (Excel).
2. **Column types**: date, number, text/category, ID-like, boolean.
3. **Date columns**: min/max range, granularity (daily? monthly?). A usable
   date column unlocks time-intelligence lessons.
4. **Candidate measures**: numeric columns that make sense to sum/average
   (revenue, cost, quantity, hours...). Note likely units/currency.
5. **Candidate dimensions**: low-cardinality text columns (region, category,
   product, customer, status...) — count distinct values for each.
6. **Quality quirks** (these become teaching moments, not problems!): missing
   values, mixed types, dates stored as text, thousand separators, duplicate
   rows, inconsistent casing, wide "crosstab" layout (months as columns).
7. **Shape classification**:
   - *Flat transactional table* → ideal; supports all modules.
   - *Wide crosstab* → great Power Query unpivot lesson in Module 1.
   - *Multiple sheets/tables* → great modeling material for Module 2.
   - *Pre-aggregated tiny table* → fine for Module 1 & 3; for Module 2 offer
     to generate a richer companion dataset.

## Derived teaching plan (internal)

From the profile, note internally:

- Which 2–3 measures the first chart should use.
- Which dimension gives the most interesting first "insight moment" (pick one
  where values genuinely differ — a bar chart where all bars are equal teaches
  nothing).
- Which quirk to use for the data-cleaning lesson.
- Whether a date table lesson is possible (real date column) or needs the
  generated-data fallback.
- Realistic expected values for checkpoints (e.g. "total revenue should be
  around 1.2M" ) so you can verify the user's results later.

## The friendly summary (user-facing)

2–5 sentences, their language, e.g.:

> "Nice — 1,842 rows of sales, one row per order line, from Jan 2024 to
> Jun 2026. I can see revenue and quantity to calculate with, and region,
> product and channel to slice by. Two little quirks we'll clean up together:
> dates are stored as text, and 12 rows are duplicated. Perfect ingredients —
> let's start cooking."

## If the user has no data

Offer to generate a practice dataset tailored to their industry (ask 1
question: "What field do you work in?"). Generate a CSV with ~500–2000 rows,
one date column spanning ~2 years, 2–3 measures, 3–4 dimensions, and 2–3
built-in quality quirks (they make Module 1 realistic). Save it (or provide as
download) and profile it as above.
