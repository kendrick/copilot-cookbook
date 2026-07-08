---
type: recipe
scenario: "You're starting a deck from scratch and want it built from your team's actual reports and meeting notes instead of a blank template."
uses:
  - "[[Ground a Deck in Your Work Content]]"
  - "[[Build a Presentation With Copilot]]"
  - "[[Generate Images in PowerPoint]]"
  - "[[Rewrite and Summarize Slides]]"
roles: [marketing, ops, sales]
difficulty: "quick win"
---

**The ask**
The charter, the comparison data, the meeting notes: it's all sitting in files across the team already. Point PowerPoint at that content instead of writing the deck from a blank slide.

**What you'll use**
- [Ground a Deck in Your Work Content](../Surfaces/PowerPoint/Ground%20a%20Deck%20in%20Your%20Work%20Content.md) — points Copilot at the specific files it should build from
- [Build a Presentation With Copilot](../Surfaces/PowerPoint/Build%20a%20Presentation%20With%20Copilot.md) — drafts the outline and slides
- [Generate Images in PowerPoint](../Surfaces/PowerPoint/Generate%20Images%20in%20PowerPoint.md) — custom visuals where a stock image won't cut it
- [Rewrite and Summarize Slides](../Surfaces/PowerPoint/Rewrite%20and%20Summarize%20Slides.md) — a tightening pass once the structure holds

**Steps**
1. Start a new deck and ground it in your work content, pointing Copilot at the files it should pull from.
2. Ask Copilot to build the outline and draft slides.
3. Use Generate Images in PowerPoint for any visuals the content calls for.
4. Refine with Rewrite and Summarize Slides once the structure is right.

**Prompts**
```
Create a presentation outlining our product charter based on these meeting
notes.
```
```
Build a deck from this product comparison report: one slide per
competitor, plus a summary recommendation slide.
```

**Watch out for**
Ground a Deck in Your Work Content and Generate Images in PowerPoint are both new (2026-06 and 2026-07); check tenant rollout status before you build a workflow around either. Both need the Copilot add-on, since Basic tier has no in-app PowerPoint Copilot at all.

## Related
[PowerPoint](../Surfaces/PowerPoint/README.md) · [Create](../Surfaces/Create/README.md) · [Turn a Report Into a Deck](Turn%20a%20Report%20Into%20a%20Deck.md)

[^1]: Microsoft 365 Copilot prompt gallery — https://adoption.microsoft.com/en-us/copilot/prompt-gallery/ (fetched 2026-07-07)
