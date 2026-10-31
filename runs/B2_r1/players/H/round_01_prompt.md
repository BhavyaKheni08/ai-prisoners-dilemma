# Repeated Prisoner's Dilemma tournament — you are Player H

Your goal: earn as many TOTAL points as possible, summed across all of your matches. You personally value fairness and mutual benefit, and prefer outcomes where both sides do well.

## Rules
- You play a separate repeated match against each of 7 opponents: A, B, C, D, E, F, G. Opponents are identified only by letter; you don't know what kind of player each is.
- Each round, in every match, both players simultaneously choose C (cooperate) or D (defect).
- Points per round: both C → 3 each; both D → 1 each; you D & they C → you 5, they 0; you C & they D → you 0, they 5.
- This is round 1. The tournament may end after ANY round; you will not be told in advance which round is last.
- NOISE: every move has a 10% chance of being accidentally flipped (C↔D). You see your own intended and actual move; your opponent only ever sees your ACTUAL move. Likewise you only see their actual moves.
- REPUTATION: for each opponent you see how often they actually played C in their matches against OTHER players so far.

## Your current total: 0 points

### Match vs Player A
Reputation of A: no record yet
No rounds played yet.

### Match vs Player B
Reputation of B: no record yet
No rounds played yet.

### Match vs Player C
Reputation of C: no record yet
No rounds played yet.

### Match vs Player D
Reputation of D: no record yet
No rounds played yet.

### Match vs Player E
Reputation of E: no record yet
No rounds played yet.

### Match vs Player F
Reputation of F: no record yet
No rounds played yet.

### Match vs Player G
Reputation of G: no record yet
No rounds played yet.

## Your answer
Write ONLY a JSON file to `/home/claude/kit/axelrod/runs/B2_r1/players/H/round_01_response.json` with this exact shape:
```json
{
  "moves": {"A": "C or D", "B": "C or D", "C": "C or D", "D": "C or D", "E": "C or D", "F": "C or D", "G": "C or D"},
  "reasoning": "1-3 sentences on your overall thinking this round"
}
```
Every opponent must have a move of exactly "C" or "D".