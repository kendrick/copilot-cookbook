# Data Contracts

The "data" here is note structure — frontmatter plus a fixed body shape. Markdown doesn't enforce it, so a new note must match these templates exactly or it drifts from the rest of the vault. The canonical spec originally lived in `PROMPT_INITIAL.md`, which is untracked scaffolding and may be deleted — so the contract is captured here to survive that.

## Feature note
```
---
category: <surface>              # e.g. Word, Copilot Chat, Agents & Agent Builder
tier: major | minor              # note importance, NOT a license tier
status: GA | Preview | Rolling out
license: Copilot add-on | Chat (Basic) | Admin config
added: <YYYY-MM if known, else blank>
new: true | false                # true if surfaced in a Pass-2 / last-~90-days sweep
source: <exact URL>
fetched: <date>
tags: [copilot, <surface>, <theme>]
---
# <Feature name>              # = filename = wikilink target, exactly

**What it is** — one or two plain-language sentences.
**Why it matters** — business/personal value in exec terms.
**Who it's for** — the roles or scenarios that benefit most.
**How to access** — app + entry point (menu, prompt, admin toggle).
**Requires** — license tier, admin enablement, or preview enrollment.

## Try it                     # omit entirely if there's no meaningful "how"
1. <concrete step>
Example prompt:
> <copy-pasteable prompt>

## Related
[[Category]] · [[Related feature]]
```

Genuinely trivial tweaks roll into a per-category `Minor Updates — <Surface>.md` note (`tier: minor`) rather than getting their own note.

## Play note (in `Plays/`)
```
---
type: play
scenario: <the business problem, in exec language>
uses: [[Feature]], [[Feature]]     # capabilities it chains
roles: [exec, sales, finance, ops]
difficulty: quick win | setup needed
---
# <Task-phrased title>

**The ask** — the problem as an exec would state it.
**What you'll use** — [[Feature]] (+ [[Feature]] if chained across apps).
**Steps** — numbered, concrete, spanning apps where needed.
**Prompts** — copy-pasteable, in code blocks.
**Watch out for** — license/preview gotchas, quality caveats.

## Related
[[Feature]] · [[Play]]
```

## `_sources.md` entries
Each source URL carries a `fetched` date. Refreshes diff against these dates to find what changed since the last pass.
