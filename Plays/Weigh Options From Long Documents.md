---
type: play
scenario: "You need to compare several long documents, like vendor contracts or filings, against each other and don't have time to read all of them closely."
uses:
  - "[[Open Files and PDFs in Chat]]"
  - "[[Work-Grounded Copilot Chat]]"
  - "[[Copilot Pages]]"
roles: [finance, sales, exec]
difficulty: "quick win"
---

**The ask**
You're deciding between vendors, filings, or proposals, and the honest way to do it means reading a stack of long PDFs side by side. Copilot Chat can hold all of them at once and give you a structured comparison instead of a pile of tabs.

**What you'll use**
- [[Open Files and PDFs in Chat]] — bring multiple documents into the same chat
- [[Work-Grounded Copilot Chat]] — reasons across them together, not one at a time
- [[Copilot Pages]] — saves the comparison somewhere your team can reference later

**Steps**
1. Open the documents directly in Copilot Chat.
2. Ask Chat to compare them against your criteria and produce a pros-and-cons table.
3. Save the result to a Copilot Page.
4. Share the Page link and keep iterating as new documents come in.

**Prompts**
```
Analyze these 10-K reports and produce an analysis of the pros and cons of
investing in each company. Include a summary table.
```
```
Compare these three vendor contracts on price, termination terms, and SLAs.
Flag anything unusual or risky in each.
```

**Watch out for**
Open Files and PDFs in Chat is new as of 2026-07, so check that it's live in your tenant before you build a workflow around it. Getting real comparisons out of your own contracts and files, rather than generic web answers, needs work-grounded chat, which requires the Copilot add-on; Basic tier chat is web-grounded only and can't see documents you haven't explicitly attached.

## Related
[[Copilot Chat]] · [[Pages & Notebooks]] · [[Copilot Pages]] · [[Prep for a Customer Call]]

[^1]: Microsoft 365 Copilot prompt gallery — https://adoption.microsoft.com/en-us/copilot/prompt-gallery/ (fetched 2026-07-07)
