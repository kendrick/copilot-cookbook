---
type: play
scenario: "A spreadsheet lands in your inbox with inconsistent formatting and no obvious story, and you need the trends without building the formulas yourself."
uses:
  - "[[Organize Data With Copilot]]"
  - "[[Analyze Data and Surface Insights]]"
  - "[[Analyst]]"
roles: [finance, ops, marketing]
difficulty: "quick win"
---

**The ask**
Someone hands you a workbook: blank rows, mismatched date formats, a column that's text in some rows and numbers in others. Before you can find anything useful in it, you have to clean it up. Let Copilot do both passes.

**What you'll use**
- [[Organize Data With Copilot]] — cleans up headers, types, and duplicate rows in Excel
- [[Analyze Data and Surface Insights]] — surfaces trends and outliers once the data is usable
- [[Analyst]] — for statistical work Excel Copilot isn't built for, like correlations or forecasting

**Steps**
1. Open the workbook and ask Excel Copilot to clean and organize the data.
2. Ask Copilot to analyze the cleaned data and surface the trends, outliers, and top or bottom performers.
3. For deeper statistical work, upload the file to the Analyst agent in the Copilot app.
4. Turn the strongest finding into a chart directly in Excel.

**Prompts**

Clean-up pass:
```
This data has inconsistent formatting and blank rows. Standardize the headers,
fix data types, remove duplicate rows, and flag any rows with missing values.
```

Insight pass:
```
Analyze this data and tell me the most important trends or outliers I should
know about. Where's revenue concentrated? What's changed month over month?
```

**Watch out for**
Organize Data With Copilot and Analyze Data and Surface Insights are both in-app Excel features and need the Copilot add-on. Analyst is a separate agent with roughly 25 monthly queries shared with Researcher, so save it for questions that actually need statistical modeling rather than a quick trend check.

## Related
[[Excel]] · [[Researcher & Analyst]] · [[Draft an Excel Pivot From a Chat-Generated Prompt]]

[^1]: Microsoft 365 Copilot prompt gallery — https://adoption.microsoft.com/en-us/copilot/prompt-gallery/ (fetched 2026-07-07)
[^2]: Get started with Analyst in Microsoft 365 Copilot — https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-analyst-in-microsoft-365-copilot (fetched 2026-07-07)
