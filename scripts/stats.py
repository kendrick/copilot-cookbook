#!/usr/bin/env python3
# Counts for the finish-by report: feature notes by surface (major/minor),
# new:true count, surface count, and recipe count. Walks the nested vault;
# category is the surface folder name, the folder's README.md is its index.
# Root derives from this file's location so a repo rename can't break it.
import os, re, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECIPES = "Plays"  # folder name for scenario recipes; update if renamed

def fm(txt):
    if not txt.startswith("---"):
        return {}
    end = txt.find("\n---", 3)
    d = {}
    for line in txt[3:end].splitlines():
        m = re.match(r"(\w+):\s*(.*)", line.strip())
        if m:
            d[m.group(1)] = m.group(2).strip()
    return d

feat = collections.defaultdict(lambda: {"major": 0, "minor": 0})
newcount = surfaces = 0
for f in glob.glob(os.path.join(ROOT, "Surfaces", "*", "*.md")):
    surface = os.path.basename(os.path.dirname(f))
    if os.path.basename(f) == "README.md":
        surfaces += 1
        continue
    d = fm(open(f, encoding="utf-8").read())
    tier = "minor" if d.get("tier") == "minor" else "major"
    feat[surface][tier] += 1
    if d.get("new", "").lower() == "true":
        newcount += 1

recipes = [f for f in glob.glob(os.path.join(ROOT, RECIPES, "*.md"))
           if os.path.basename(f) != "README.md"]

print("FEATURE NOTES BY SURFACE (major / minor):")
gt_major = gt_minor = 0
for s in sorted(feat):
    mj, mn = feat[s]["major"], feat[s]["minor"]
    gt_major += mj; gt_minor += mn
    print(f"  {s:28} {mj:2} major   {mn:2} minor   ({mj + mn} total)")
total = gt_major + gt_minor
print(f"\n  TOTALS: {total} feature notes = {gt_major} major + {gt_minor} minor")
print(f"  Surface notes (README.md indexes): {surfaces}")
print(f"  Feature notes with new:true      : {newcount}")
print(f"  Recipe notes                     : {len(recipes)}")
print(f"  Grand total notes (excl indexes) : {total + len(recipes)}")
