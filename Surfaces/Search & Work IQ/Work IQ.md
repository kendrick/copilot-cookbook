---
category: Search & Work IQ
tier: major
status: GA
license: "Admin config"
added: 2026-06
new: true
source: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/
fetched: 2026-07-07
tags: [copilot, work-iq, grounding]
---

**What it is**
A workplace intelligence layer that provides semantic, permission-aware context across Microsoft 365 and external systems, exposed through REST, MCP, and A2A APIs. It's the grounding engine behind Copilot, agents, and custom workflows, including Agent Mode in apps like PowerPoint.[^1]

**Why it matters**
Every Copilot answer and every agent action is only as good as the context grounding it. Work IQ standardizes that layer, respecting the permissions a user already has, so developers and admins aren't rebuilding permission-aware retrieval for each new agent or integration.

**Who it's for**
Developers and admins building or configuring agents and custom workflows. End users encounter it indirectly, as the grounding behind Agent Mode.

**How to access**
REST, MCP, or A2A APIs; also underpins in-app Agent Mode grounding.

**Requires**
Admin configuration; developer access for direct API use.

## Related
[Search & Work IQ](README.md) · [Copilot Search](Copilot%20Search.md) · [Copilot Connectors](Copilot%20Connectors.md) · [Agents & Agent Builder](../Agents%20%26%20Agent%20Builder/README.md)

---
[^1]: Work IQ APIs — https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/ (fetched 2026-07-07)
[^2]: Announcing the new Work IQ APIs — https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/ (fetched 2026-07-07)
