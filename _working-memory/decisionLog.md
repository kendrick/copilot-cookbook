# Decision Log

Append-only; newest entry on top. Don't edit past entries; supersede them with a new one.

Each entry follows this shape:

```markdown
## 2026-04-19: Short title

**Source:** the commit, PR, or discussion it came from (optional for hand-written entries)

**Context:** Why this came up.
**Decision:** What was decided.
**Alternatives considered:** What was rejected, and why.
```

## 2026-07-07: Add staleness.py so refreshes start from a triage worklist

**Source:** commit 822fd8b

**Context:** Copilot ships ~monthly and the catalog drifts, but the Refresh workflow re-fetched everything blind — no fast read on what had actually gone stale.
**Decision:** Add read-only `scripts/staleness.py` that reports three things before a refresh: sources past a 30-day baseline, `new: true` notes older than 90 days to flip to `false`, and Preview/Rolling out notes to re-check for GA. Wire it in as step one of conventions.md Refresh and surface it in the README, so a refresh becomes a diff against a worklist rather than a rebuild.
**Alternatives considered:** Keep eyeballing `fetched` dates by hand (rejected — misses the new-flag and pre-GA dimensions and doesn't scale as the catalog grows).

## 2026-07-07: Re-author full history to the personal identity, add origin, push

**Context:** The vault was built under a work email (`k.arnett@slalom.com`) but it's a personal knowledge base that belongs on a personal GitHub, not work product.
**Decision:** Rewrite every commit's author and committer to `Kendrick Arnett <kmarnett@gmail.com>`, add the `origin` remote (`github_personal:kendrick/copilot-cookbook`), and push `main`. Every commit hash changed as a result; the `Source:` lines in earlier decisionLog entries were repointed to the new hashes in the same pass, so they still resolve.
**Alternatives considered:** Re-author only future commits (rejected — leaves the work email stamped across the whole existing history on a personal repo). Start a fresh repo (rejected — discards the build narrative the history preserves).

## 2026-07-07: Restructure into Surfaces/ folders and switch to markdown links

**Source:** commits 11a39ab (reorganize), 1fb3ade (convert links), bc42ae5 (rename)

**Context:** The root held 80+ flat notes — unnavigable, and a poor fit for exporting to Microsoft Loop, whose page hierarchy wants a tree.
**Decision:** Move every feature note under `Surfaces/<Surface>/` with the category note as that folder's `README.md`; convert body `[[wikilinks]]` to relative markdown links so links resolve by path (survives Loop export, and lets each folder reuse the `README.md` name); rename `Plays/` to `Recipes/` to fit the cookbook framing. Sequenced as pure `git mv` commits so history follows the files.
**Alternatives considered:** Stay flat and lean on Obsidian MOCs/tags (rejected — doesn't fix the file tree and doesn't pre-build the Loop page tree). Keep wikilinks (rejected — Loop ignores them, and README name collisions block the folder-index pattern).

## 2026-07-07: Genesis build of the Copilot Cookbook KB

**Source:** commit `6235496` (single commit on `main`)

**Context:** Needed a leader-facing Copilot reference to anchor an executive-coaching curriculum.
**Decision:** Two-layer vault — a feature catalog plus scenario-first "plays" — with a licensing spine (Chat Basic vs Copilot add-on vs Admin config) running through every note. Naming is enforced by a canonical, gitignored `_research/MANIFEST.md`. New capabilities fold into their category tagged `new: true` rather than living in a separate silo.
**Alternatives considered:** Developer-oriented framing (rejected — wrong audience). One flat feature list (rejected — loses the "how do I get X done" entry path that the plays layer provides).
