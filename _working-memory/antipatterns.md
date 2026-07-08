# Antipatterns

<!-- Negative knowledge. Things the team tried that didn't work, captured so   -->
<!-- agents and humans don't re-litigate closed loops. Append-only, like        -->
<!-- decisionLog.md.                                                            -->
<!--                                                                            -->
<!-- Format: -->
<!-- ## YYYY-MM-DD — [Short title in imperative voice — what to avoid]         -->
<!-- **Tried:** What was attempted                                              -->
<!-- **What broke:** Observed failure mode                                      -->
<!-- **Why we backed out:** Root cause if known; otherwise the observed pain    -->
<!-- **Don't suggest:** Specific things agents should not re-propose            -->
<!--                                                                            -->
<!-- The last line is the agent-targeted lever. Be specific. "Don't suggest    -->
<!-- moving X to Y" beats "don't suggest big refactors."                       -->

## 2026-07-07 — Don't assume links auto-follow a moved or renamed note

**Tried:** N/A — flagging after the wikilink-to-markdown migration.
**What broke:** Obsidian auto-updates `[[wikilinks]]` on rename, but the vault now uses path-based relative markdown links, which it does not auto-fix.
**Why we backed out:** We traded auto-rename for Loop portability on purpose.
**Don't suggest:** Moving or renaming a note by hand and assuming its links still resolve. Recompute the relative links (the reorg used a script for this) and re-run `scripts/verify_graph.py` after any move.

## 2026-07-07 — Don't space-wrap em dashes

**Tried:** Writing prose with spaced em dashes (`word — word`).
**What broke:** Doesn't match how the user writes; got corrected.
**Why we backed out:** User style — em dashes chain directly with text on both sides.
**Don't suggest:** Spaced em dashes in any prose. Chain directly (`like—this`) or use other punctuation. Only exception is the `- term — description` list bullet.

## 2026-07-07 — Don't hard-wrap prose or commit messages

**Tried:** Wrapping paragraphs and commit-message bodies at a fixed column.
**What broke:** Renders badly in GitHub's UI and IDEs; got corrected.
**Why we backed out:** User wants the terminal or git's pager to wrap at display time.
**Don't suggest:** Manual hard returns inside a paragraph anywhere, commit messages included. One unwrapped line per paragraph.

## 2026-07-07 — Don't invent UI steps for a Rolling out feature

**Tried:** Considering concrete click-path steps for `Copilot in Loop`, which is mid-transition to Copilot Pages.
**What broke:** The steps wouldn't be verifiable against a live source and could be wrong for a feature still shipping.
**Why we backed out:** Every claim must trace to a fetched source; a `Rolling out` feature has no stable UI to document.
**Don't suggest:** Writing step-by-step UI instructions for any `Rolling out` or `Preview` note beyond what the source actually shows.

## 2026-07-07 — Don't "fix" the intentionally-empty Minor Updates — Teams note

**Tried:** N/A — flagging for future agents.
**What broke:** `Minor Updates — Teams.md` has no bullets, which reads like an omission bug.
**Why we backed out:** Nothing genuinely Teams-minor surfaced in the research sweep. The note is an honest placeholder ("revisit once a more granular what's-new sweep is available"), not a gap to fill.
**Don't suggest:** Inventing Teams minor-update content to populate that note. Leave it empty until a real what's-new sweep surfaces something.

## 2026-07-07 — Don't assert a Claude version more specific than "Claude"

**Tried:** Naming a specific Claude version as selectable in Copilot Chat.
**What broke:** The release notes say only "Claude"; a more specific version would over-claim.
**Why we backed out:** Fidelity to source wording — GPT-5.5 is named with its Instant/Thinking variants, but the Claude entry is not versioned.
**Don't suggest:** Any Claude version string beyond "Claude" in the model-selection notes.
