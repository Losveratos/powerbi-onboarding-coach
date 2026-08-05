# Module 4 — Power BI Service: publish & share

Audience: anyone past Module 1. XP: 40 per lesson, module badge: **Head Chef** ⭐
Estimated effort: 45–60 minutes across 3 lessons.

Prerequisite check (ask before starting): do they have a work/school Microsoft
account with a Power BI license (Free/Pro/PPU) or Fabric capacity? Personal
accounts can't sign into the Service. If they have no license, teach the
concepts with screenshots-in-words and mark the hands-on parts as "when you
get access". A Fabric trial (if their tenant allows it) is a fine sandbox.

## Lesson 4.1 — Publish & find your way around

- Context: Desktop is the kitchen, the Service (app.powerbi.com) is the
  restaurant where people get served.
- Task: Publish from Desktop → My Workspace (or a test workspace). Tour:
  report vs. semantic model (two items appear — explain the difference!),
  editing vs. viewing, where Refresh lives now.
- Checkpoint: report opens in the browser; interactions work.
- Quiz idea: what are the TWO items that appeared in the workspace after
  publishing, and which one holds the data?

## Lesson 4.2 — Sharing done right

- Context: the #1 beginner mistake is emailing .pbix files. The Service has
  proper ways, each with an audience.
- Teach the ladder: share a report link (quick, small audience) → workspace
  roles (Viewer/Contributor/Member/Admin — teams building together) → **Apps**
  (the polished way to serve many viewers). Mention licensing reality briefly:
  viewers need Pro/PPU unless the workspace is on capacity (F/P SKU).
- Task: share the report with one colleague or their own second account;
  OR build a minimal app from the workspace if they have rights.
- Checkpoint: recipient can open it (or they can describe the app they built).
- Quiz idea: 40 sales reps need to SEE a dashboard, 2 analysts maintain it —
  who gets what role/license?

## Lesson 4.3 — Refresh & minimal governance

- Context: a published report is a promise that the numbers stay current.
- Teach: scheduled refresh needs the file source reachable from the cloud —
  local files need a Data Gateway (concept only: a bridge on a PC/server that
  the Service calls through). Better long-term: sources in SharePoint/OneLake/
  databases. Show where refresh schedule and failure notifications live.
- Governance-in-3-bullets: sensible workspace structure (not everything in My
  Workspace), naming conventions, know who owns each dataset.
- Task: set up a scheduled refresh (or a manual one + walk through the
  schedule dialog if no gateway), enable failure e-mails.
- Checkpoint: refresh history shows a successful run.
- Quiz: module final — items vs workspace vs app, when a gateway is needed,
  first thing to check when refresh fails.

Module wrap-up: award **Head Chef** ⭐, update tracker — if all four modules
are complete, award the grand badge **Master of the Data Kitchen** 🏆 and make
a small ceremony of it (recap of the whole journey, from first CSV load to a
shared, refreshing, IBCS-styled report — that's a real skill set now).
Suggest next steps from resources.md § Beyond (PL-300 path on MS Learn,
Daten-WG videos, community).
