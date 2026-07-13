---
type: recipe
scenario: "You ran a survey, the responses are in, and you need the story in them, not just a pile of rows."
uses:
  - "[[Create in the Copilot App]]"
  - "[[Analyst]]"
roles: [hr, it, exec]
difficulty: "quick win"
---

**The ask**
A pulse survey or a feedback form comes back with a few hundred responses, and "read all of it" isn't a plan. Build the survey in Create, then hand the results to Analyst for an analysis that shows its work.

**What you'll use**
- [Create in the Copilot App](../Surfaces/Create/Create%20in%20the%20Copilot%20App.md) — generates the form or survey from a description
- [Analyst](../Surfaces/Researcher%20%26%20Analyst/Analyst.md) — runs visible Python over the results, so you see the code behind each trend

**Steps**
1. In the Copilot app, use Create to generate the survey from a plain description of what you want to learn.
2. Collect responses, then export or upload the results to the Analyst agent.
3. Ask Analyst for the themes, the outliers, and which differences are statistically real.
4. Take the findings, and the code Analyst shows, into whatever you're reporting.

**Prompts**
```
Create a 6-question employee survey on how the new hybrid policy is landing,
with a mix of rating scales and one open comment.
```
```
Analyze this survey data and generate strategic recommendations, flagging any
statistically significant trends.
```

**Watch out for**
Create forms sit on the free Basic tier, but Analyst needs the Copilot add-on and shares a pool of roughly 25 monthly queries with Researcher, so save it for the real analysis. Because Analyst shows its Python, you can also see when a "trend" is really just a handful of responses, worth checking before you present it as a finding.

## Related
[Create](../Surfaces/Create/README.md) · [Researcher & Analyst](../Surfaces/Researcher%20%26%20Analyst/README.md) · [Find the Story in a Messy Spreadsheet](Find%20the%20Story%20in%20a%20Messy%20Spreadsheet.md)

[^1]: Frequently asked questions about Create in the Microsoft 365 Copilot app — https://support.microsoft.com/en-us/microsoft-365-copilot/frequently-asked-questions-about-create-in-the-microsoft-365-copilot-app (fetched 2026-07-13)
[^2]: Empower your workforce with Copilot: Marketing — https://learn.microsoft.com/en-us/training/modules/empower-workforce-copilot-marketing/ (fetched 2026-07-07)
