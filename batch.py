#!/usr/bin/env python3
"""batch.py init SETTING   -> 5 runs runs/SETTING_r1..r5
   batch.py step SETTING R -> resolve R-1 (if R>1) then write prompts R for all runs; print dispatch
   batch.py finish SETTING -> resolve 10"""
import os, sys, json, subprocess
ROOT = os.path.dirname(os.path.abspath(__file__))
def runs(setting): return [os.path.join(ROOT, "runs", f"{setting}_r{i}") for i in range(1, 6)]
def eng(d, *args):
    out = subprocess.run([sys.executable, os.path.join(ROOT, "engine.py"), *args], env={**os.environ, "RUN_DIR": d},
                         capture_output=True, text=True)
    if out.returncode: print(out.stderr); sys.exit(1)
    return out.stdout
cmd, setting = sys.argv[1], sys.argv[2]
if cmd == "init":
    for i, d in enumerate(runs(setting), 1): eng(d, "init", setting, str(100 + i))
elif cmd in ("step", "finish"):
    R = int(sys.argv[3]) if cmd == "step" else 11
    for d in runs(setting):
        if R > 1: eng(d, "resolve", str(R - 1))
        if cmd == "step": eng(d, "prompts", str(R))
    if cmd == "step":
        for d in runs(setting):
            s = json.load(open(os.path.join(d, "state.json")))
            print(os.path.basename(d), " ".join(f"{c}:{p['model']}" for c, p in sorted(s["players"].items()) if p["kind"] == "ai"))
