---
type: recipe
scenario: "The board deck is due, the inputs are scattered across a dozen files and threads, and it always eats a night."
uses:
  - "[[Copilot Notebooks]]"
  - "[[Turn a Notebook Into Office Files]]"
roles: [exec, finance]
difficulty: "setup needed"
---

**The ask**
A board pack is a compile job, financials, project updates, prior decks, the threads where things actually got decided, into one coherent narrative. Gather the sources into a grounded Notebook, then generate the deck from it.

**What you'll use**
- [Copilot Notebooks](../Surfaces/Pages%20%26%20Notebooks/Copilot%20Notebooks.md) — one workspace grounded on a fixed set of sources, so every answer draws on the same material
- [Turn a Notebook Into Office Files](../Surfaces/Pages%20%26%20Notebooks/Turn%20a%20Notebook%20Into%20Office%20Files.md) — generates the PowerPoint and a Word summary from that Notebook

**Steps**
1. Create a Notebook and add this cycle's sources, financials, project updates, the last board deck, key threads.
2. Ask questions inside it to shape the narrative: what's up, what's at risk, what needs a decision.
3. Generate a board-ready PowerPoint, and a Word summary, from the Notebook.
4. Edit for judgment and framing, the part that's still yours.

**Prompts**
```
From these sources, draft the three things the board most needs to know this
quarter and the two decisions we need from them.
```
```
Generate a board-ready PowerPoint from this notebook: performance, key risks,
and decisions needed.
```

**Watch out for**
Needs the add-on. Board material is often the most confidential content in the tenant; generated files inherit sensitivity labels, but confirm the label before you share. This is the one-off, high-stakes compile, for a standing cadence, the recurring-status notebook recipe is the better fit.

## Related
[Pages & Notebooks](../Surfaces/Pages%20%26%20Notebooks/README.md) · [Build a Copilot Notebook for a Recurring Project Status](Build%20a%20Copilot%20Notebook%20for%20a%20Recurring%20Project%20Status.md) · [Turn a Report Into a Deck](Turn%20a%20Report%20Into%20a%20Deck.md)

[^1]: Get started with Microsoft 365 Copilot Notebooks — https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-notebooks (fetched 2026-07-07)
[^2]: Microsoft 365 Copilot release notes — https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes (fetched 2026-07-07)
