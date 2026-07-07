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

## 2026-07-07: Genesis build of the Copilot Cookbook KB

**Source:** commit `d455182` (single commit on `main`)

**Context:** Needed a leader-facing Copilot reference to anchor an executive-coaching curriculum.
**Decision:** Two-layer vault — a feature catalog plus scenario-first "plays" — with a licensing spine (Chat Basic vs Copilot add-on vs Admin config) running through every note. Naming is enforced by a canonical, gitignored `_research/MANIFEST.md`. New capabilities fold into their category tagged `new: true` rather than living in a separate silo.
**Alternatives considered:** Developer-oriented framing (rejected — wrong audience). One flat feature list (rejected — loses the "how do I get X done" entry path that the plays layer provides).
