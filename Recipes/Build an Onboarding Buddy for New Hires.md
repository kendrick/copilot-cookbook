---
type: recipe
scenario: "Every new hire asks the same twenty questions in their first week, and they're all answered somewhere on a team site nobody reads."
uses:
  - "[[Copilot in SharePoint]]"
  - "[[SharePoint Agents]]"
roles: [hr, champion, managers]
difficulty: "setup needed"
---

**The ask**
The onboarding answers exist; they're just buried in a SharePoint site new hires can't navigate yet. Build the content, then put an agent on it so people can ask instead of hunt.

**What you'll use**
- [Copilot in SharePoint](../Surfaces/SharePoint/Copilot%20in%20SharePoint.md) — drafts or refreshes the onboarding site and pages from a description
- [SharePoint Agents](../Surfaces/SharePoint/SharePoint%20Agents.md) — every site has a ready-made agent scoped to its content; build a custom one for a curated experience

**Steps**
1. Use Copilot in SharePoint to build or update the onboarding site: first-week checklist, tools, who to ask, policies.
2. The site's ready-made agent is already available for new hires to ask.
3. For a tighter experience, create a custom agent scoped to the onboarding library.
4. Point new hires at the agent on day one.

**Prompts**
```
Create a new-hire onboarding page with a first-week checklist, key contacts,
and links to the tools a new engineer needs.
```
```
What do I need to set up on my first day, and who approves my equipment order?
```

**Watch out for**
Copilot in SharePoint is in preview, with usage limits, and isn't available in Government or air-gapped clouds. SharePoint agents are GA but need the Copilot license or an org-enabled pay-as-you-go plan. An agent answers only from what a given user can already access, and only as well as the site is written, a thin page yields a confidently thin answer. For a general team assistant across mixed sources, build one in Agent Builder instead.

## Related
[SharePoint](../Surfaces/SharePoint/README.md) · [Stand Up a No-Code Team Agent](Stand%20Up%20a%20No-Code%20Team%20Agent.md) · [Schedule a Recurring Status Digest](Schedule%20a%20Recurring%20Status%20Digest.md)

[^1]: Get started with Copilot in SharePoint — https://learn.microsoft.com/en-us/sharepoint/copilot-in-sharepoint-get-started (fetched 2026-07-13)
[^2]: Get started with agents in SharePoint — https://support.microsoft.com/en-us/sharepoint/copilot-in-sharepoint/get-started-with-agents-in-sharepoint (fetched 2026-07-13)
