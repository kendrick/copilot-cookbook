# Conventions

## Naming
Filename is the human-readable note title. Each surface folder's index is its `README.md`.

## File Organization
Feature notes live under `Surfaces/<Surface>/` beside that surface's `README.md` index; recipes live in `Recipes/`; raw fetch distillations live in gitignored `_research/`.

## Links
Body links are relative markdown links, URL-encoded (`[Title](../Excel/Suggest%20Formulas%20in%20Excel.md)`). Recipe frontmatter `uses:` keeps Obsidian `[[wikilinks]]` on purpose — it's metadata, resolved by name, and stripped on export. We left wikilinks for Loop portability, which costs Obsidian's auto-update-on-rename: after moving or renaming any note, recompute relative links and re-run `scripts/verify_graph.py`.

## Prose
No hard line breaks anywhere, including commit messages — one unwrapped line per paragraph. Em dashes are never space-wrapped; chain them directly (`like—this`) or reach for other punctuation. The `- term — description` list bullet is the sanctioned exception. Keep title-case headings and bulleted/numbered lists. Run human-facing prose (notes, README, MOCs, commit messages) through the `humanizer` skill before merge.

## Sourcing
Every capability claim traces to a live Microsoft page. Don't invent UI steps a source doesn't show. Prefer the source's own wording over a more specific claim.

## Refresh (Copilot ships monthly)
Two passes, the same two that built the vault: (1) re-fetch every URL in `_sources.md` to re-establish the full surface, then (2) pull the newest monthly "What's New" posts and release notes and fold anything not already captured into its category tagged `new: true` — never a separate "new features" silo. Diff the `fetched` dates to see what moved. Delegate web fetching to Haiku sub-agents (user instruction). For JS-heavy marketing/adoption pages, prefix the URL with the `r.jina.ai/https://<url>` reader (the jina CLI isn't installed). Haiku agents sometimes stall asking for env context instead of executing — re-task them forcefully.

## Verify
Before claiming graph integrity or counts, run `python3 scripts/verify_graph.py` (expect 0 broken / 0 orphans) and `python3 scripts/stats.py` (feature/surface/recipe counts). Both derive their root from the script location, so a repo rename won't break them. `verify_graph.py` walks the nested tree, resolves markdown link targets by path, and skips non-vault dirs plus root `CLAUDE.md`/`AGENTS.md` and inline-code examples, so only real vault notes count.

## Enrich
To add more recipes or per-app example prompts, the original fetch data with verbatim prompts lives in `_research/06-prompts-roles.md` (gitignored).
