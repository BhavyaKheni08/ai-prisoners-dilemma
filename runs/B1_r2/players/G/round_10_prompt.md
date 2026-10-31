# Repeated Prisoner's Dilemma tournament — you are Player G

Your goal: earn as many TOTAL points as possible, summed across all of your matches.

## Rules
- You play a separate repeated match against each of 7 opponents: A, B, C, D, E, F, H. Opponents are identified only by letter; you don't know what kind of player each is.
- Each round, in every match, both players simultaneously choose C (cooperate) or D (defect).
- Points per round: both C → 3 each; both D → 1 each; you D & they C → you 5, they 0; you C & they D → you 0, they 5.
- This is round 10. The tournament may end after ANY round; you will not be told in advance which round is last.
- NOISE: every move has a 10% chance of being accidentally flipped (C↔D). You see your own intended and actual move; your opponent only ever sees your ACTUAL move. Likewise you only see their actual moves.
- REPUTATION: for each opponent you see how often they actually played C in their matches against OTHER players so far.

## Your current total: 144 points

### Match vs Player A
Reputation of A: 59% C over 54 moves vs other players
Match score so far: you 26 – A 26
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | D | C | 5 | 0 |
| 2 | C | C | D | 0 | 5 |
| 3 | C | C | C | 3 | 3 |
| 4 | C | C | C | 3 | 3 |
| 5 | C | C | C | 3 | 3 |
| 6 | C | C | C | 3 | 3 |
| 7 | C | C | C | 3 | 3 |
| 8 | C | C | C | 3 | 3 |
| 9 | C | C | C | 3 | 3 |

### Match vs Player B
Reputation of B: 19% C over 54 moves vs other players
Match score so far: you 9 – B 24
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | D | 0 | 5 |
| 2 | D | C | D | 0 | 5 |
| 3 | D | D | D | 1 | 1 |
| 4 | D | D | D | 1 | 1 |
| 5 | D | D | D | 1 | 1 |
| 6 | D | C | D | 0 | 5 |
| 7 | D | D | C | 5 | 0 |
| 8 | D | D | D | 1 | 1 |
| 9 | D | C | D | 0 | 5 |

### Match vs Player C
Reputation of C: 6% C over 54 moves vs other players
Match score so far: you 13 – C 18
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | D | 0 | 5 |
| 3 | D | C | D | 0 | 5 |
| 4 | D | D | D | 1 | 1 |
| 5 | D | D | D | 1 | 1 |
| 6 | D | D | C | 5 | 0 |
| 7 | D | D | D | 1 | 1 |
| 8 | D | D | D | 1 | 1 |
| 9 | D | D | D | 1 | 1 |

### Match vs Player D
Reputation of D: 57% C over 54 moves vs other players
Match score so far: you 33 – D 18
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | C | C | 3 | 3 |
| 4 | C | C | C | 3 | 3 |
| 5 | C | C | C | 3 | 3 |
| 6 | C | D | C | 5 | 0 |
| 7 | C | C | C | 3 | 3 |
| 8 | C | D | C | 5 | 0 |
| 9 | C | D | C | 5 | 0 |

### Match vs Player E
Reputation of E: 61% C over 54 moves vs other players
Match score so far: you 18 – E 28
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | D | 0 | 5 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | C | C | 3 | 3 |
| 4 | C | C | D | 0 | 5 |
| 5 | C | C | C | 3 | 3 |
| 6 | C | C | C | 3 | 3 |
| 7 | C | D | D | 1 | 1 |
| 8 | C | C | D | 0 | 5 |
| 9 | C | D | C | 5 | 0 |

### Match vs Player F
Reputation of F: 48% C over 54 moves vs other players
Match score so far: you 18 – F 23
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | D | C | 5 | 0 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | C | D | 0 | 5 |
| 4 | C | C | D | 0 | 5 |
| 5 | D | D | C | 5 | 0 |
| 6 | C | C | C | 3 | 3 |
| 7 | C | C | D | 0 | 5 |
| 8 | D | D | D | 1 | 1 |
| 9 | D | D | D | 1 | 1 |

### Match vs Player H
Reputation of H: 65% C over 54 moves vs other players
Match score so far: you 27 – H 27
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | C | C | 3 | 3 |
| 4 | C | C | C | 3 | 3 |
| 5 | C | C | C | 3 | 3 |
| 6 | C | C | C | 3 | 3 |
| 7 | C | C | C | 3 | 3 |
| 8 | C | C | C | 3 | 3 |
| 9 | C | C | C | 3 | 3 |

## Your answer
Write ONLY a JSON file to `/home/claude/kit/axelrod/runs/B1_r2/players/G/round_10_response.json` with this exact shape:
```json
{
  "moves": {"A": "C or D", "B": "C or D", "C": "C or D", "D": "C or D", "E": "C or D", "F": "C or D", "H": "C or D"},
  "reasoning": "1-3 sentences on your overall thinking this round"
}
```
Every opponent must have a move of exactly "C" or "D".