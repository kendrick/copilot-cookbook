---
type: recipe
scenario: "The numbers you need are spread across three or four workbooks, and reconciling them by hand is a morning you don't have."
uses:
  - "[[Reference Other Workbooks]]"
  - "[[Agent Mode in Excel]]"
roles: [finance, ops, exec]
difficulty: "setup needed"
---

**The ask**
The monthly numbers live in separate files, one per region or per team, and someone has to stitch them into a single view before anyone can read the trend. Let Copilot pull from the other workbooks and plan the consolidation before it touches your sheet.

**What you'll use**
- [Reference Other Workbooks](../Surfaces/Excel/Reference%20Other%20Workbooks.md) — imports data from other files in OneDrive or SharePoint without copy-paste
- [Agent Mode in Excel](../Surfaces/Excel/Agent%20Mode%20in%20Excel.md) — proposes a multi-step plan for the consolidation and waits for your approval before running it

**Steps**
1. Open a fresh workbook and turn on Agent Mode in the Copilot pane.
2. Name the source workbooks and describe the consolidated view you want.
3. Read the plan Copilot proposes, and approve or adjust it before it runs.
4. Once the combined table is built, ask for the chart that tells the story.

**Prompts**
```
Import the monthly sales data from East.xlsx, West.xlsx, and Central.xlsx,
then build one table with a row per region and a column per month.
```
```
Add a column for quarter-over-quarter change and chart the three regions
against each other.
```

**Watch out for**
Both features need the Copilot add-on, and the source workbooks have to be reachable in OneDrive or SharePoint. Agent Mode's whole point is that it plans first, so actually read the plan before you approve it, especially when it's about to restructure real numbers.

## Related
[Excel](../Surfaces/Excel/README.md) · [Find the Story in a Messy Spreadsheet](Find%20the%20Story%20in%20a%20Messy%20Spreadsheet.md) · [Draft an Excel Pivot From a Chat-Generated Prompt](Draft%20an%20Excel%20Pivot%20From%20a%20Chat-Generated%20Prompt.md)

[^1]: Get started with Copilot in Excel — https://support.microsoft.com/en-us/Excel/copilot/get-started-with-copilot-in-excel (fetched 2026-07-07)
