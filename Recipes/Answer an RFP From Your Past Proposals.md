---
type: recipe
scenario: "An RFP lands with forty questions you've basically answered before, scattered across proposals you can't quite find."
uses:
  - "[[Copilot Search]]"
  - "[[Ground a Draft on Your Files]]"
roles: [sales]
difficulty: "setup needed"
---

**The ask**
Most RFP questions aren't new; your team has answered a version of them in a past proposal, if you could find it. Search your prior responses, then draft each answer in Word grounded on the ones you find.

**What you'll use**
- [Copilot Search](../Surfaces/Search%20%26%20Work%20IQ/Copilot%20Search.md) — semantic search across Microsoft 365 and connected systems to surface prior proposals by meaning, not just keyword
- [Ground a Draft on Your Files](../Surfaces/Word/Ground%20a%20Draft%20on%20Your%20Files.md) — references up to 20 files by typing "/" so the draft is built on real prior answers

**Steps**
1. Search for the strongest past responses on each theme the RFP hits.
2. In Word, type "/" to reference the best source proposals for a given question.
3. Draft the answer against those sources, in your standard proposal voice.
4. Fact-check every reused claim against what you actually offer today.

**Prompts**
```
Find our past RFP and proposal responses about data security, SOC 2, and
uptime commitments.
```
```
Draft an answer to this RFP question about implementation timelines using
/Acme-proposal-2025.docx, matching our standard proposal tone.
```

**Watch out for**
Copilot Search needs the add-on, and third-party sources only show up if an admin has configured the connectors. Ground a Draft caps at 20 references. The real risk here is confidently reusing a claim that's since changed, a capability you no longer offer, an old SLA, so the fact-check pass isn't optional.

## Related
[Word](../Surfaces/Word/README.md) · [Search & Work IQ](../Surfaces/Search%20%26%20Work%20IQ/README.md) · [Ask Copilot About Data That Lives Outside Microsoft](Ask%20Copilot%20About%20Data%20That%20Lives%20Outside%20Microsoft.md)

[^1]: Microsoft 365 Copilot Search — https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-search (fetched 2026-07-07)
[^2]: Draft and add content with Copilot in Word — https://support.microsoft.com/en-us/Word/copilot/draft-and-add-content-with-copilot-in-word (fetched 2026-07-07)
