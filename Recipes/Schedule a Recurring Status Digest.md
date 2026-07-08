---
type: recipe
scenario: "You run the same 'what happened this week on Project X' prompt every Monday morning and want Copilot to just do it without you."
uses:
  - "[[Scheduled Prompts and Long-Running Tasks]]"
  - "[[Work-Grounded Copilot Chat]]"
  - "[[Copilot Pages]]"
roles: [exec, ops, it]
difficulty: "setup needed"
---

**The ask**
If you're running the same prompt on the same cadence, it doesn't need you. Schedule it once and let the digest show up where your team already looks.

**What you'll use**
- [Scheduled Prompts and Long-Running Tasks](../Surfaces/Cowork/Scheduled%20Prompts%20and%20Long-Running%20Tasks.md) — runs the prompt on a recurring schedule
- [Work-Grounded Copilot Chat](../Surfaces/Copilot%20Chat/Work-Grounded%20Copilot%20Chat.md) — the underlying summarization
- [Copilot Pages](../Surfaces/Pages%20%26%20Notebooks/Copilot%20Pages.md) — where the digest lands each time

**Steps**
1. In Copilot Chat, write the prompt you'd normally run manually each week.
2. Save it as a scheduled prompt with your cadence, such as every Monday at 7am.
3. Point the digest's output at a Copilot Page or Teams channel so it lands somewhere your team actually checks.
4. Adjust the schedule or prompt as the project's rhythm changes.

**Prompts**
```
Every Monday at 7am, summarize all emails and Teams chats from the past week
about Project Falcon, highlighting the primary asks and open items, and
post the result to the Project Falcon status page.
```

**Watch out for**
Scheduled Prompts and Long-Running Tasks is new as of 2026-07; confirm it's GA rather than still rolling out in your tenant before you rely on it for anything time-sensitive. It also requires the Copilot add-on for work-grounded scheduling.

## Related
[Copilot Chat](../Surfaces/Copilot%20Chat/README.md) · [Cowork](../Surfaces/Cowork/README.md) · [Stand Up a No-Code Team Agent](Stand%20Up%20a%20No-Code%20Team%20Agent.md)

[^1]: Microsoft 365 Copilot prompt gallery — https://adoption.microsoft.com/en-us/copilot/prompt-gallery/ (fetched 2026-07-07)
