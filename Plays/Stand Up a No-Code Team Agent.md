---
type: play
scenario: "Your team keeps asking the same handful of questions about the same documents, and it's not worth a developer ticket to fix."
uses:
  - "[[Agent Builder]]"
  - "[[Agent Store]]"
roles: [it, hr, ops]
difficulty: "setup needed"
---

**The ask**
HR gets the same PTO policy question every week. A project team keeps re-asking where things stand in the same SharePoint documentation. Neither needs custom development; both need a five-minute agent scoped to the right knowledge source.

**What you'll use**
- [Agent Builder](../Surfaces/Agents%20%26%20Agent%20Builder/Agent%20Builder.md) — describes the agent in plain language and points it at knowledge sources
- [Agent Store](../Surfaces/Agents%20%26%20Agent%20Builder/Agent%20Store.md) — publishes it so your team can find it

**Steps**
1. In Copilot Chat, go to Agents and create an agent.
2. Describe its purpose and point it at knowledge sources: SharePoint, Teams, OneDrive, or uploaded files (OneDrive caps at 50 files).
3. Test it with the real questions your team actually asks, not hypothetical ones.
4. Publish it to the Agent Store, or share it directly with your team.

**Prompts**
```
Create an agent that answers employee questions about our PTO and
remote-work policies, grounded in the HR Policies SharePoint site. If it
doesn't know, it should say so and point to HR.
```
```
Create an FAQ agent for Project Falcon that answers questions from the
project's SharePoint documentation.
```

**Watch out for**
Agent Builder needs the Copilot add-on, Copilot Chat pay-as-you-go, or a Copilot Studio license; Basic tier alone can't create one. If the agent needs to take action instead of just answering questions, that's past what Agent Builder does, and you'll need Copilot Studio instead.

## Related
[Agents & Agent Builder](../Surfaces/Agents%20%26%20Agent%20Builder/README.md) · [Copilot Studio](../Surfaces/Agents%20%26%20Agent%20Builder/Copilot%20Studio.md) · [Schedule a Recurring Status Digest](Schedule%20a%20Recurring%20Status%20Digest.md)

[^1]: Agent Builder — Build agents — https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents (fetched 2026-07-07)
