---
type: recipe
scenario: "A quarter of ideas and meeting notes has piled up across a OneNote section, and none of it is a plan yet."
uses:
  - "[[Summarize Notes in OneNote]]"
  - "[[Draft in OneNote]]"
  - "[[Create Tasks From Notes]]"
roles: [pm, ic]
difficulty: "quick win"
---

**The ask**
Notes accumulate faster than they resolve. You've got a section full of half-thoughts, meeting scraps, and decisions, and it needs to become a plan with owners and tasks, without you re-reading all of it first.

**What you'll use**
- [Summarize Notes in OneNote](../Surfaces/OneNote%20%26%20Loop/Summarize%20Notes%20in%20OneNote.md) — condenses the section into themes and open questions, cited
- [Draft in OneNote](../Surfaces/OneNote%20%26%20Loop/Draft%20in%20OneNote.md) — drafts the plan from that summary, in place
- [Create Tasks From Notes](../Surfaces/OneNote%20%26%20Loop/Create%20Tasks%20From%20Notes.md) — pulls the action items into a trackable task list

**Steps**
1. Ask Copilot to summarize the section into main themes and unresolved questions.
2. From that summary, ask it to draft a plan with phases and owners where the notes name them.
3. Extract the action items into tasks.

**Prompts**
```
Summarize these notes into the main themes, the decisions already made, and
the questions still open.
```
```
Draft a project plan from these notes, with phases and an owner for each item
where the notes name one.
```

**Watch out for**
All three need the add-on, and Draft in OneNote is still rolling out on the Web and Teams versions, so it may not be everywhere yet. Summarize skips notebooks protected by Windows Information Protection. This turns messy notes into a first draft of a plan; the owners and dates it infers still need a human to confirm.

## Related
[OneNote & Loop](../Surfaces/OneNote%20%26%20Loop/README.md) · [Turn Meeting Notes Into a Project Brief](Turn%20Meeting%20Notes%20Into%20a%20Project%20Brief.md) · [Build a Copilot Notebook for a Recurring Project Status](Build%20a%20Copilot%20Notebook%20for%20a%20Recurring%20Project%20Status.md)

[^1]: Copilot in OneNote — https://support.microsoft.com/en-us/copilot-onenote (fetched 2026-07-07)
[^2]: Create a to-do list and tasks in OneNote with Copilot — https://support.microsoft.com/en-us/office/create-a-to-do-list-and-tasks-in-onenote-with-copilot-95fdfbeb-d499-4024-9387-5416ab56a58e (fetched 2026-07-07)
