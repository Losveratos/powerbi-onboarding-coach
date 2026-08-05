# Module 1 — Foundations (load, clean, first visuals)

Audience: Newcomers and Explorers. XP: 40 per lesson, module badge: **Prep Cook** 🔪
Estimated effort: 60–90 minutes across 5 lessons. Fine to split over sessions.

Teach one lesson per exchange-cycle, following the lesson rhythm from SKILL.md
(context → guided task → checkpoint → quiz → XP).

## Lesson 1.1 — Get the data in

- Context: everything in Power BI starts with Get Data; their file is the ingredient.
- Task: open Power BI Desktop → Get Data → Text/CSV (or Excel workbook) →
  navigate to their file → **Transform Data** (not Load! — explain that this
  detour through Power Query is the pro habit).
- Checkpoint: "What does the preview show — how many columns, and do the
  headers look right?" Compare against the data profile.
- Quiz idea: "What's the difference between *Load* and *Transform Data*?"

## Lesson 1.2 — Clean it in Power Query

- Context: 80% of real BI work is data prep; Power Query records every step so
  cleaning is repeatable — next month's file cleans itself.
- Task: fix THE quirks found in profiling (pick 1–3): set correct data types
  (especially the date column), remove duplicates, rename cryptic columns,
  unpivot if crosstab-shaped. Give exact ribbon click paths. If a step needs
  M code, provide it copy-paste ready with one sentence of what it does.
- Checkpoint: "Look at the Applied Steps list on the right — read me the steps
  you now have." Then: Close & Apply.
- Quiz idea: "Next month you get a new file with the same problems. What do
  you have to redo in Power Query? (Answer: nothing — just refresh.)"

## Lesson 1.3 — First visual & the insight moment

- Context: now the fun part — from table to picture in three clicks.
- Task: build a bar/column chart with their most interesting dimension ×
  main measure (from the profile's teaching plan). Then sort it descending.
- Checkpoint: "Which [dimension value] is biggest, and roughly what value does
  it show?" — verify against profile expectations. Make this a small
  celebration: they just produced their first real insight from their own data.
- Quiz idea: which visual for which question (trend → line, share → bar, ...).

## Lesson 1.4 — Slice, dice, filter

- Context: interactivity is Power BI's superpower over static Excel charts.
- Task: add a slicer (second dimension), add a card with the total of the main
  measure, click around and watch cross-filtering; then one page-level filter.
- Checkpoint: "Set the slicer to [specific value] — what does the card show
  now?" Verify plausibility.
- Quiz idea: difference between a slicer and a filter pane filter.

## Lesson 1.5 — Save, refresh, mini-dashboard

- Context: wrap the basics into something they'd actually show a colleague.
- Task: arrange 3–4 visuals on one page (card, bar, line-over-time if a date
  column exists, slicer), give the page a title text box, save the .pbix.
  Then the magic trick: change/add a row in the source file, hit Refresh,
  watch the report update.
- Checkpoint: screenshot or description of their page; confirm Refresh worked.
- Quiz: 3-question module final, mixing the previous topics, adapted to their
  data.

Module wrap-up: recap (load → clean → visualize → interact → refresh), award
**Prep Cook** badge, update tracker, recommend Module 2 (if they want to
understand the "why" behind numbers: modeling & DAX) or Module 3 (if they want
prettier, more professional reports next).

MS Learn follow-up link for this module: see resources.md § Module 1.
