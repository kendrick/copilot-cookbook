---
type: recipe
scenario: "You know the deck exists, you remember it had the Q3 pricing table, but you have no idea what it's called or who sent it."
uses:
  - "[[Copilot Search]]"
  - "[[Work IQ]]"
roles: [exec, ic, sales]
difficulty: "quick win"
---

**The ask**
Keyword search fails when you don't have the keyword, only a memory of what the thing was about. Describe it instead, and let Copilot match on meaning across everything you're entitled to see.

**What you'll use**
- [Copilot Search](../Surfaces/Search%20%26%20Work%20IQ/Copilot%20Search.md) — semantic search across Microsoft 365 and connected systems, matching on meaning rather than exact words
- [Work IQ](../Surfaces/Search%20%26%20Work%20IQ/Work%20IQ.md) — the permission-aware context layer underneath, which is why a vague description resolves to the right file you already have access to

**Steps**
1. Describe what you remember: the topic, a rough timeframe, who was involved.
2. Open the closest result.
3. Refine the description if the first pass is near but not it.

**Prompts**
```
Find the deck with the Q3 pricing table that someone shared around the
leadership offsite in June.
```
```
Where's the latest version of the vendor contract for Contoso?
```

**Watch out for**
Copilot Search needs the add-on, and third-party systems only show up if an admin configured the connectors. It surfaces only what you already have permission to see, Work IQ enforces that, so it won't turn up something you weren't entitled to. That's the feature, not a limitation.

## Related
[Search & Work IQ](../Surfaces/Search%20%26%20Work%20IQ/README.md) · [Answer an RFP From Your Past Proposals](Answer%20an%20RFP%20From%20Your%20Past%20Proposals.md) · [Ask Copilot About Data That Lives Outside Microsoft](Ask%20Copilot%20About%20Data%20That%20Lives%20Outside%20Microsoft.md)

[^1]: Microsoft 365 Copilot Search — https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-search (fetched 2026-07-07)
[^2]: Work IQ APIs — https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/ (fetched 2026-07-07)
