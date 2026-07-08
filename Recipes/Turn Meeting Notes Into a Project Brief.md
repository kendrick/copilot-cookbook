---
type: recipe
scenario: "A kickoff meeting produced a pile of notes and half-assigned action items, and you need a real project brief out of it before end of day."
uses:
  - "[[Meeting Recap and Intelligent Recap]]"
  - "[[Create Tasks From Notes]]"
  - "[[Draft with Copilot in Word]]"
  - "[[Ground a Draft on Your Files]]"
roles: [ops, it, exec]
difficulty: "quick win"
---

**The ask**
The meeting produced a decision and a scattered list of who's doing what. Nobody wants to read raw notes to find that out, so turn them into a brief with a shape: goals, scope, owners, timeline.

**What you'll use**
- [Meeting Recap and Intelligent Recap](../Surfaces/Teams/Meeting%20Recap%20and%20Intelligent%20Recap.md) — captures notes and action items from the meeting itself
- [Create Tasks From Notes](../Surfaces/OneNote%20%26%20Loop/Create%20Tasks%20From%20Notes.md) — turns those action items into trackable tasks
- [Draft with Copilot in Word](../Surfaces/Word/Draft%20with%20Copilot%20in%20Word.md) with [Ground a Draft on Your Files](../Surfaces/Word/Ground%20a%20Draft%20on%20Your%20Files.md) — writes the brief from the notes

**Steps**
1. Use Meeting Recap and Intelligent Recap during or right after the meeting to capture notes and action items.
2. In OneNote or Loop, turn the action items into tasks so they don't get lost in a doc nobody reopens.
3. In Word, draft the brief and ground it on the meeting notes and task list so it pulls real content instead of a generic template.
4. Tighten the language with a rewrite pass once the structure is right.

**Prompts**
```
Create a list of notes and action items from this meeting.
```
```
Draft a one-page project brief from these meeting notes and action items.
Include goals, scope, owners, and a rough timeline.
```

**Watch out for**
Create Tasks From Notes and in-app Word drafting both need the Copilot add-on. Grounding a Word draft on a file only works if that file is already in SharePoint or OneDrive and you have access to it, so save the notes there before you start drafting.

## Related
[Word](../Surfaces/Word/README.md) · [Teams](../Surfaces/Teams/README.md) · [OneNote & Loop](../Surfaces/OneNote%20%26%20Loop/README.md) · [Build a Copilot Notebook for a Recurring Project Status](Build%20a%20Copilot%20Notebook%20for%20a%20Recurring%20Project%20Status.md)

[^1]: Microsoft 365 Copilot — top 10 things to try first — https://www.microsoft.com/en-us/microsoft-365-copilot/copilot-top-10-things-to-try-first (fetched 2026-07-07)
[^2]: Microsoft 365 Copilot prompt gallery — https://adoption.microsoft.com/en-us/copilot/prompt-gallery/ (fetched 2026-07-07)
