---
type: recipe
scenario: "You know what pivot you want out of a spreadsheet but not how to ask Excel Copilot for it."
uses:
  - "[[Work-Grounded Copilot Chat]]"
  - "[[Create Charts and PivotTables]]"
roles: [finance, ops, sales]
difficulty: "quick win"
---

**The ask**
You have a workbook and a rough idea of the summary you want (revenue by region, headcount by department, whatever it is), but writing a prompt that gets Excel Copilot to build the right PivotTable on the first try is its own skill. Let Copilot Chat write that prompt for you.

**What you'll use**
- [Work-Grounded Copilot Chat](../Surfaces/Copilot%20Chat/Work-Grounded%20Copilot%20Chat.md) — describe the pivot in plain language and get back a precise Excel Copilot prompt
- [Create Charts and PivotTables](../Surfaces/Excel/Create%20Charts%20and%20PivotTables.md) — the in-app Excel feature that actually builds the PivotTable and chart

**Steps**
1. Open Copilot Chat and describe your data (column names are enough) and the summary you're after.
2. Ask Chat to turn that into a specific, well-formed prompt for Excel Copilot.
3. Copy the prompt it gives you.
4. Open the workbook in Excel, open Copilot, and paste the prompt.
5. Review the PivotTable and chart Copilot builds, and ask a follow-up if a field is in the wrong place.

**Prompts**

Ask Copilot Chat to write the Excel prompt:
```
I have a workbook with columns: Region, Rep, Product, Units, Revenue, Month.
I want a PivotTable that shows total Revenue by Region and Month, broken out
by Product, with a PivotChart. Write me a clear, specific prompt I can paste
into Excel Copilot to build this.
```

Paste the result into Excel Copilot:
```
Create a PivotTable summarizing total Revenue by Region and Month, broken out
by Product as columns. Add a PivotChart showing the trend by Month for each
Region. Place the PivotTable on a new worksheet named "Revenue Summary."
```

**Watch out for**
Excel's in-app Copilot needs the Copilot add-on. Basic tier has no in-app Excel Copilot at all, so this recipe doesn't work if you're only licensed for Copilot Chat (Basic). The chat step that writes your prompt can run on either tier since it's not touching your actual data.

## Related
[Excel](../Surfaces/Excel/README.md) · [Copilot Chat](../Surfaces/Copilot%20Chat/README.md) · [Suggest Formulas in Excel](../Surfaces/Excel/Suggest%20Formulas%20in%20Excel.md) · [Find the Story in a Messy Spreadsheet](Find%20the%20Story%20in%20a%20Messy%20Spreadsheet.md)

[^1]: Microsoft 365 Copilot — top 10 things to try first — https://www.microsoft.com/en-us/microsoft-365-copilot/copilot-top-10-things-to-try-first (fetched 2026-07-07)
[^2]: Microsoft 365 Copilot prompt gallery — https://adoption.microsoft.com/en-us/copilot/prompt-gallery/ (fetched 2026-07-07)
