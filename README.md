# Power BI Onboarding Coach 🧑‍🍳

**Deutsch** · [English below ⬇️](#english)

Ein KI-Skill, der dir **Power BI mit deinen eigenen Daten** beibringt — als
persönliches Onboarding-Erlebnis: Level-Einschätzung, individueller Lernpfad,
Schritt-für-Schritt-Aufgaben in Power BI Desktop, Checkpoints, Quizze und ein
gamifizierter Fortschritts-Tracker mit XP und Küchen-Badges. 🔪🥣🎨⭐

Du bringst eine CSV- oder Excel-Datei mit, mit der du wirklich arbeitest — und
jede Übung, jedes DAX-Snippet und jede Quizfrage baut auf **deinen** Spalten
und **deinem** Business-Kontext auf. Der Skill ist auf Englisch geschrieben,
der Coach antwortet in **deiner** Sprache.

## Was drin steckt

| Modul | Inhalt | Badge |
|---|---|---|
| 1 · Foundations | Daten laden, Power Query, erste Visuals, Slicer, Refresh | 🔪 Prep Cook |
| 2 · Modeling & DAX | Sternschema, Beziehungen, Measures, CALCULATE, Zeitintelligenz | 🥣 Saucier |
| 3 · Visualization & IBCS | Declutter, Chart-Wahl, IBCS-Notation, Custom Visuals | 🎨 Plating Artist |
| 4 · Service & Sharing | Publish, Workspaces & Apps, Refresh, Mini-Governance | ⭐ Maître d' |

Der Coach empfiehlt dir anhand deines Levels einen Einstieg — die Wahl hast du.

## Installation

### Claude.ai / Claude Desktop (einfachster Weg, keine Technik nötig)

1. `powerbi-onboarding-coach.zip` von der [neuesten Release](https://github.com/Losveratos/powerbi-onboarding-coach/releases/latest) herunterladen.
   (**Nicht** den grünen „Code → Download ZIP"-Button nehmen — GitHub packt dort
   alles in einen Ordner `…-main`, und der Skill-Upload erwartet den Ordnernamen
   `powerbi-onboarding-coach`.)
2. In Claude: **Einstellungen → Fähigkeiten (Skills) → Skill hochladen** und die ZIP auswählen.
3. Fertig — weiter bei „So benutzt du den Coach".

### Claude Code

```bash
git clone https://github.com/Losveratos/powerbi-onboarding-coach.git ~/.claude/skills/powerbi-onboarding-coach
```

### Andere KI-Tools (ChatGPT, Copilot, …)

Der Skill ist reines Markdown ohne Tool-Abhängigkeiten: Inhalt von
[`SKILL.md`](SKILL.md) als System-/Projektanweisung einfügen; die Dateien aus
[`references/`](references/) und [`assets/`](assets/) bei Bedarf mitgeben
(die SKILL.md sagt dem Modell, wann es welche Datei braucht).

## So benutzt du den Coach (How to use)

1. **Voraussetzung:** [Power BI Desktop](https://aka.ms/pbidesktopstore)
   installieren (kostenlos). Der Coach hilft auch dabei.
2. **Neuen Chat starten** und deine CSV-/Excel-Datei anhängen — irgendwas,
   womit du wirklich arbeitest (Verkaufszahlen, Projektliste, Exporte …).
   Keine Daten zur Hand? Der Coach generiert dir einen realistischen
   Übungsdatensatz aus deiner Branche.
3. **Einfach lostippen**, z. B.:
   - *„Bring mir Power BI bei — hier sind meine Daten."*
   - *„Ich kenne die Basics, aber DAX verwirrt mich. Coach mich!"*
4. **Der Coach fragt zuerst**: dein Level, dein Vorwissen, dein Ziel. Danach
   empfiehlt er dir einen Lernpfad — entscheiden tust du.
5. **Dann geht's los**: kleine Aufgaben, die **du** in Power BI Desktop
   klickst (mit Copy-Paste-DAX vom Coach), Checkpoints („was zeigt deine
   Karte jetzt an?"), Mini-Quizze, XP und Badges.
6. **Pausieren jederzeit.** Der Coach speichert `powerbi-coach-progress.json`
   und generiert `my-powerbi-progress.html` — deine persönliche
   Fortschritts-Seite. Nächste Session einfach sagen: *„Lass uns mit meinem
   Power BI Kurs weitermachen"* (Fortschrittsdatei anhängen, falls der Chat
   sie nicht mehr hat).

**Tipp:** Ehrlich antworten beim Level — der Coach passt Tempo und Tiefe an.
Falsche Quiz-Antworten kosten nichts — dir entgehen höchstens ein paar
Bonus-XP. 😄

## Verwandte Ressourcen

- 📺 [Daten-WG Knowledge Kitchen](https://datenwgknowledgekitchen.com/) — deutschsprachige Video-Bibliothek zu Power BI, Fabric & IBCS
- 📊 [IBCS Custom Visuals by Daten-WG](https://github.com/Losveratos/Power-BI-Custom-Visuals-byDatenWG) — kostenlose IBCS-Visuals
- 🎓 [Microsoft Learn: Get started with Power BI](https://learn.microsoft.com/training/paths/get-started-power-bi/)

---

<a name="english"></a>
# English

An AI skill that teaches you **Power BI hands-on with your own data** — as a
personal onboarding experience: level assessment, a personalized learning
path, step-by-step tasks in Power BI Desktop, checkpoints, quizzes, and a
gamified progress tracker with XP and kitchen badges. 🔪🥣🎨⭐

You bring a CSV or Excel file you actually work with — every exercise, DAX
snippet, and quiz question is built on **your** columns and **your** business
context. The skill is written in English and coaches you in **your** language.

## What's inside

| Module | Content | Badge |
|---|---|---|
| 1 · Foundations | Load data, Power Query, first visuals, slicers, refresh | 🔪 Prep Cook |
| 2 · Modeling & DAX | Star schema, relationships, measures, CALCULATE, time intelligence | 🥣 Saucier |
| 3 · Visualization & IBCS | Decluttering, chart choice, IBCS notation, custom visuals | 🎨 Plating Artist |
| 4 · Service & Sharing | Publish, workspaces & apps, refresh, governance basics | ⭐ Maître d' |

The coach recommends a starting point based on your level — the choice is yours.

## Installation

### Claude.ai / Claude Desktop (easiest, no tech skills needed)

1. Download `powerbi-onboarding-coach.zip` from the [latest release](https://github.com/Losveratos/powerbi-onboarding-coach/releases/latest).
   (**Not** the green "Code → Download ZIP" button — GitHub wraps everything in
   a `…-main` folder there, and the skill upload expects the folder to be named
   `powerbi-onboarding-coach`.)
2. In Claude: **Settings → Skills → Upload skill**, pick the ZIP.
3. Done — continue with "How to use".

### Claude Code

```bash
git clone https://github.com/Losveratos/powerbi-onboarding-coach.git ~/.claude/skills/powerbi-onboarding-coach
```

### Other AI tools (ChatGPT, Copilot, …)

The skill is plain Markdown with no tool dependencies: paste the contents of
[`SKILL.md`](SKILL.md) as a system/project instruction and provide the files
from [`references/`](references/) and [`assets/`](assets/) when needed
(SKILL.md tells the model when to read which file).

## How to use

1. **Prerequisite:** install [Power BI Desktop](https://aka.ms/pbidesktopstore)
   (free). The coach can help with this too.
2. **Start a new chat** and attach your CSV/Excel file — anything you actually
   work with (sales figures, project lists, exports…). No data at hand? The
   coach generates a realistic practice dataset for your industry.
3. **Just start typing**, e.g.:
   - *"Teach me Power BI — here's my data."*
   - *"I know the basics but DAX confuses me. Coach me!"*
4. **The coach interviews you first**: your level, prior knowledge, your goal.
   Then it recommends a learning path — you decide.
5. **Then it's hands-on**: small tasks that **you** click through in Power BI
   Desktop (with copy-paste DAX from the coach), checkpoints ("what does your
   card show now?"), mini quizzes, XP and badges.
6. **Pause anytime.** The coach maintains `powerbi-coach-progress.json` and
   generates `my-powerbi-progress.html` — your personal progress page. Next
   session, just say: *"Let's continue my Power BI course"* (attach the
   progress file if the chat no longer has it).

**Tip:** Answer the level questions honestly — the coach adapts pace and
depth. Wrong quiz answers cost nothing — you just miss out on a few bonus
XP. 😄

## Related resources

- 📺 [Daten-WG Knowledge Kitchen](https://datenwgknowledgekitchen.com/) — German-language video library on Power BI, Fabric & IBCS
- 📊 [IBCS Custom Visuals by Daten-WG](https://github.com/Losveratos/Power-BI-Custom-Visuals-byDatenWG) — free IBCS visuals
- 🎓 [Microsoft Learn: Get started with Power BI](https://learn.microsoft.com/training/paths/get-started-power-bi/)

## License / Lizenz

MIT — use, share, improve. / Nutzen, teilen, verbessern ausdrücklich erwünscht.
