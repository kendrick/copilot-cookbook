# Project Overview

## What This Is
A wikilinked Obsidian knowledge base of Microsoft 365 Copilot, built for an executive-coaching curriculum — audience is business leaders, not developers.

## Stack
- Language: Obsidian-flavored Markdown (no code, no build step)
- Framework: Obsidian vault (a wikilink graph)
- Styling: n/a
- Data layer: YAML frontmatter per note
- Deployment: none — a git-tracked vault opened directly in Obsidian

## Repository Structure
- Feature and category notes at repo root (`Word.md`, `Copilot Chat.md`, …)
- `Plays/` — scenario-first recipes that chain features
- `Copilot Features MOC.md` + `Plays MOC.md` — the two entry-point maps
- `_sources.md` — every source URL with its `fetched` date
- `_research/` — gitignored fetch distillations plus the canonical MANIFEST
- `_working-memory/`, `scripts/` — working-memory-kit scaffolding

## Key Constraints
- Every claim traces to a live Microsoft page fetched 2026-07-07.
- The wikilink graph must stay at 0 broken links and 0 orphans.
- Any new note must be registered in `_research/MANIFEST.md` (exact title = filename = wikilink target) *before* it's linked, or the graph breaks.
- `Plays MOC.md` groups plays by **business need** (analyze data, catch up, draft from messy inputs, prep for a meeting, build a deck, automate a recurring task, research a topic), never by app — that grouping is the fast lookup when a leader states a problem.
- Two plays are load-bearing for the coaching curriculum and must survive any rebuild: "Build a Copilot Notebook for a recurring project status" and "Draft an Excel pivot from a Chat-generated prompt" (the latter must show BOTH prompts — the one asking Chat to write the Excel prompt, and the resulting prompt pasted into Excel).
