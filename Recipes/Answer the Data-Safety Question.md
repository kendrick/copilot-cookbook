---
type: recipe
scenario: "Before anyone will greenlight a Copilot rollout, security and legal want to know exactly what happens to the data."
uses:
  - "[[Enterprise Data Protection]]"
  - "[[Data Loss Prevention and Sensitivity Labels]]"
  - "[[Copilot Control System]]"
roles: [champion, it, exec]
difficulty: "setup needed"
---

**The ask**
The rollout stalls on three questions: does it train on our prompts, does it respect the labels we already trust, and who decides which agents our people can run. Have straight, sourced answers ready: no, yes, and you do.

**What you'll use**
- [Enterprise Data Protection](../Surfaces/Admin%20%26%20Governance/Enterprise%20Data%20Protection.md) — the standing guarantee that prompts and responses don't train the foundation models
- [Data Loss Prevention and Sensitivity Labels](../Surfaces/Admin%20%26%20Governance/Data%20Loss%20Prevention%20and%20Sensitivity%20Labels.md) — how existing Purview policies and labels carry into Copilot
- [Copilot Control System](../Surfaces/Admin%20%26%20Governance/Copilot%20Control%20System.md) — the admin hub for enabling by group and governing which agents run

**Steps**
1. Lead with the data-training answer, it's the first question in the room.
2. Show that existing DLP policies and sensitivity labels are honored; Copilot inherits them rather than working around them.
3. Walk through the Control System: who decides which agents users can run, and how to turn one off.
4. Hand the room the Microsoft source pages, not just your reassurance.

**Watch out for**
These are standing platform guarantees and admin controls, not a switch you flip on rollout day. The protections inherit what you've already set up, so "Copilot respects your labels" only means something if you actually have labels and DLP configured. Keep this conversation grounded in the source pages; it's the one where your word alone won't carry it.

## Related
[Admin & Governance](../Surfaces/Admin%20%26%20Governance/README.md) · [Decide Who Gets a Copilot License](Decide%20Who%20Gets%20a%20Copilot%20License.md) · [Prove Copilot Is Earning Its Seat](Prove%20Copilot%20Is%20Earning%20Its%20Seat.md)

[^1]: Microsoft 365 Copilot — Privacy — https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-privacy (fetched 2026-07-07)
[^2]: Copilot Control System — Security and governance — https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-control-system/security-governance (fetched 2026-07-07)
