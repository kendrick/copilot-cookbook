# Open Questions

<!-- Things that are unresolved and should not be guessed at. -->
<!-- Agents encountering these should ask rather than assume. -->

## Brand Kit license tier — conflict between the note and a fresh source

`Surfaces/Create/Brand Kit for Visuals.md` lists `license: Chat (Basic)`, sourced from the June 2026 What's New blog. A 2026-07-13 fetch of the dedicated Brand Kit support page (create-and-manage-official-brand-kits-in-the-microsoft-365-copilot-app) says it requires a paid "Microsoft 365 Copilot Premium" license. "Premium" is a SKU name the vault doesn't otherwise use, so it wasn't flipped on a single Haiku-fetched read (per the antipattern about over-claiming a SKU). Recipe "Produce On-Brand Visuals Without a Designer" sidesteps it by calling Brand Kit "a paid, admin-configured capability" without naming a tier. Resolve on the next refresh: re-fetch the Brand Kit page directly and correct the note's license if the paid-tier claim holds.

## Features still uncovered by any recipe after Batch 2

Deliberately left for a later pass: Copilot in Loop (deprecated integration, mid-transition to Pages), Copilot Studio (only reached via "Stand Up a No-Code Team Agent"), Agent Store (same), and Suggest Formulas in Excel (adjacent to covered Excel recipes). None is a gap worth a thin recipe today.
