---
type: recipe
scenario: "You've got back-to-back one-on-ones and can't remember what each person committed to last time, let alone what they've shipped since."
uses:
  - "[[Work-Grounded Copilot Chat]]"
  - "[[Meeting Recap and Intelligent Recap]]"
roles: [managers, exec]
difficulty: "quick win"
---

**The ask**
A one-on-one goes better when you walk in knowing what the person has been working on and what you two last agreed. Rebuild that in two minutes instead of skimming old threads between meetings.

**What you'll use**
- [Work-Grounded Copilot Chat](../Surfaces/Copilot%20Chat/Work-Grounded%20Copilot%20Chat.md) — pulls the person's recent work from your shared emails, chats, files, and meetings
- [Meeting Recap and Intelligent Recap](../Surfaces/Teams/Meeting%20Recap%20and%20Intelligent%20Recap.md) — recovers what was decided and assigned last time

**Steps**
1. Ask Chat for a read on the person's recent work and anything they're waiting on from you.
2. Pull the recap of your last one-on-one for the decisions and action items.
3. Note the two or three things to actually follow up on.

**Prompts**
```
Summarize what Priya has been working on in the last two weeks from our
emails, chats, and shared files, and list anything she's waiting on from me.
```
```
What did we decide and assign in my last one-on-one with Priya?
```

**Watch out for**
Work grounding needs the add-on, that's what lets Chat see the person's actual work instead of answering generically. Keep this to the shared work you'd already discuss; it's prep for a conversation, not an activity audit, and it reads very differently if you treat it as one.

## Related
[Copilot Chat](../Surfaces/Copilot%20Chat/README.md) · [Prep for a Customer Call](Prep%20for%20a%20Customer%20Call.md) · [Get the Gist of a Meeting You Missed](Get%20the%20Gist%20of%20a%20Meeting%20You%20Missed.md)

[^1]: Microsoft 365 Copilot overview — https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-overview (fetched 2026-07-07)
[^2]: Catch up on meetings with Microsoft 365 Copilot in Teams — https://support.microsoft.com/en-us/teams/copilot/catch-up-on-meetings-with-microsoft-365-copilot-in-teams (fetched 2026-07-07)
