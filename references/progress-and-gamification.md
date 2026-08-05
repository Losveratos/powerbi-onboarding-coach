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
| 🥣 Saucier | Module 2 complete |
| 🎨 Plating Artist | Module 3 complete |
| ⭐ Maître d' | Module 4 complete |
| 💡 First Insight | First chart built from own data (Lesson 1.3) |
| 🧮 Measure Maker | First explicit DAX measure (Lesson 2.3) |
| 🧠 Quiz Streak | 5 quiz questions right on first try in a row |
| 🏆 Master of the Data Kitchen | All four modules complete |

Badge names are deliberately distinct from the XP level names (levels use the
classic brigade ranks Dishwasher → Head Chef; module badges use kitchen
stations) — never mix the two when announcing progress.

## Progress file: `powerbi-coach-progress.json`

Keep it small and human-readable. Schema (all fields required unless noted):

```json
{
  "learner": "Anna",
  "language": "de",
  "level": "Newcomer",
  "goal": "Monatliches Sales-Reporting ersetzen",
  "dataset": {"file": "sales_2026.csv", "rows": 1842, "mainMeasure": "Revenue"},
  "xp": 330,
  "kitchenRank": "Commis",
  "badges": ["💡 First Insight", "🔪 Prep Cook"],
  "quizStats": {"asked": 9, "firstTry": 7, "currentStreak": 3},
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

`quizStats.currentStreak` counts consecutive first-try-correct answers and
resets to 0 on any miss — it must live in the file so the 🧠 Quiz Streak badge
(5 in a row) survives a session break. Once the badge is earned, keep counting
but don't award it again.

## HTML progress tracker

Template: `assets/progress-tracker.html`. It contains the marker line
`const PROGRESS = /*PROGRESS_DATA*/null;`. To generate: replace
`/*PROGRESS_DATA*/null` with the current JSON object, save as
`my-powerbi-progress.html` next to the progress file. Everything else in the
template is self-contained (no network access, works from disk).

The tracker deliberately follows the design system of the Daten-WG Knowledge
Kitchen site (https://datenwgknowledgekitchen.com/): paper background
`#FAFAF5`, white cards with `#E7E4DB` hairlines, petrol green accent
`#117865`, warm orange `#C25A2D` only for "now/active" states, Segoe UI
variable font stack, uppercase letter-spaced eyebrow labels with a short
leading line, and a 4px colored left border per module (blue `#166088`, teal
`#2A857A`, dark red-brown `#5C2E2E`, red `#8B2E2E`). If you ever extend or
rebuild the tracker, keep this visual language so it feels like part of the
Knowledge Kitchen family.

Regenerate after each lesson in file-capable environments; in chat-only
environments, generate it as an artifact/download at module completions and
keep a compact text scoreboard ("240 XP · Kitchen Help · 2 badges") in chat
otherwise.
