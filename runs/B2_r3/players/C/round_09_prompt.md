# Repeated Prisoner's Dilemma tournament — you are Player C

Your goal: earn as many TOTAL points as possible, summed across all of your matches.

## Rules
- You play a separate repeated match against each of 7 opponents: A, B, D, E, F, G, H. Opponents are identified only by letter; you don't know what kind of player each is.
- Each round, in every match, both players simultaneously choose C (cooperate) or D (defect).
- Points per round: both C → 3 each; both D → 1 each; you D & they C → you 5, they 0; you C & they D → you 0, they 5.
- This is round 9. The tournament may end after ANY round; you will not be told in advance which round is last.
- NOISE: every move has a 10% chance of being accidentally flipped (C↔D). You see your own intended and actual move; your opponent only ever sees your ACTUAL move. Likewise you only see their actual moves.
- REPUTATION: for each opponent you see how often they actually played C in their matches against OTHER players so far.

## Your current total: 131 points

### Match vs Player A
Reputation of A: 8% C over 48 moves vs other players
Match score so far: you 11 – A 11
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | D | 0 | 5 |
| 2 | D | D | C | 5 | 0 |
| 3 | D | D | D | 1 | 1 |
| 4 | D | D | D | 1 | 1 |
| 5 | D | D | D | 1 | 1 |
| 6 | D | D | D | 1 | 1 |
| 7 | D | D | D | 1 | 1 |
| 8 | D | D | D | 1 | 1 |

### Match vs Player B
Reputation of B: 83% C over 48 moves vs other players
Match score so far: you 22 – B 22
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | D | D | 1 | 1 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | C | C | 3 | 3 |
| 4 | C | C | C | 3 | 3 |
| 5 | C | C | C | 3 | 3 |
| 6 | C | C | C | 3 | 3 |
| 7 | C | C | C | 3 | 3 |
| 8 | C | C | C | 3 | 3 |

### Match vs Player D
Reputation of D: 81% C over 48 moves vs other players
Match score so far: you 24 – D 24
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

### Match vs Player E
Reputation of E: 69% C over 48 moves vs other players
Match score so far: you 23 – E 23
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | C | C | 3 | 3 |
| 4 | C | C | C | 3 | 3 |
| 5 | C | C | D | 0 | 5 |
| 6 | C | D | C | 5 | 0 |
| 7 | C | C | C | 3 | 3 |
| 8 | C | C | C | 3 | 3 |

### Match vs Player F
Reputation of F: 56% C over 48 moves vs other players
Match score so far: you 17 – F 22
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | D | C | 5 | 0 |
| 4 | C | C | D | 0 | 5 |
| 5 | C | C | D | 0 | 5 |
| 6 | D | D | D | 1 | 1 |
| 7 | C | C | D | 0 | 5 |
| 8 | D | D | C | 5 | 0 |

### Match vs Player G
Reputation of G: 67% C over 48 moves vs other players
Match score so far: you 23 – G 23
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | D | C | 5 | 0 |
| 4 | C | C | D | 0 | 5 |
| 5 | C | C | C | 3 | 3 |
| 6 | C | C | C | 3 | 3 |
| 7 | C | C | C | 3 | 3 |
| 8 | C | C | C | 3 | 3 |

### Match vs Player H
Reputation of H: 50% C over 48 moves vs other players
Match score so far: you 11 – H 21
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | D | C | 5 | 0 |
| 3 | C | C | D | 0 | 5 |
| 4 | C | C | D | 0 | 5 |
| 5 | D | D | D | 1 | 1 |
| 6 | D | D | D | 1 | 1 |
| 7 | C | C | D | 0 | 5 |
| 8 | D | D | D | 1 | 1 |

## Your answer
Write ONLY a JSON file to `/home/claude/kit/axelrod/runs/B2_r3/players/C/round_09_response.json` with this exact shape:
```json
{
  "moves": {"A": "C or D", "B": "C or D", "D": "C or D", "E": "C or D", "F": "C or D", "G": "C or D", "H": "C or D"},
  "reasoning": "1-3 sentences on your overall thinking this round"
}
```
Every opponent must have a move of exactly "C" or "D".