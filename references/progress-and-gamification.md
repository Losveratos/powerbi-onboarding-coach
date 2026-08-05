# Progress tracking & gamification

## XP table

| Event | XP |
|---|---|
| Complete a lesson (task + checkpoint) | Module 1: 40 · Modules 2/3: 50 · Module 4: 40 |
| Quiz question right on first try | +10 |
| Quiz question right after a hint | +5 |
| Module final quiz all correct | +25 bonus |
| Comeback (resuming after a previous session) | +15 "Consistency" bonus |

Levels by total XP: 0 = **Dishwasher** · 100 = **Kitchen Help** ·
250 = **Commis** · 450 = **Chef de Partie** · 700 = **Sous Chef** ·
1000 = **Head Chef**. Announce level-ups when they happen.

## Badges

| Badge | Earned by |
|---|---|
| 🔪 Prep Cook | Module 1 complete |
| 👨‍🍳 Sous Chef | Module 2 complete |
| 🎨 Plating Artist | Module 3 complete |
| ⭐ Head Chef | Module 4 complete |
| 💡 First Insight | First chart built from own data (Lesson 1.3) |
| 🧮 Measure Maker | First explicit DAX measure (Lesson 2.3) |
| 🧠 Quiz Streak | 5 quiz questions right on first try in a row |
| 🏆 Master of the Data Kitchen | All four modules complete |

## Progress file: `powerbi-coach-progress.json`

Keep it small and human-readable. Schema (all fields required unless noted):

```json
{
  "learner": "Anna",
  "language": "de",
  "level": "Newcomer",
  "goal": "Monatliches Sales-Reporting ersetzen",
  "dataset": {"file": "sales_2026.csv", "rows": 1842, "mainMeasure": "Revenue"},
  "xp": 240,
  "kitchenRank": "Kitchen Help",
  "badges": ["💡 First Insight", "🔪 Prep Cook"],
  "quizStats": {"asked": 9, "firstTry": 7},
  "modules": {
    "1": {"status": "done", "lessons": [1,2,3,4,5]},
    "2": {"status": "in-progress", "lessons": [1]},
    "3": {"status": "open", "lessons": []},
    "4": {"status": "open", "lessons": []}
  },
  "lastSession": "2026-08-05",
  "notes": "Datumsspalte war Text; Slicer-Konzept saß sofort."
}
```

`notes` is your coach memory — 1–3 short observations that help the next
session continue smoothly (sticking points, pace, preferences).

## HTML progress tracker

Template: `assets/progress-tracker.html`. It contains the marker line
`const PROGRESS = /*PROGRESS_DATA*/null;`. To generate: replace
`/*PROGRESS_DATA*/null` with the current JSON object, save as
`my-powerbi-progress.html` next to the progress file. Everything else in the
template is self-contained (no network access, works from disk, light/dark).

Regenerate after each lesson in file-capable environments; in chat-only
environments, generate it as an artifact/download at module completions and
keep a compact text scoreboard ("240 XP · Kitchen Help · 2 badges") in chat
otherwise.
