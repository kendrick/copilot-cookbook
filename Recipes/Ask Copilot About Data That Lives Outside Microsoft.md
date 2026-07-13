---
type: recipe
scenario: "The answer you need is in Salesforce or ServiceNow or Jira, and you're tired of leaving Copilot to go look it up."
uses:
  - "[[Copilot Connectors]]"
roles: [champion, exec, sales]
difficulty: "setup needed"
---

**The ask**
Copilot is most useful when it can reach the systems your work actually lives in, not just Microsoft 365. Connect those systems, and Copilot can answer from them in Chat, Researcher, and Excel Agent Mode.

**What you'll use**
- [Copilot Connectors](../Surfaces/Search%20%26%20Work%20IQ/Copilot%20Connectors.md) — federated, MCP-based connectors that bring third-party sources into Copilot

**Steps**
1. As a champion, identify the systems your team keeps leaving Copilot to check.
2. Request those connectors from your admin, connecting is an admin job, not a user one.
3. Once a connector is live, its source shows up in Chat, Researcher, and Excel Agent Mode.
4. Then anyone can ask across it.

**Prompts**
```
Summarize the open support tickets for Contoso from ServiceNow alongside the
latest email thread with their account team.
```

**Watch out for**
This is admin configuration: the connecting is IT's job, so a champion's role is scoping and advocating, not flipping the switch. Each connector needs setup plus access to the underlying system, and answers still respect each user's permissions in that system. Nothing here works until the connector is actually live, so this is a request to make, then a capability to use.

## Related
[Search & Work IQ](../Surfaces/Search%20%26%20Work%20IQ/README.md) · [Find the File You Can Describe but Can't Name](Find%20the%20File%20You%20Can%20Describe%20but%20Can't%20Name.md) · [Scan the Market With Chat](Scan%20the%20Market%20With%20Chat.md)

[^1]: Microsoft 365 Copilot release notes — https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes (fetched 2026-07-07)
[^2]: What's New in Microsoft 365 Copilot — June 2026 — https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%e2%80%99s-new-in-microsoft-365-copilot--june-2026/4529572 (fetched 2026-07-07)
