---
type: play
scenario: "You're back from vacation, leave, or a stretch of back-to-back meetings and need to know what happened without reading every email and chat yourself."
uses:
  - "[[Work-Grounded Copilot Chat]]"
  - "[[Copilot Chat Across Your Inbox]]"
  - "[[Copilot Pages]]"
roles: [exec, ops, it]
difficulty: "quick win"
---

**The ask**
Two weeks away means a flooded inbox, missed Teams threads, and a project that moved without you. Ask Copilot for the version of events, not the raw feed.

**What you'll use**
- [Work-Grounded Copilot Chat](../Surfaces/Copilot%20Chat/Work-Grounded%20Copilot%20Chat.md) — pulls a synthesis across emails, chats, and files
- [Copilot Chat Across Your Inbox](../Surfaces/Outlook/Copilot%20Chat%20Across%20Your%20Inbox.md) — narrows in on what needs a reply in Outlook specifically
- [Copilot Pages](../Surfaces/Pages%20%26%20Notebooks/Copilot%20Pages.md) — keeps the summary somewhere you can reread through the day

**Steps**
1. Ask Copilot Chat what's new on a topic or project, organized by emails, chats, and files.
2. Use Copilot Chat Across Your Inbox to find the messages that actually need a response from you.
3. Save the synthesis to a Copilot Page so you're not re-running the same prompt later.

**Prompts**
```
Tell me what's new about Project X since June 20, organized by emails, chats,
and files.
```
```
Show me all emails from the last 7 days where I'm in the To line, and
summarize what needs a response from me.
```

**Watch out for**
Copilot Chat Across Your Inbox is new as of 2026-07; confirm it's rolled out in your tenant. Anything that reads your actual mailbox and files requires work-grounded chat, which needs the Copilot add-on. Basic tier chat is web-grounded only, so it can't see what you missed.

## Related
[Copilot Chat](../Surfaces/Copilot%20Chat/README.md) · [Outlook](../Surfaces/Outlook/README.md) · [Get the Gist of a Meeting You Missed](Get%20the%20Gist%20of%20a%20Meeting%20You%20Missed.md)

[^1]: Microsoft 365 Copilot — top 10 things to try first — https://www.microsoft.com/en-us/microsoft-365-copilot/copilot-top-10-things-to-try-first (fetched 2026-07-07)
[^2]: Microsoft 365 Copilot prompt gallery — https://adoption.microsoft.com/en-us/copilot/prompt-gallery/ (fetched 2026-07-07)
