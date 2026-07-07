#!/usr/bin/env python3
# Counts for the finish-by report: feature notes by category (major/minor),
# new:true count, category-note count, and play count. Root derives from this
# file's location so a repo rename can't break it.
import os, glob, re, collections

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
feat = collections.defaultdict(lambda: {"major": 0, "minor": 0})
newcount = 0; total = 0; catcount = 0
def fm(txt):
    if not txt.startswith("---"): return {}
    end = txt.find("\n---", 3)
    d = {}
    for line in txt[3:end].splitlines():
        m = re.match(r"(\w+):\s*(.*)", line.strip())
        if m: d[m.group(1)] = m.group(2).strip()
    return d
for f in glob.glob(os.path.join(root, "*.md")):
    b = os.path.basename(f)[:-3]
    if b in ("_sources", "Copilot Features MOC", "Plays MOC", "README"): continue
    d = fm(open(f, encoding="utf-8").read())
    if "tier" in d:  # feature note
        total += 1
        cat = d.get("category", "?")
        tier = d.get("tier", "major")
        feat[cat]["minor" if tier == "minor" else "major"] += 1
        if d.get("new", "").lower() == "true": newcount += 1
    else:
        catcount += 1
plays = len(glob.glob(os.path.join(root, "Plays", "*.md")))
print("FEATURE NOTES BY CATEGORY (major / minor):")
gt_major = gt_minor = 0
for cat in sorted(feat):
    mj = feat[cat]["major"]; mn = feat[cat]["minor"]
    gt_major += mj; gt_minor += mn
    print(f"  {cat:28} {mj:2} major   {mn:2} minor   ({mj + mn} total)")
print(f"\n  TOTALS: {total} feature notes = {gt_major} major + {gt_minor} minor")
print(f"  Category notes (non-feature): {catcount}")
print(f"  Feature notes with new:true : {newcount}")
print(f"  Play notes                  : {plays}")
print(f"  Grand total .md (excl _sources/MOCs/README): {total + catcount + plays}")
