#!/usr/bin/env python3
"""roles.py SETTING[,SETTING2...] R [TAG] -> for each AI role: model and prompt paths (one per run, all settings).
Writes tasks/<TAG>_RR_<slug>.txt (TAG defaults to the setting string)."""
import json, os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
settings, R = sys.argv[1].split(","), int(sys.argv[2])
tag = sys.argv[3] if len(sys.argv) > 3 else sys.argv[1]
roles = {}
for setting in settings:
    for i in range(1, 6):
        d = os.path.join(ROOT, "runs", f"{setting}_r{i}")
        s = json.load(open(os.path.join(d, "state.json")))
        for c, p in sorted(s["players"].items()):
            if p["kind"] == "ai":
                roles.setdefault(p["name"], (p["model"], []))[1].append(f"{d}/players/{c}/round_{R:02d}_prompt.md")
SLUG = {"competitive": "comp", "cooperative": "coop"}
os.makedirs(os.path.join(ROOT, "tasks"), exist_ok=True)
for name, (model, paths) in roles.items():
    persona = name.split("(")[1].rstrip(")")
    size = name.split()[0].lower()
    slug = SLUG.get(persona, size)
    with open(os.path.join(ROOT, "tasks", f"{tag}_{R:02d}_{slug}.txt"), "w") as f:
        f.write("\n".join(paths) + "\n")
    print(f"TASK {tag}_{R:02d}_{slug} {model} ({len(paths)} games)")
