---
type: recipe
scenario: "Every meeting, someone half-listens so they can take notes, and the notes still come out thin."
uses:
  - "[[Facilitator Agent]]"
roles: [pm, managers, exec]
difficulty: "setup needed"
---

**The ask**
Note-taking and participating pull in opposite directions, and both lose. Let the Facilitator agent keep the running notes, track the agenda, and capture decisions and action items, so everyone can actually be in the conversation.

**What you'll use**
- [Facilitator Agent](../Surfaces/Teams/Facilitator%20Agent.md) — takes real-time collaborative notes in a scheduled Teams meeting, tracks the agenda, and captures decisions and action items

**Steps**
1. When scheduling the meeting, turn Facilitator on in the meeting options.
2. Set an agenda so it can keep time against it.
3. Run the meeting and let it maintain the shared notes.
4. Afterward, review the decisions and action items, and push the action items to Planner.

**Prompts**
```
Summarize the decisions and the open action items Facilitator captured, with
an owner for each where one was named.
```

**Watch out for**
Facilitator is in preview and needs the Microsoft 365 Copilot license. It works in scheduled meetings only, not channel meetings, instant meetings, or calls, and it can't read sensitivity-labeled content. It captures what's said; someone still has to confirm the action items are right and complete before anyone acts on them.

## Related
[Teams](../Surfaces/Teams/README.md) · [Turn a Meeting Into an Assigned Plan](Turn%20a%20Meeting%20Into%20an%20Assigned%20Plan.md) · [Get the Gist of a Meeting You Missed](Get%20the%20Gist%20of%20a%20Meeting%20You%20Missed.md)

[^1]: Facilitator in Microsoft Teams meetings — https://support.microsoft.com/en-us/teams/copilot/facilitator-in-microsoft-teams-meetings (fetched 2026-07-13)
