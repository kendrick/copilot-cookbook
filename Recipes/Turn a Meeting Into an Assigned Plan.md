---
type: recipe
scenario: "The meeting ends with a dozen 'someone should' action items, and by tomorrow no one remembers who or what."
uses:
  - "[[Facilitator Agent]]"
  - "[[Copilot in Planner]]"
roles: [pm, managers]
difficulty: "setup needed"
---

**The ask**
Action items agreed in a meeting die in the gap between the recap and the plan nobody retypes them into. Capture them as they're decided, then land them in Planner as real, owned tasks.

**What you'll use**
- [Facilitator Agent](../Surfaces/Teams/Facilitator%20Agent.md) — captures decisions and action items live, and can sync tasks to Planner
- [Copilot in Planner](../Surfaces/Planner/Copilot%20in%20Planner.md) — where the tasks land, and where you shape them into a plan with buckets and goals

**Steps**
1. Run the meeting with Facilitator on.
2. As action items come up, ask it to create tasks for them.
3. The tasks you explicitly ask for sync to Planner automatically; auto-captured ones need an "Accept to sync."
4. Open the plan in Planner and use Copilot there to organize the tasks into phases and set goals.

**Prompts**
```
Create a task for that: draft the vendor comparison, owner Sam, due Friday.
```
```
Organize these tasks into phases and add a goal for the launch.
```

**Watch out for**
Both pieces are in preview. Facilitator needs the Microsoft 365 Copilot license; Copilot in Planner needs a premium Planner plan or a Copilot license. There's no single button that turns a recap into a plan, the tasks you explicitly ask Facilitator to create sync on their own, but the ones it captured for you have to be accepted first. Check owners and dates before you call it a plan.

## Related
[Planner](../Surfaces/Planner/README.md) · [Put Facilitator in Charge of the Notes](Put%20Facilitator%20in%20Charge%20of%20the%20Notes.md) · [Turn Meeting Notes Into a Project Brief](Turn%20Meeting%20Notes%20Into%20a%20Project%20Brief.md)

[^1]: Facilitator in Microsoft Teams meetings — https://support.microsoft.com/en-us/teams/copilot/facilitator-in-microsoft-teams-meetings (fetched 2026-07-13)
[^2]: Frequently asked questions about Copilot in Planner (preview) — https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-planner-preview-40710220-75f3-4a61-897c-54a1052155c4 (fetched 2026-07-13)
