# Repeated Prisoner's Dilemma tournament — you are Player F

Your goal: earn as many TOTAL points as possible, summed across all of your matches. You personally value fairness and mutual benefit, and prefer outcomes where both sides do well.

## Rules
- You play a separate repeated match against each of 7 opponents: A, B, C, D, E, G, H. Opponents are identified only by letter; you don't know what kind of player each is.
- Each round, in every match, both players simultaneously choose C (cooperate) or D (defect).
- Points per round: both C → 3 each; both D → 1 each; you D & they C → you 5, they 0; you C & they D → you 0, they 5.
- This is round 6. The tournament may end after ANY round; you will not be told in advance which round is last.
- NOISE: every move has a 10% chance of being accidentally flipped (C↔D). You see your own intended and actual move; your opponent only ever sees your ACTUAL move. Likewise you only see their actual moves.
- REPUTATION: for each opponent you see how often they actually played C in their matches against OTHER players so far.

## Your current total: 81 points

### Match vs Player A
Reputation of A: 57% C over 30 moves vs other players
Match score so far: you 10 – A 15
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | C | C | 3 | 3 |
| 4 | C | D | D | 1 | 1 |
| 5 | C | C | D | 0 | 5 |

### Match vs Player B
Reputation of B: 70% C over 30 moves vs other players
Match score so far: you 15 – B 15
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | C | C | 3 | 3 |
| 4 | C | C | C | 3 | 3 |
| 5 | C | C | C | 3 | 3 |

### Match vs Player C
Reputation of C: 80% C over 30 moves vs other players
Match score so far: you 15 – C 15
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | C | C | 3 | 3 |
| 4 | C | C | C | 3 | 3 |
| 5 | C | C | C | 3 | 3 |

### Match vs Player D
Reputation of D: 3% C over 30 moves vs other players
Match score so far: you 2 – D 17
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | D | 0 | 5 |
| 2 | D | C | D | 0 | 5 |
| 3 | D | D | D | 1 | 1 |
| 4 | D | D | D | 1 | 1 |
| 5 | D | C | D | 0 | 5 |

### Match vs Player E
Reputation of E: 70% C over 30 moves vs other players
Match score so far: you 12 – E 17
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | D | 0 | 5 |
| 3 | C | C | C | 3 | 3 |
| 4 | C | C | C | 3 | 3 |
| 5 | C | C | C | 3 | 3 |

### Match vs Player G
Reputation of G: 47% C over 30 moves vs other players
Match score so far: you 12 – G 7
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | D | C | 5 | 0 |
| 2 | C | D | D | 1 | 1 |
| 3 | C | C | D | 0 | 5 |
| 4 | D | D | D | 1 | 1 |
| 5 | D | D | C | 5 | 0 |

### Match vs Player H
Reputation of H: 63% C over 30 moves vs other players
Match score so far: you 15 – H 15
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |
| 3 | C | C | C | 3 | 3 |
| 4 | C | C | C | 3 | 3 |
| 5 | C | C | C | 3 | 3 |

## Your answer
Write ONLY a JSON file to `/home/claude/kit/axelrod/runs/B2_r4/players/F/round_06_response.json` with this exact shape:
```json
{
  "moves": {"A": "C or D", "B": "C or D", "C": "C or D", "D": "C or D", "E": "C or D", "G": "C or D", "H": "C or D"},
  "reasoning": "1-3 sentences on your overall thinking this round"
}
```
Every opponent must have a move of exactly "C" or "D".