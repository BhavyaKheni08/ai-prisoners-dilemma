#!/usr/bin/env python3
"""Analyze finished tournament; writes results.json and prints key facts."""
import json, os
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
s = json.load(open(os.path.join(BASE, "state.json")))
P = s["players"]
codes = sorted(P)


def rounds(a, b):
    k = f"{min(a,b)}-{max(a,b)}"
    return s["matches"][k]["rounds"]


tot = defaultdict(int); wins = defaultdict(int); losses = defaultdict(int); ties = defaultdict(int)
h2h = {}
for a in codes:
    for b in codes:
        if a == b: continue
        rs = rounds(a, b)
        pa = sum(r["points"][a] for r in rs); pb = sum(r["points"][b] for r in rs)
        h2h[f"{a}>{b}"] = [pa, pb]
        tot[a] += pa
        if pa > pb: wins[a] += 1
        elif pa < pb: losses[a] += 1
        else: ties[a] += 1

stats = {}
for c in codes:
    intended = []; actual = []
    forgive_noise = [0, 0]   # opponent's last actual D was noise (they intended C): did c intend C next?
    respond_real_d = [0, 0]  # opponent's last actual D was intentional
    first_defect = []        # c defected first (intended D when opponent's previous actual moves all C)
    for o in codes:
        if o == c: continue
        rs = rounds(c, o)
        for i, r in enumerate(rs):
            intended.append(r["intended"][c]); actual.append(r["actual"][c])
            if i > 0:
                prev = rs[i - 1]
                if prev["actual"][o] == "D":
                    bucket = forgive_noise if prev["intended"][o] == "C" else respond_real_d
                    bucket[1] += 1
                    if r["intended"][c] == "C": bucket[0] += 1
            if r["intended"][c] == "D" and all(x["actual"][o] == "C" for x in rs[:i]):
                first_defect.append((o, r["round"]))
    stats[c] = {
        "name": P[c]["name"], "kind": P[c]["kind"], "total": tot[c],
        "wins": wins[c], "losses": losses[c], "ties": ties[c],
        "intended_C": round(100 * intended.count("C") / len(intended), 1),
        "actual_C": round(100 * actual.count("C") / len(actual), 1),
        "forgive_noise": forgive_noise, "after_real_D_coop": respond_real_d,
        "unprovoked_defections": first_defect,
    }

# Pair type cooperation
def mutual_c_rate(group_a, group_b):
    n = m = 0
    for a in group_a:
        for b in group_b:
            if a >= b: continue
            for r in rounds(a, b):
                n += 1; m += (r["actual"][a] == "C" and r["actual"][b] == "C")
    return round(100 * m / n, 1) if n else None

ai = [c for c in codes if P[c]["kind"] == "ai"]
out = {"stats": stats, "h2h": h2h, "players": P,
       "mutual_C_ai_vs_ai": mutual_c_rate(ai, ai)}
json.dump(out, open(os.path.join(BASE, "results.json"), "w"), indent=1)

print("LEADERBOARD")
for c in sorted(codes, key=lambda c: -tot[c]):
    st = stats[c]
    print(f"{c} {st['name']:<28} {st['total']:>4}  W{st['wins']} L{st['losses']} T{st['ties']}  "
          f"intC {st['intended_C']}%  forgive-noise {st['forgive_noise']}  after-real-D-coop {st['after_real_D_coop']}  "
          f"unprovoked D {st['unprovoked_defections']}")
print("AI-vs-AI mutual C %:", out["mutual_C_ai_vs_ai"])
print("\nHEAD TO HEAD (row player points vs column)")
print("    " + "".join(f"{o:>8}" for o in codes))
for a in codes:
    print(f"{a:>3} " + "".join(f"{'—':>8}" if a == b else f"{h2h[f'{a}>{b}'][0]:>4}-{h2h[f'{a}>{b}'][1]:<3}" for b in codes))
