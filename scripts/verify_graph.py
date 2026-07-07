#!/usr/bin/env python3
# Graph-integrity check for the vault: reports broken wikilinks and orphan notes.
# Root derives from this file's location (scripts/ lives under the repo root), so
# it survives a repo rename — an earlier copy hardcoded the old path and broke.
import os, re, glob, collections

# Scaffolding/meta docs that live at the repo root but aren't part of the vault
# graph — they carry illustrative [[placeholders]] and shouldn't count as notes.
SKIP = {"CLAUDE", "AGENTS", "PROMPT_INITIAL", "PROMPT_HANDOFF"}
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = [f for f in glob.glob(os.path.join(root, "*.md")) + glob.glob(os.path.join(root, "Plays", "*.md"))
         if os.path.basename(f)[:-3] not in SKIP]
# basename without .md -> canonical note name
names = set()
for f in files:
    b = os.path.basename(f)[:-3]
    names.add(b)
link_re = re.compile(r"\[\[([^\]]+)\]\]")
code_re = re.compile(r"`[^`]*`")  # strip inline-code so prose examples like `[[wikilinks]]` don't read as links
inbound = collections.Counter()
broken = collections.defaultdict(list)
for f in files:
    txt = code_re.sub("", open(f, encoding="utf-8").read())
    src = os.path.basename(f)[:-3]
    for m in link_re.findall(txt):
        target = m.split("|")[0].split("#")[0].strip()
        if target == "": continue
        if target in names:
            if target != src:
                inbound[target] += 1
        else:
            broken[src].append(target)
print("=== TOTAL notes:", len(names))
print("\n=== BROKEN LINKS (target file missing) ===")
nb = 0
for src, tgts in sorted(broken.items()):
    for t in tgts:
        print(f"  [{src}] -> [[{t}]]"); nb += 1
if nb == 0: print("  none")
print(f"  total broken: {nb}")
# Orphans: files with zero inbound (exclude MOCs, README, _sources)
exclude = {"Copilot Features MOC", "Plays MOC", "README", "_sources"}
print("\n=== ORPHANS (no inbound wikilink) ===")
no = 0
for n in sorted(names):
    if n in exclude: continue
    if inbound[n] == 0:
        print("  " + n); no += 1
if no == 0: print("  none")
print(f"  total orphans: {no}")
