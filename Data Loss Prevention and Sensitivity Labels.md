---
category: Admin & Governance
tier: major
status: GA
license: "Admin config"
added:
new: false
source: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-control-system/security-governance
fetched: 2026-07-07
tags: [copilot, governance, data-protection]
---

**What it is**
Purview Data Loss Prevention policies apply to Copilot the same way they apply everywhere else in M365. Sensitivity labels are honored: content labeled Confidential stays out of responses it shouldn't touch. SharePoint search that feeds Copilot respects restricted-search settings, so Copilot can't surface content a search restriction was meant to hide.

**Why it matters**
The worry underneath "will Copilot leak something" is usually really "will Copilot ignore the labels and restrictions we already trust." It doesn't. It inherits them.

**Who it's for**
Security and compliance teams, and anyone answering "what happens if a labeled document is grounding material."

**How to access**
Purview compliance portal for DLP policy configuration; sensitivity labels are set at the document level as usual.

**Requires**
Admin configuration via Purview; requires existing DLP/sensitivity label setup to have something to enforce.

## Related
[[Admin & Governance]] · [[Enterprise Data Protection]] · [[Copilot Control System]] · [[Minor Updates — Admin & Governance]]

[^1]: Copilot Control System — Security and governance — https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-control-system/security-governance (fetched 2026-07-07)
