# Project Overview

## What This Is
An Obsidian knowledge base of Microsoft 365 Copilot, built for an executive-coaching curriculum — audience is business leaders, not developers.

## Stack
- Language: Obsidian-flavored Markdown (no code, no build step)
- Framework: Obsidian vault; internal links are relative markdown links (not wikilinks), so it also renders as plain md outside Obsidian
- Styling: n/a
- Data layer: YAML frontmatter per note
- Deployment: none — a git-tracked vault opened directly in Obsidian

## Repository Structure
- `Surfaces/<Surface>/` — one folder per surface (Word, Excel, Copilot Chat, …); each folder's `README.md` is the surface index and its feature notes sit beside it
- `Surfaces/README.md` — map of all surfaces (was `Copilot Features MOC`)
- `Recipes/` — scenario-first recipes that chain features; `Recipes/README.md` is their index (was `Plays MOC`)
- `README.md` — vault front door
- `_sources.md` — every source URL with its `fetched` date
- `_research/` — gitignored fetch distillations plus the MANIFEST
- `_working-memory/`, `scripts/` — working-memory-kit scaffolding

## Key Constraints
- Every claim traces to a live Microsoft page fetched 2026-07-07.
- The link graph must stay at 0 broken links and 0 orphans — check with `scripts/verify_graph.py` after any move or new note.
- Links are relative markdown links resolved by path, so filenames no longer need to be globally unique (every surface folder reuses `README.md`). The `_research/MANIFEST.md` name registry is legacy from the wikilink era and no longer gates linking.
- `Recipes/README.md` groups recipes by **business need** (analyze data, catch up, draft from messy inputs, prep for a meeting, build a deck, automate a recurring task, research a topic), never by app — that grouping is the fast lookup when a leader states a problem.
- Two recipes are load-bearing for the coaching curriculum and must survive any rebuild: "Build a Copilot Notebook for a Recurring Project Status" and "Draft an Excel Pivot From a Chat-Generated Prompt" (the latter must show BOTH prompts — the one asking Chat to write the Excel prompt, and the resulting prompt pasted into Excel).
