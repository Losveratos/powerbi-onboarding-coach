# Changelog

## v1.1.0 — 2026-08-05

- **Install:** release workflow builds a `powerbi-onboarding-coach.zip` with the
  correct root folder name for the Claude skill upload; README points to the
  release instead of GitHub's `Code → Download ZIP` (whose `…-main` folder name
  breaks the upload).
- **Badges renamed** to avoid collision with the XP level names: Module 2
  👨‍🍳 Sous Chef → 🥣 Saucier, Module 4 ⭐ Head Chef → ⭐ Maître d'. The tracker
  maps old badge names in existing progress files automatically.
- **Quiz streak persists:** new `quizStats.currentStreak` field in
  `powerbi-coach-progress.json` so the 🧠 Quiz Streak badge survives session
  breaks.
- **Tracker i18n:** `my-powerbi-progress.html` now renders German or English
  based on the `language` field in the progress file (labels, statuses, quiz
  line, footer, genitive-correct title).
- **Locale pitfalls lesson:** Module 1 and the data-profiling reference now
  cover semicolon CSVs, comma decimals and DD.MM.YYYY dates ("Using Locale" in
  Power Query) — the most common first-import blocker for European users.
- **Date table best practice:** Module 2 builds the calendar over whole years
  so YTD/PY behave predictably.
- **Trigger tuning:** SKILL.md description adds German trigger phrases and an
  explicit "do NOT use when the analysis should be done FOR the user" rule;
  frontmatter now carries `license` and `metadata.version`.

## v1.0.0 — 2026-08

- Initial release: SKILL.md coaching flow (intake interview → data profiling →
  module choice → lesson rhythm), 4 modules, gamification (XP, kitchen ranks,
  badges), HTML progress tracker in the Knowledge-Kitchen design, bilingual
  README.
