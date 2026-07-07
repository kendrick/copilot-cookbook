---
type: play
scenario: "You have a customer call in twenty minutes and need the account history, not a scramble through old emails."
uses:
  - "[[Work-Grounded Copilot Chat]]"
  - "[[Copilot in Teams Calls]]"
  - "[[Copilot Pages]]"
  - "[[Meeting Recap and Intelligent Recap]]"
roles: [sales, exec]
difficulty: "quick win"
---

**The ask**
Whether it's a delivery issue you need to smooth over or a renewal conversation, you want to walk in knowing what's open with the account and what the contact has already told you, not find out mid-call that you missed something.

**What you'll use**
- [[Work-Grounded Copilot Chat]] — summarizes account history from emails, chats, and files
- [[Copilot Pages]] — turns that summary into a prep sheet you can glance at during the call
- [[Copilot in Teams Calls]] — live follow-up question suggestions once the call is underway
- [[Meeting Recap and Intelligent Recap]] — captures next steps afterward

**Steps**
1. Ask Copilot Chat to summarize everything about the customer from the last several months.
2. Save the summary to a Copilot Page as your prep sheet.
3. During the call, lean on Copilot in Teams Calls for follow-up question suggestions in the moment.
4. After the call, capture next steps with Meeting Recap and Intelligent Recap.

**Prompts**
```
Summarize all emails, chats, and files about Acme Corp from the last 90 days.
Highlight open commitments, past issues, and the primary contact's
priorities.
```
```
Suggest three follow-up questions I should ask on this call given what's
open with this account.
```

**Watch out for**
Copilot in Teams Calls needs the Copilot add-on. So does work-grounded chat, since it's the only way Copilot can see the customer's actual history in your mailbox and files rather than answering from general knowledge.

## Related
[[Copilot Chat]] · [[Teams]] · [[Copilot Pages]] · [[Build a Copilot Notebook for a Recurring Project Status]]

[^1]: Microsoft 365 Copilot prompt gallery — https://adoption.microsoft.com/en-us/copilot/prompt-gallery/ (fetched 2026-07-07)
[^2]: Microsoft 365 Copilot — top 10 things to try first — https://www.microsoft.com/en-us/microsoft-365-copilot/copilot-top-10-things-to-try-first (fetched 2026-07-07)
