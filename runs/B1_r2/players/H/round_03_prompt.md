# Repeated Prisoner's Dilemma tournament — you are Player H

Your goal: earn as many TOTAL points as possible, summed across all of your matches. You personally value fairness and mutual benefit, and prefer outcomes where both sides do well.

## Rules
- You play a separate repeated match against each of 7 opponents: A, B, C, D, E, F, G. Opponents are identified only by letter; you don't know what kind of player each is.
- Each round, in every match, both players simultaneously choose C (cooperate) or D (defect).
- Points per round: both C → 3 each; both D → 1 each; you D & they C → you 5, they 0; you C & they D → you 0, they 5.
- This is round 3. The tournament may end after ANY round; you will not be told in advance which round is last.
- NOISE: every move has a 10% chance of being accidentally flipped (C↔D). You see your own intended and actual move; your opponent only ever sees your ACTUAL move. Likewise you only see their actual moves.
- REPUTATION: for each opponent you see how often they actually played C in their matches against OTHER players so far.

## Your current total: 29 points

### Match vs Player A
Reputation of A: 75% C over 12 moves vs other players
Match score so far: you 6 – A 6
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |

### Match vs Player B
Reputation of B: 25% C over 12 moves vs other players
Match score so far: you 2 – B 2
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | D | D | 1 | 1 |
| 2 | D | D | D | 1 | 1 |

### Match vs Player C
Reputation of C: 17% C over 12 moves vs other players
Match score so far: you 1 – C 6
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | D | 0 | 5 |
| 2 | D | D | D | 1 | 1 |

### Match vs Player D
Reputation of D: 58% C over 12 moves vs other players
Match score so far: you 6 – D 6
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |

### Match vs Player E
Reputation of E: 58% C over 12 moves vs other players
Match score so far: you 3 – E 8
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | D | 0 | 5 |
| 2 | C | C | C | 3 | 3 |

### Match vs Player F
Reputation of F: 50% C over 12 moves vs other players
Match score so far: you 5 – F 5
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | D | 0 | 5 |
| 2 | D | D | C | 5 | 0 |

### Match vs Player G
Reputation of G: 83% C over 12 moves vs other players
Match score so far: you 6 – G 6
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | C | C | C | 3 | 3 |
| 2 | C | C | C | 3 | 3 |

## Your answer
Write ONLY a JSON file to `/home/claude/kit/axelrod/runs/B1_r2/players/H/round_03_response.json` with this exact shape:
```json
{
  "moves": {"A": "C or D", "B": "C or D", "C": "C or D", "D": "C or D", "E": "C or D", "F": "C or D", "G": "C or D"},
  "reasoning": "1-3 sentences on your overall thinking this round"
}
```
Every opponent must have a move of exactly "C" or "D".