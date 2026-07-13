---
type: recipe
scenario: "Renewal is coming up and someone's going to ask whether the Copilot spend is actually doing anything."
uses:
  - "[[Copilot Adoption Analytics]]"
roles: [champion, exec]
difficulty: "setup needed"
---

**The ask**
"Is anyone actually using this" decides whether a rollout gets renewed or quietly shelved. Answer it with data, who's using it, whether that's sticking, and what impact and sentiment say, instead of a handful of anecdotes.

**What you'll use**
- [Copilot Adoption Analytics](../Surfaces/Admin%20%26%20Governance/Copilot%20Adoption%20Analytics.md) — the Copilot Dashboard in Viva Insights: Readiness, Adoption, Impact, and Sentiment

**Steps**
1. Pull the Adoption view for active users trending over months, not a single snapshot.
2. Layer in Impact for the productivity signal and Sentiment for how people say it's going.
3. Frame the story around where it's landed and where the next push should go.
4. Bring it to the renewal conversation with two or three concrete wins alongside the numbers.

**Watch out for**
This lives in Viva Insights and is admin-configured. Keep the two questions separate: Adoption answers "who has a seat and uses it," while Impact and Sentiment answer "is it worth it", collapsing them into one number weakens both. Usage on its own isn't value, which is why the concrete wins matter. Deciding who gets a seat in the first place is the companion recipe below.

## Related
[Admin & Governance](../Surfaces/Admin%20%26%20Governance/README.md) · [Decide Who Gets a Copilot License](Decide%20Who%20Gets%20a%20Copilot%20License.md) · [Answer the Data-Safety Question](Answer%20the%20Data-Safety%20Question.md)

[^1]: Copilot Dashboard in Viva Insights — https://learn.microsoft.com/en-us/viva/insights/org-team-insights/copilot-dashboard (fetched 2026-07-13)
[^2]: Copilot Control System — Security and governance — https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-control-system/security-governance (fetched 2026-07-07)
