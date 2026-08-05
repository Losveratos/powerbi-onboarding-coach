# Module 2 — Data Modeling & DAX

Audience: Explorers and Practitioners (Module 1 or equivalent required).
XP: 50 per lesson, module badge: **Saucier** 🥣
Estimated effort: 90–120 minutes across 5 lessons.

If the user's data is a single flat table, that's fine — Lessons 2.1–2.2 build
the star schema FROM it (dimension tables via Power Query reference +
remove-duplicates). If they uploaded multiple tables/sheets, use those.

## Lesson 2.1 — Why a star schema (and build the date table)

- Context: flat tables work until they don't — one fact table + dimension
  tables is how every serious Power BI model is built. Kitchen metaphor: mise
  en place — ingredients sorted into bowls before cooking.
- Task: create a date table covering WHOLE years — time intelligence (YTD, PY
  in 2.5) only behaves predictably on complete years. Provide copy-paste DAX:
  `Date = CALENDAR(DATE(YEAR(MIN(<Fact>[<DateCol>])),1,1), DATE(YEAR(MAX(<Fact>[<DateCol>])),12,31))`
  plus Year/Month/MonthNo columns via `FORMAT`/`MONTH`. Mark as date table.
- Checkpoint: "How many rows does your Date table have?" (should be full
  years × 365/366 — verify against the profiled date range).
- Quiz idea: why not just use the date column in the fact table? (auto
  date/time pitfalls, shared calendar across facts).

## Lesson 2.2 — Relationships

- Task: build a dimension table from their data if needed (Power Query:
  Reference → keep key columns → Remove Duplicates), then connect in Model
  view: drag key → key. Explain 1:* direction and single-direction filtering
  with THEIR columns as the example.
- Checkpoint: describe the model view — which tables, which lines, 1 and * on
  the right ends?
- Quiz idea: "Filter flows from the 1-side to the *-side — so if you put
  [DimColumn] on a chart, why does [Measure] change?"

## Lesson 2.3 — First measures

- Context: implicit aggregation is training wheels; explicit measures are the
  craft. From here on, every number on a report should be a measure.
- Task: create a measures table (Enter Data, empty, named `_Measures`), then
  2–3 measures on their columns, e.g. `Total Revenue = SUM(...)`,
  `Order Count = COUNTROWS(...)`, `Avg per Order = DIVIDE([Total Revenue],[Order Count])`.
  Explain DIVIDE vs `/` (divide-by-zero safety).
- Checkpoint: card visual with the new measure — does the total match the
  profile expectation?
- Quiz idea: measure vs calculated column — when which? (row context vs filter
  context, storage).

## Lesson 2.4 — CALCULATE, the one function to rule them all

- Context: CALCULATE changes the filter context — 80% of practical DAX is
  CALCULATE + time intelligence.
- Task: 2 measures with their data, e.g.
  `Revenue <TopSegment> = CALCULATE([Total Revenue], <Dim>[<Col>] = "<value>")` and a
  `% of Total = DIVIDE([Total Revenue], CALCULATE([Total Revenue], ALL(<Dim>)))`.
- Checkpoint: matrix with dimension × both measures; do the percentages sum to
  100%?
- Quiz idea: predict-the-number — "before you click: what will
  [Revenue <TopSegment>] show in the row for <other segment>?" (Answer: the same
  value everywhere / the override effect — great aha moment.)

## Lesson 2.5 — Time intelligence

- Requires the date table from 2.1 marked as date table.
- Task: `Revenue YTD = TOTALYTD([Total Revenue], 'Date'[Date])` and
  `Revenue PY = CALCULATE([Total Revenue], SAMEPERIODLASTYEAR('Date'[Date]))`,
  plus `Δ PY % = DIVIDE([Total Revenue]-[Revenue PY],[Revenue PY])`. Line
  chart: month × Revenue and Revenue PY.
- Checkpoint: does PY show empty for the first year of data? (Expected —
  explain why.)
- Quiz: 3-question module final (context transition, CALCULATE behavior, when
  YTD resets).

Module wrap-up: award **Saucier** 🥣 (the station chef who masters the sauces
— DAX is the sauce), update tracker. Natural next step:
Module 3 (make the numbers look professional — IBCS) or Module 4 (share the
model with the team). MS Learn links: resources.md § Module 2.
