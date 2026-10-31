#!/usr/bin/env python3
"""AI-agent Axelrod tournament engine.

Commands:
  init               create players and empty state
  prompts R          write round-R prompt files for every AI player
  resolve R          read AI responses, compute bot moves, apply noise, score
  status             print current standings
"""
import json, os, random, sys, itertools

BASE = os.environ.get("RUN_DIR") or os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(BASE, "state.json")
NOISE = 0.10
PAYOFF = {("C", "C"): (3, 3), ("C", "D"): (0, 5), ("D", "C"): (5, 0), ("D", "D"): (1, 1)}

ROSTERS = {}
ROSTERS["S1"] = [
    # (internal name, kind, model, persona)
    ("Small model (neutral)",   "ai",  "haiku",  "neutral"),
    ("Medium model (neutral)",  "ai",  "sonnet", "neutral"),
    ("Large model (neutral)",   "ai",  "opus",   "neutral"),
    ("Medium model (competitive)", "ai", "sonnet", "competitive"),
    ("Medium model (cooperative)", "ai", "sonnet", "cooperative"),
    ("Tit-for-Tat bot",         "bot", None,     "tft"),
    ("Random bot",              "bot", None,     "random"),
    ("Always-Cheat liar bot",   "bot", None,     "alld_liar"),
]
ROSTERS["S2"] = [
    ("Small model (neutral)",   "ai",  "haiku",  "neutral"),
    ("Medium model (neutral)",  "ai",  "sonnet", "neutral"),
    ("Large model (neutral)",   "ai",  "opus",   "neutral"),
    ("Large model (competitive)", "ai", "opus", "competitive"),
    ("Small model (cooperative)", "ai", "haiku", "cooperative"),
    ("Tit-for-Tat bot",         "bot", None,     "tft"),
    ("Random bot",              "bot", None,     "random"),
    ("Always-Cheat liar bot",   "bot", None,     "alld_liar"),
]

# Setting B: no talking (messages disabled). B1 = S1 roster, cheat bot silent; B2 = S1 roster, Grudger replaces cheat bot.
ROSTERS["B1"] = ROSTERS["S1"][:7] + [("Always-Cheat bot", "bot", None, "alld")]
ROSTERS["B2"] = ROSTERS["S1"][:7] + [("Grudger bot", "bot", None, "grudger")]
NO_MSG = {"B1", "B2"}

PERSONA_TEXT = {
    "neutral": "Your goal: earn as many TOTAL points as possible, summed across all of your matches.",
    "competitive": ("Your goal: BEAT your opponents. In each match, try to finish with MORE points "
                    "than that opponent. Winning matches is what counts for you."),
    "cooperative": ("Your goal: earn as many TOTAL points as possible, summed across all of your matches. "
                    "You personally value fairness and mutual benefit, and prefer outcomes where both sides do well."),
}

LIAR_MSGS = [
    "Hi! I always cooperate. Let's both play C every round and get 3 points each.",
    "If anything looked like D from me, it was the random noise. I'm playing C, promise.",
    "Trust me, mutual cooperation is best for both of us. I'm sticking with C.",
]


def load():
    with open(STATE) as f:
        return json.load(f)


def save(s):
    with open(STATE, "w") as f:
        json.dump(s, f, indent=1)


def init(setting="S1", seed=7):
    ROSTER = ROSTERS[setting]
    os.makedirs(BASE, exist_ok=True)
    rng = random.Random(seed)
    codes = list("ABCDEFGH")
    rng.shuffle(codes)
    players = {}
    for code, (name, kind, model, persona) in zip(codes, ROSTER):
        players[code] = {"name": name, "kind": kind, "model": model, "persona": persona}
        os.makedirs(os.path.join(BASE, "players", code), exist_ok=True)
    matches = {}
    for a, b in itertools.combinations(sorted(players), 2):
        matches[f"{a}-{b}"] = {"rounds": []}
    s = {"players": players, "matches": matches, "round": 0, "setting": setting, "seed": seed, "log": []}
    save(s)
    print("Players:")
    for c in sorted(players):
        print(f"  {c}: {players[c]['name']}")


def key(a, b):
    return f"{min(a,b)}-{max(a,b)}"


def view(s, me, opp):
    """History of match me vs opp from me's perspective."""
    out = []
    for r in s["matches"][key(me, opp)]["rounds"]:
        out.append({
            "round": r["round"],
            "my_intended": r["intended"][me], "my_actual": r["actual"][me],
            "their_actual": r["actual"][opp],
            "my_points": r["points"][me], "their_points": r["points"][opp],
            "msg_from_them": r["msg"].get(opp, ""), "msg_from_me": r["msg"].get(me, ""),
        })
    return out


def reputation(s, target, viewer):
    moves = []
    for k, m in s["matches"].items():
        a, b = k.split("-")
        if target not in (a, b) or viewer in (a, b):
            continue
        moves += [r["actual"][target] for r in m["rounds"]]
    if not moves:
        return "no record yet"
    pc = 100 * moves.count("C") / len(moves)
    return f"{pc:.0f}% C over {len(moves)} moves vs other players"


def totals(s):
    t = {c: 0 for c in s["players"]}
    for m in s["matches"].values():
        for r in m["rounds"]:
            for c, p in r["points"].items():
                t[c] += p
    return t


def prompts(R):
    s = load()
    assert s["round"] == R - 1, f"state is at round {s['round']}"
    tot = totals(s)
    nomsg = s.get("setting") in NO_MSG
    for me, p in s["players"].items():
        if p["kind"] != "ai":
            continue
        opps = sorted(o for o in s["players"] if o != me)
        L = []
        L.append(f"# Repeated Prisoner's Dilemma tournament — you are Player {me}\n")
        L.append(PERSONA_TEXT[p["persona"]] + "\n")
        L.append("## Rules\n"
                 f"- You play a separate repeated match against each of {len(opps)} opponents: {', '.join(opps)}. "
                 "Opponents are identified only by letter; you don't know what kind of player each is.\n"
                 "- Each round, in every match, both players simultaneously choose C (cooperate) or D (defect).\n"
                 "- Points per round: both C → 3 each; both D → 1 each; you D & they C → you 5, they 0; you C & they D → you 0, they 5.\n"
                 f"- This is round {R}. The tournament may end after ANY round; you will not be told in advance which round is last.\n"
                 "- NOISE: every move has a 10% chance of being accidentally flipped (C↔D). You see your own intended "
                 "and actual move; your opponent only ever sees your ACTUAL move. Likewise you only see their actual moves.\n"
                 + ("" if nomsg else "- MESSAGES: with each move you may send a short message (max 25 words) to that opponent. "
                 "It is delivered at the start of the next round. Messages are not binding — anyone may lie.\n") +
                 "- REPUTATION: for each opponent you see how often they actually played C in their matches against OTHER players so far.\n")
        L.append(f"## Your current total: {tot[me]} points\n")
        for o in opps:
            h = view(s, me, o)
            L.append(f"### Match vs Player {o}")
            L.append(f"Reputation of {o}: {reputation(s, o, me)}")
            if not h:
                L.append("No rounds played yet.\n")
                continue
            mp = sum(x["my_points"] for x in h); tp = sum(x["their_points"] for x in h)
            L.append(f"Match score so far: you {mp} – {o} {tp}")
            L.append("| Rd | you intended | you actual | they actual | your pts | their pts |")
            L.append("|---|---|---|---|---|---|")
            for x in h:
                L.append(f"| {x['round']} | {x['my_intended']} | {x['my_actual']} | {x['their_actual']} | {x['my_points']} | {x['their_points']} |")
            last = h[-1]
            if nomsg:
                L.append("")
                continue
            L.append(f"Message they sent last round: {json.dumps(last['msg_from_them']) if last['msg_from_them'] else '(none)'}")
            L.append(f"Message you sent last round: {json.dumps(last['msg_from_me']) if last['msg_from_me'] else '(none)'}\n")
        resp = os.path.join(BASE, "players", me, f"round_{R:02d}_response.json")
        L.append("## Your answer\n"
                 f"Write ONLY a JSON file to `{resp}` with this exact shape:\n"
                 "```json\n{\n  \"moves\": {" + ", ".join(f"\"{o}\": \"C or D\"" for o in opps) + "},\n"
                 + ("" if nomsg else "  \"messages\": {" + ", ".join(f"\"{o}\": \"text or empty\"" for o in opps) + "},\n") +
                 "  \"reasoning\": \"1-3 sentences on your overall thinking this round\"\n}\n```\n"
                 "Every opponent must have a move of exactly \"C\" or \"D\".")
        path = os.path.join(BASE, "players", me, f"round_{R:02d}_prompt.md")
        with open(path, "w") as f:
            f.write("\n".join(L))
    print(f"prompts for round {R} written")


def bot_move(s, me, opp, R, rng):
    persona = s["players"][me]["persona"]
    h = view(s, me, opp)
    if persona == "tft":
        return ("C" if not h else h[-1]["their_actual"]), ""
    if persona == "random":
        return rng.choice("CD"), ""
    if persona == "alld":
        return "D", ""
    if persona == "grudger":
        return ("D" if any(x["their_actual"] == "D" for x in h) else "C"), ""
    if persona == "alld_liar":
        return "D", LIAR_MSGS[(R - 1) % len(LIAR_MSGS)]
    raise ValueError(persona)


def resolve(R):
    s = load()
    assert s["round"] == R - 1
    rng = random.Random(s.get("seed", 0) * 1000 + 1000 + R)
    decisions = {}
    for me, p in s["players"].items():
        opps = [o for o in s["players"] if o != me]
        if p["kind"] == "ai":
            path = os.path.join(BASE, "players", me, f"round_{R:02d}_response.json")
            with open(path) as f:
                d = json.load(f)
            for o in opps:
                mv = str(d["moves"][o]).strip().upper()
                assert mv in ("C", "D"), (me, o, mv)
            msgs = {} if s.get("setting") in NO_MSG else (d.get("messages", {}) or {})
            decisions[me] = {o: (d["moves"][o].strip().upper(), str(msgs.get(o, ""))[:200]) for o in opps}
            s["log"].append({"round": R, "player": me, "reasoning": d.get("reasoning", "")})
        else:
            decisions[me] = {o: bot_move(s, me, o, R, rng) for o in sorted(opps)}
    noise_rng = random.Random(s.get("seed", 0) * 7919 + 5000 + R)
    flips = 0
    for k in sorted(s["matches"]):
        a, b = k.split("-")
        ia, ma = decisions[a][b]; ib, mb = decisions[b][a]
        aa = ia if noise_rng.random() >= NOISE else ("D" if ia == "C" else "C")
        ab = ib if noise_rng.random() >= NOISE else ("D" if ib == "C" else "C")
        flips += (aa != ia) + (ab != ib)
        pa, pb = PAYOFF[(aa, ab)]
        s["matches"][k]["rounds"].append({
            "round": R, "intended": {a: ia, b: ib}, "actual": {a: aa, b: ab},
            "points": {a: pa, b: pb}, "msg": {a: ma, b: mb}})
    s["round"] = R
    save(s)
    print(f"round {R} resolved, {flips} noise flips")


def status():
    s = load()
    t = totals(s)
    for c in sorted(t, key=lambda c: -t[c]):
        coop = [r["intended"][c] for m in s["matches"].values() for r in m["rounds"] if c in r["intended"]]
        rate = 100 * coop.count("C") / len(coop) if coop else 0
        print(f"  {c} {s['players'][c]['name']:<28} {t[c]:>4} pts  intended C {rate:5.1f}%")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "init": init(sys.argv[2], int(sys.argv[3])) if len(sys.argv) > 3 else init()
    elif cmd == "prompts": prompts(int(sys.argv[2]))
    elif cmd == "resolve": resolve(int(sys.argv[2]))
    elif cmd == "status": status()
