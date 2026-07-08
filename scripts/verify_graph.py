#!/usr/bin/env python3
# Graph-integrity check: reports broken markdown links and orphan notes across
# the nested vault. The vault moved from name-resolved [[wikilinks]] to
# path-resolved [md](links), so this validates that every relative link target
# actually exists on disk. Root derives from this file's location so a repo
# rename can't break it.
import os, re, sys, urllib.parse, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Non-vault trees and root scaffolding docs are not part of the link graph.
SKIP_DIRS = {".git", "_working-memory", "scripts", ".claude", ".github", "_research"}
SKIP_ROOT_FILES = {"CLAUDE.md", "AGENTS.md"}
# Index / entry files legitimately have no inbound link; don't flag as orphans.
ENTRY = {"README.md", "Surfaces/README.md", "Recipes/README.md", "_sources.md"}

link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
fence_re = re.compile(r"```.*?```", re.S)
inline_re = re.compile(r"`[^`]*`")

def vault_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, ROOT)
            if os.path.dirname(rel) == "" and fn in SKIP_ROOT_FILES:
                continue
            yield full, rel

files = list(vault_files())
inbound = collections.Counter()
broken = []
for full, rel in files:
    txt = open(full, encoding="utf-8").read()
    txt = inline_re.sub("", fence_re.sub("", txt))  # ignore links inside code
    src_dir = os.path.dirname(full)
    for target in link_re.findall(txt):
        t = target.strip().split("#", 1)[0]
        if not t or t.startswith(("http://", "https://", "mailto:")):
            continue
        dec = urllib.parse.unquote(t)
        dest = os.path.normpath(os.path.join(src_dir, dec))
        if os.path.isfile(dest):
            drel = os.path.relpath(dest, ROOT)
            if drel != rel:
                inbound[drel] += 1
        else:
            broken.append((rel, target))

print(f"=== TOTAL vault notes: {len(files)}")
print("\n=== BROKEN LINKS (target file missing) ===")
for src, t in sorted(broken):
    print(f"  [{src}] -> ({t})")
print("  none" if not broken else f"  total broken: {len(broken)}")

print("\n=== ORPHANS (no inbound link) ===")
orphans = [rel for _, rel in files if rel not in ENTRY and inbound[rel] == 0]
for o in sorted(orphans):
    print(f"  {o}")
print("  none" if not orphans else f"  total orphans: {len(orphans)}")

sys.exit(1 if broken or orphans else 0)
