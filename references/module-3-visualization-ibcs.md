# Module 3 — Visualization & IBCS report design

Audience: anyone past Module 1. XP: 50 per lesson, module badge: **Plating Artist** 🎨
Estimated effort: 60–90 minutes across 4 lessons.

## Lesson 3.1 — Less is more (declutter)

- Context: the goal of a report is a decision, not decoration. Most default
  charts carry noise — we remove it.
- Task: take a chart from their report (or build one): remove unneeded
  legend/gridlines/shadows, direct-label instead of axis where sensible, one
  font, aligned visuals, sensible title that states the MESSAGE ("Revenue up
  12% driven by <top segment>") instead of a label ("Revenue by segment").
- Checkpoint: before/after — ask what they removed and what got clearer.
- Quiz idea: what belongs in a chart title?

## Lesson 3.2 — The right chart for the question

- Task: 3 mini-exercises on their data: trend over time (line), ranking (bar,
  sorted), part-to-whole (stacked bar or 100% — and why pie gets the side-eye
  beyond 2–3 slices). Let THEM pick the visual first, then discuss.
- Checkpoint: their three charts, right types, sorted correctly.
- Quiz idea: match question → chart type (4 pairs).

## Lesson 3.3 — IBCS in 20 minutes

- Context: IBCS (International Business Communication Standards) = a notation
  standard so every report reads the same way: actual/previous-year/plan/
  forecast always look identical, variances always visible. Companies adopt it
  because readers stop re-learning every report.
- Teach the visual core (keep it practical):
  - Scenario notation: AC solid dark, PY grey, PL/BU outlined, FC hatched.
  - Show variances, not just values: ΔPY, ΔPL as bars, green = good / red =
    bad **relative to business impact** (cost up = red even though the number
    grew).
  - No color decoration; color = meaning only. Uniform scales on comparable
    charts.
- Task: convert one of their charts to IBCS style with core visuals (e.g.
  column chart AC vs PY with a variance chart above it — conditional
  formatting for red/green). If their data has no plan/PY scenario, derive PY
  from time intelligence (Module 2.5) or compare two segments.
- Checkpoint: screenshot/description; is good/bad coloring semantically right
  for their KPI?
- Quiz idea: "Revenue +8%, Costs +8% — which is green, which is red, why?"

## Lesson 3.4 — IBCS custom visuals & finishing the dashboard

- Context: core visuals can fake IBCS, but purpose-built custom visuals do
  waterfalls/variance charts natively.
- Point to the free Daten-WG IBCS visuals:
  https://github.com/Losveratos/Power-BI-Custom-Visuals-byDatenWG — explain
  how to import a .pbiviz (Visualizations pane → ⋯ → Import a visual from a
  file) and that organizational deployment goes via the admin portal.
- Task: rebuild their variance view with a suitable custom visual (e.g. a
  waterfall for the ΔPY bridge), OR — if they can't install visuals — polish
  the core-visual version. Then final dashboard assembly: KPI cards top-left,
  most important chart top, details below, consistent titles.
- Checkpoint: the finished page. Give one round of concrete, kind design
  feedback (max 3 suggestions).
- Quiz: module final — 3 questions on decluttering, chart choice, IBCS
  semantics.

Module wrap-up: award **Plating Artist**, update tracker. German speakers:
point to the Visualisierung & IBCS bucket on
https://datenwgknowledgekitchen.com/ for video deep dives. Next: Module 4 to
put the dashboard in front of the team.
