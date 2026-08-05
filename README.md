# Power BI Onboarding Coach 🧑‍🍳

Ein KI-Skill, der dir **Power BI mit deinen eigenen Daten** beibringt — als
persönliches Onboarding-Erlebnis: Level-Einschätzung, individueller Lernpfad,
Schritt-für-Schritt-Aufgaben in Power BI Desktop, Checkpoints, Quizze und ein
gamifizierter Fortschritts-Tracker mit XP und Küchen-Badges. 🔪👨‍🍳🎨⭐

Du lädst eine CSV- oder Excel-Datei hoch, mit der du wirklich arbeitest — und
jede Übung, jedes DAX-Snippet und jede Quizfrage baut auf **deinen** Spalten
und **deinem** Business-Kontext auf.

**An AI skill that teaches you Power BI hands-on, using your own CSV/Excel
data** — with a personalized learning path, checkpoints, quizzes, XP and
badges. The skill itself is written in English and coaches you in your
language (German, English, …).

## Was drin steckt

| Modul | Inhalt |
|---|---|
| 1 · Foundations | Daten laden, Power Query, erste Visuals, Slicer, Refresh |
| 2 · Modeling & DAX | Sternschema, Beziehungen, Measures, CALCULATE, Zeitintelligenz |
| 3 · Visualization & IBCS | Declutter, Chart-Wahl, IBCS-Notation, Custom Visuals |
| 4 · Service & Sharing | Publish, Workspaces & Apps, Refresh, Mini-Governance |

Der Coach empfiehlt dir anhand deines Levels einen Einstieg — die Wahl hast du.

## Installation

### Claude.ai / Claude Desktop (einfachster Weg, keine Technik nötig)

1. Oben auf dieser GitHub-Seite: grüner Button **Code → Download ZIP**.
2. In Claude: **Einstellungen → Skills (Fähigkeiten) → Skill hochladen** und
   die ZIP auswählen.
3. Neuen Chat starten, Datendatei anhängen und schreiben:
   *„Bring mir Power BI bei"* — los geht's.

### Claude Code

```bash
git clone https://github.com/<owner>/powerbi-onboarding-coach.git ~/.claude/skills/powerbi-onboarding-coach
```

Danach in einem Projektordner mit deiner CSV/Excel einfach sagen:
*„Starte mein Power BI Onboarding mit sales.csv"*.

### Andere KI-Tools (ChatGPT, Copilot, …)

Der Skill ist reines Markdown ohne Tool-Abhängigkeiten. Kopiere den Inhalt von
[`SKILL.md`](SKILL.md) als System-/Projektanweisung und hänge bei Bedarf die
Dateien aus [`references/`](references/) an, wenn das Tool danach fragt
(die `SKILL.md` sagt dem Modell, wann es welche Datei braucht).

## Voraussetzungen

- **Power BI Desktop** (kostenlos): https://aka.ms/pbidesktopstore
- Eine CSV- oder Excel-Datei mit Daten, die dich interessieren
  (keine da? Der Coach generiert dir einen realistischen Übungsdatensatz)
- Für Modul 4: ein Arbeits-/Schulkonto mit Power-BI-Zugang (optional)

## Fortschritt & Gamification

Der Coach führt eine kleine Datei `powerbi-coach-progress.json` und generiert
daraus `my-powerbi-progress.html` — deine persönliche Fortschritts-Seite mit
XP-Balken, Levels (Dishwasher → Head Chef) und Badges. Damit kannst du das
Onboarding jederzeit unterbrechen und in einer späteren Session fortsetzen.

## Verwandte Ressourcen

- 📺 [Daten-WG Knowledge Kitchen](https://datenwgknowledgekitchen.com/) —
  deutschsprachige Video-Bibliothek rund um Power BI, Fabric & IBCS
- 📊 [IBCS Custom Visuals by Daten-WG](https://github.com/Losveratos/Power-BI-Custom-Visuals-byDatenWG) —
  kostenlose IBCS-Visuals (Waterfall, Variance, KPI …)
- 🎓 [Microsoft Learn: Get started with Power BI](https://learn.microsoft.com/training/paths/get-started-power-bi/)

## Lizenz

MIT — nutzen, teilen, verbessern ausdrücklich erwünscht.
