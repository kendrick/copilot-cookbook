#!/usr/bin/env python3
# Refresh triage: what to look at before a monthly/quarterly update pass, so a
# refresh is a diff and not a rebuild. Read-only. Reports three things:
#   1. how stale the fetch baseline is (re-pull sources past SOURCE_DAYS),
#   2. new: true notes old enough to age out (added > NEW_DAYS),
#   3. Preview / Rolling out notes to re-check for GA.
# Run it first each refresh; it turns "where do I even look" into a worklist.
# Root derives from this file's location so a repo rename can't break it.
import os, re, glob, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DAYS = 30   # Copilot ships ~monthly; past this the fetch baseline is stale
NEW_DAYS = 90      # how long a capability keeps its new: true badge
TODAY = datetime.date.today()

def fm(path):
    txt = open(path, encoding="utf-8").read()
    if not txt.startswith("---"):
        return {}
    end = txt.find("\n---", 3)
    d = {}
    for line in txt[3:end].splitlines():
        m = re.match(r"(\w+):\s*(.*)", line.strip())
        if m:
            d[m.group(1)] = m.group(2).strip()
    return d

def parse_ym(s):    # added: YYYY-MM (month precision) -> first of month
    m = re.match(r"(\d{4})-(\d{2})$", s or "")
    return datetime.date(int(m[1]), int(m[2]), 1) if m else None

def parse_ymd(s):   # fetched: YYYY-MM-DD
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s or "")
    return datetime.date(int(m[1]), int(m[2]), int(m[3])) if m else None

def rel(p):
    return os.path.relpath(p, ROOT)

notes = [n for n in glob.glob(os.path.join(ROOT, "Surfaces", "*", "*.md"))
         + glob.glob(os.path.join(ROOT, "Recipes", "*.md"))
         if os.path.basename(n) != "README.md"]

print("=" * 64)
print(f"REFRESH TRIAGE  (today {TODAY}, thresholds: source {SOURCE_DAYS}d, new {NEW_DAYS}d)")

# 1) fetch baseline from _sources.md, plus per-note drift after incremental runs
print("=" * 64)
print("SOURCE FRESHNESS")
src = os.path.join(ROOT, "_sources.md")
base = None
if os.path.isfile(src):
    m = re.search(r"fetched \*\*(\d{4}-\d{2}-\d{2})\*\*", open(src, encoding="utf-8").read())
    base = parse_ymd(m[1]) if m else None
if base:
    age = (TODAY - base).days
    print(f"  _sources.md baseline: {base} ({age}d ago)"
          f"{'   << OVERDUE — re-pull release notes + monthly What'+chr(39)+'s New' if age > SOURCE_DAYS else ''}")
else:
    print("  _sources.md: no 'All fetched **DATE**' line found")
dated = sorted((d, n) for d, n in
               ((parse_ymd(fm(n).get("fetched", "")), n) for n in notes) if d)
if dated:
    stale = [1 for d, _ in dated if (TODAY - d).days > SOURCE_DAYS]
    print(f"  oldest note fetched: {dated[0][0]} ({(TODAY-dated[0][0]).days}d ago); "
          f"{len(stale)}/{len(dated)} notes past {SOURCE_DAYS}d")

# 2) new: true notes old enough to age out
print("=" * 64)
print(f"NEW FLAGS TO AGE OUT  (new: true with added > {NEW_DAYS}d)")
aged, undated = [], []
for n in notes:
    d = fm(n)
    if d.get("new", "").lower() != "true":
        continue
    added = parse_ym(d.get("added", ""))
    if added is None:
        undated.append(n)
    elif (TODAY - added).days > NEW_DAYS:
        aged.append(((TODAY - added).days, added, n))
for days, added, n in sorted(aged, reverse=True):
    print(f"  {added}  ({days}d)  {rel(n)}   -> set new: false")
if not aged:
    print("  none")
if undated:
    print(f"  ! new: true with no added date ({len(undated)}) — add one so it can age out:")
    for n in undated:
        print(f"      {rel(n)}")

# 3) Preview / Rolling out to re-check for GA
print("=" * 64)
print("PRE-GA NOTES TO RE-CHECK  (status != GA)")
prega = sorted((s, n) for s, n in
               ((fm(n).get("status"), n) for n in notes) if s and s != "GA")
for s, n in prega:
    print(f"  {s:14} {rel(n)}")
if not prega:
    print("  none")
print("=" * 64)
