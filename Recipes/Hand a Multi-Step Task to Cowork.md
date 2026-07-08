---
type: recipe
scenario: "A task has several steps that each depend on the last (pull data, build a comparison, draft an email) and you'd rather describe the whole thing once than do it step by step yourself."
uses:
  - "[[Copilot Cowork]]"
  - "[[Scheduled Prompts and Long-Running Tasks]]"
roles: [ops, it, exec]
difficulty: "setup needed"
---

**The ask**
Some tasks aren't a single prompt. They're a chain: gather this, compare it to that, then draft something based on the result. Cowork works through multi-step tasks like that, checking in with you at each step instead of running unattended and hoping it got things right.

**What you'll use**
- [Copilot Cowork](../Surfaces/Cowork/Copilot%20Cowork.md) — the agentic executor that works through the steps with approval at each one
- [Scheduled Prompts and Long-Running Tasks](../Surfaces/Cowork/Scheduled%20Prompts%20and%20Long-Running%20Tasks.md) — for turning a one-off Cowork task into a recurring one

**Steps**
1. Confirm with IT or your admin that Cowork is enabled for your tenant. It's off by default even with the right license.
2. Describe the task end to end, including what "done" looks like.
3. Approve each step as Cowork proposes it; it doesn't run unattended.
4. For tasks you'll repeat, pair Cowork with Scheduled Prompts and Long-Running Tasks so future runs kick off on their own.

**Prompts**
```
Pull last quarter's regional sales figures, build a comparison against the
prior quarter, and draft a summary email to the regional leads flagging any
region down more than 5%.
```

**Watch out for**
Cowork requires a Copilot user subscription license plus usage-based billing through Copilot Credits, which is metered spend on top of the license, and it's admin-disabled by default. Confirm both the license and the enablement before you promise this to a team.

## Related
[Cowork](../Surfaces/Cowork/README.md) · [Copilot Chat](../Surfaces/Copilot%20Chat/README.md) · [Schedule a Recurring Status Digest](Schedule%20a%20Recurring%20Status%20Digest.md)

[^1]: Microsoft 365 Copilot — Cowork — https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/ (fetched 2026-07-07)
[^2]: Copilot Cowork is now generally available — https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/ (fetched 2026-07-07)
