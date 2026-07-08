# Copilot Cookbook

A wikilinked knowledge base of Microsoft 365 Copilot. It answers two different questions:

- **"What can Copilot do?"** → the feature catalog, organized by where each capability lives.
- **"How do I get *X* done?"** → the recipes, organized by the problem a user states out loud.

Every claim traces to a live Microsoft page, fetched 2026-07-07. It's built for Obsidian: open the vault and follow the `[[wikilinks]]`, or start from a map:

- **[Copilot Features MOC](Surfaces/README.md)** — every capability, grouped by surface (Word, Excel, Chat, Agents, and the rest). Newest features are folded into their category and tagged `new: true`, not siloed.
- **[Recipes](Recipes/README.md)** — scenario recipes grouped by business need: analyze data, catch up on what I missed, draft from messy inputs, prep for a meeting, build a deck, automate a recurring task, research a topic.

## How it's organized

- **Category notes** (e.g. `Word.md`, `Copilot Chat.md`) — one per surface, each linking its feature notes.
- **Feature notes** — one capability each, with frontmatter for tier, status (GA / Preview / Rolling out), license, and whether it's new. Named for the capability, so the filename is the wikilink.
- **Recipes** (in `Recipes/`) — terse, scenario-first notes that chain features, with copy-pasteable prompts and cross-app steps.
- **[_sources](_sources.md)** — every source URL with its last-updated and fetch date, so you can diff on a re-run.

## Reading the frontmatter

Two things people always ask, *can we use it today* and *what does it cost*, live in the frontmatter of each feature note:

- `status` — `GA` (use it now), `Preview` / `Rolling out` (not everywhere yet).
- `license` — `Chat (Basic)` (free with Microsoft 365), `Copilot add-on` (the paid per-user license), or `Admin config` (an IT control, not an end-user feature).

The distinction between Copilot Chat (Basic) and the Copilot add-on runs through the whole catalog. [Copilot Licensing Tiers](Surfaces/Admin%20%26%20Governance/Copilot%20Licensing%20Tiers.md) lays it out.

## Refreshing it

Copilot ships monthly. To update: re-fetch the pages in [_sources](_sources.md), diff against the `fetched` dates, and fold new capabilities into their category with `new: true`. The two passes that built this — establish the full surface, then layer in the newest month — are the same two you'd repeat.
