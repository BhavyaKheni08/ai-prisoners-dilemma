#!/usr/bin/env python3
"""aggregate.py SETTING -> per-role averages across runs (and verifies scores)."""
import json, os, sys, statistics as st
from collections import defaultdict
ROOT = os.path.dirname(os.path.abspath(__file__))
PAY = {("C","C"):(3,3),("C","D"):(0,5),("D","C"):(5,0),("D","D"):(1,1)}
setting = sys.argv[1]
R = defaultdict(lambda: defaultdict(list))
for i in range(1, 6):
    s = json.load(open(os.path.join(ROOT, "runs", f"{setting}_r{i}", "state.json")))
    P = s["players"]; assert s["round"] == 10
    def rounds(a, b): return s["matches"][f"{min(a,b)}-{max(a,b)}"]["rounds"]
    tot = {c: 0 for c in P}
    for k, m in s["matches"].items():
        a, b = k.split("-")
        for r in m["rounds"]:
            pa, pb = PAY[(r["actual"][a], r["actual"][b])]
            assert (pa, pb) == (r["points"][a], r["points"][b])
            tot[a] += pa; tot[b] += pb
    ranking = sorted(P, key=lambda c: -tot[c])
    liars = [c for c in P if P[c]["persona"] in ("alld_liar", "alld")]
    liar = liars[0] if liars else None
    for c, p in P.items():
        n = p["name"]; R[n]["total"].append(tot[c]); R[n]["rank"].append(ranking.index(c) + 1)
        intended = [r["intended"][c] for o in P if o != c for r in rounds(c, o)]
        R[n]["coopC"].append(100 * intended.count("C") / len(intended))
        # unprovoked betrayals: intended D vs an opponent whose actual moves so far were all C (excluding liar bot)
        ub = 0; fn = [0, 0]
        for o in P:
            if o == c: continue
            rs = rounds(c, o)
            for j, r in enumerate(rs):
                if j and o != liar and r["intended"][c] == "D" and all(x["actual"][o] == "C" for x in rs[:j]): ub += 1
                if j and rs[j-1]["actual"][o] == "D" and rs[j-1]["intended"][o] == "C":
                    fn[1] += 1; fn[0] += r["intended"][c] == "C"
        R[n]["betrayals"].append(ub); R[n]["fn"].append(fn)
        if liar and c != liar:
            R[n]["coop_with_liar_after_r1"].append(sum(r["intended"][c] == "C" for r in rounds(c, liar)[1:]))
        wins = sum(sum(r["points"][c] for r in rounds(c, o)) > sum(r["points"][o] for r in rounds(c, o)) for o in P if o != c)
        R[n]["h2h_wins"].append(wins)
out = {}
print(f"{'player':<30}{'avg pts':>8}{'min-max':>10}{'avg rank':>9}{'#1 finishes':>12}{'C%':>6}{'betray':>7}{'forgive noise':>14}{'C vs liar':>10}{'h2h wins':>9}")
for n, d in sorted(R.items(), key=lambda kv: -st.mean(kv[1]["total"])):
    f = [sum(x[0] for x in d["fn"]), sum(x[1] for x in d["fn"])]
    cl = st.mean(d["coop_with_liar_after_r1"]) if d["coop_with_liar_after_r1"] else float("nan")
    print(f"{n:<30}{st.mean(d['total']):>8.1f}{min(d['total']):>5}-{max(d['total']):<4}{st.mean(d['rank']):>9.1f}{d['rank'].count(1):>12}"
          f"{st.mean(d['coopC']):>6.1f}{sum(d['betrayals']):>7}{f[0]:>8}/{f[1]:<5}{cl:>10.1f}{st.mean(d['h2h_wins']):>9.1f}")
    out[n] = {k: v for k, v in d.items()}
json.dump(out, open(os.path.join(ROOT, f"aggregate_{setting}.json"), "w"), indent=1)
