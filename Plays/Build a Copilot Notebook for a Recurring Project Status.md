---
type: play
scenario: "You write the same project status update every week from scraps of files, meeting notes, and emails scattered across a dozen places."
uses:
  - "[[Copilot Notebooks]]"
  - "[[Copilot Pages]]"
  - "[[Meeting Recap and Intelligent Recap]]"
  - "[[Turn a Notebook Into Office Files]]"
roles: [ops, exec, it]
difficulty: "setup needed"
---

**The ask**
Every recurring status update starts from zero: dig up the files, remember what was said in Tuesday's standup, find last week's write-up to see what changed. A Notebook fixes that by giving the project a single place that accumulates everything relevant, so the status update becomes a prompt against material that's already there instead of a fresh research pass.

**What you'll use**
- [[Copilot Notebooks]] — the persistent reference library that holds everything for the project
- [[Copilot Pages]] — feeds in prior status write-ups as a source
- [[Meeting Recap and Intelligent Recap]] — the Teams meeting notes you'll keep adding week over week
- [[Turn a Notebook Into Office Files]] — exports the status as a document once it's written

**Steps**
1. In the M365 Copilot app, create a new Notebook for the project.
2. Add sources: the relevant files from SharePoint or OneDrive, Teams meeting recaps from your status meetings, related emails, and any existing Copilot Page with a prior status write-up.
3. As the project runs, keep adding each week's meeting recap and any new files. The Notebook only stays useful if it stays current, so treat it as ongoing upkeep rather than a one-time upload.
4. When the status is due, prompt the Notebook to generate the update from everything inside it.
5. If the update needs to go out as a document or slide, use Turn a Notebook Into Office Files to export it.

**Prompts**
```
Using everything in this notebook, write this week's project status update:
what shipped, what's blocked, what's next, and any risks that came up in
this week's meetings.
```
```
Compare this week's notebook contents to last week's and call out what
changed.
```

**Watch out for**
Notebooks require a Copilot or Copilot Chat license plus SharePoint or OneDrive access; the underlying feature is available even on Chat-only licensing, but the update quality tracks how much of your work data the license lets it ground on, so it's noticeably stronger on the full add-on. The three-column layout is a 2026-06 change, so training material or screenshots from before then won't match what you see.

## Related
[[Pages & Notebooks]] · [[Copilot Pages]] · [[Teams]] · [[Prep for a Customer Call]]

[^1]: Get started with Microsoft 365 Copilot Notebooks — https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-notebooks (fetched 2026-07-07)
[^2]: How Microsoft 365 Copilot Notebooks works — https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works (fetched 2026-07-07)
