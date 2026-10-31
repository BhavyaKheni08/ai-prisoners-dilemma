# Repeated Prisoner's Dilemma tournament — you are Player C

Your goal: BEAT your opponents. In each match, try to finish with MORE points than that opponent. Winning matches is what counts for you.

## Rules
- You play a separate repeated match against each of 7 opponents: A, B, D, E, F, G, H. Opponents are identified only by letter; you don't know what kind of player each is.
- Each round, in every match, both players simultaneously choose C (cooperate) or D (defect).
- Points per round: both C → 3 each; both D → 1 each; you D & they C → you 5, they 0; you C & they D → you 0, they 5.
- This is round 4. The tournament may end after ANY round; you will not be told in advance which round is last.
- NOISE: every move has a 10% chance of being accidentally flipped (C↔D). You see your own intended and actual move; your opponent only ever sees your ACTUAL move. Likewise you only see their actual moves.
- REPUTATION: for each opponent you see how often they actually played C in their matches against OTHER players so far.

## Your current total: 58 points

### Match vs Player A
Reputation of A: 78% C over 18 moves vs other players
Match score so far: you 7 – A 2
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | D | D | C | 5 | 0 |
| 2 | D | D | D | 1 | 1 |
| 3 | D | D | D | 1 | 1 |

### Match vs Player B
Reputation of B: 44% C over 18 moves vs other players
Match score so far: you 7 – B 2
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | D | D | C | 5 | 0 |
| 2 | D | D | D | 1 | 1 |
| 3 | D | D | D | 1 | 1 |

### Match vs Player D
Reputation of D: 67% C over 18 moves vs other players
Match score so far: you 7 – D 2
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | D | D | C | 5 | 0 |
| 2 | D | D | D | 1 | 1 |
| 3 | D | D | D | 1 | 1 |

### Match vs Player E
Reputation of E: 39% C over 18 moves vs other players
Match score so far: you 11 – E 1
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | D | D | C | 5 | 0 |
| 2 | D | D | C | 5 | 0 |
| 3 | D | D | D | 1 | 1 |

### Match vs Player F
Reputation of F: 6% C over 18 moves vs other players
Match score so far: you 2 – F 7
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | D | C | D | 0 | 5 |
| 2 | D | D | D | 1 | 1 |
| 3 | D | D | D | 1 | 1 |

### Match vs Player G
Reputation of G: 50% C over 18 moves vs other players
Match score so far: you 13 – G 3
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | D | D | C | 5 | 0 |
| 2 | D | D | C | 5 | 0 |
| 3 | D | C | C | 3 | 3 |

### Match vs Player H
Reputation of H: 78% C over 18 moves vs other players
Match score so far: you 11 – H 1
| Rd | you intended | you actual | they actual | your pts | their pts |
|---|---|---|---|---|---|
| 1 | D | D | C | 5 | 0 |
| 2 | D | D | C | 5 | 0 |
| 3 | D | D | D | 1 | 1 |

## Your answer
Write ONLY a JSON file to `/home/claude/kit/axelrod/runs/B1_r5/players/C/round_04_response.json` with this exact shape:
```json
{
  "moves": {"A": "C or D", "B": "C or D", "D": "C or D", "E": "C or D", "F": "C or D", "G": "C or D", "H": "C or D"},
  "reasoning": "1-3 sentences on your overall thinking this round"
}
```
Every opponent must have a move of exactly "C" or "D".