# Conventions

## Naming
Note title = filename = wikilink target, exactly. Register every new note in `_research/MANIFEST.md` before linking to it, so the graph never breaks.

## File Organization
Feature and category notes live at the repo root; plays live in `Plays/`; raw fetch distillations and the MANIFEST live in gitignored `_research/`.

## Prose
No hard line breaks anywhere, including commit messages — one unwrapped line per paragraph. Em dashes are never space-wrapped; chain them directly (`like—this`) or reach for other punctuation. The `- term — description` list bullet is the sanctioned exception. Keep title-case headings and bulleted/numbered lists. Run human-facing prose (notes, README, MOCs, commit messages) through the `humanizer` skill before merge.

## Sourcing
Every capability claim traces to a live Microsoft page. Don't invent UI steps a source doesn't show. Prefer the source's own wording over a more specific claim.

## Refresh (Copilot ships monthly)
Two passes, the same two that built the vault: (1) re-fetch every URL in `_sources.md` to re-establish the full surface, then (2) pull the newest monthly "What's New" posts and release notes and fold anything not already captured into its category tagged `new: true` — never a separate "new features" silo. Diff the `fetched` dates to see what moved. Delegate web fetching to Haiku sub-agents (user instruction). For JS-heavy marketing/adoption pages, prefix the URL with the `r.jina.ai/https://<url>` reader (the jina CLI isn't installed). Haiku agents sometimes stall asking for env context instead of executing — re-task them forcefully.

## Verify
Before claiming graph integrity or counts, run `python3 scripts/verify_graph.py` (expect 0 broken / 0 orphans) and `python3 scripts/stats.py` (feature/category/play counts). Both derive their root from the script location, so a repo rename won't break them. `verify_graph.py` skips the scaffolding docs (CLAUDE, AGENTS, PROMPT_*) and inline-code examples, so only real vault notes count.

## Enrich
To add more plays or per-app example prompts, the original fetch data with verbatim prompts lives in `_research/06-prompts-roles.md` (gitignored).
