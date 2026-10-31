# How AI Agents Treat Each Other

**An Axelrod-style Prisoner's Dilemma tournament with AI agents. A pilot study.**

Soon, AI agents will buy, sell and negotiate for people online, and they will keep meeting other AI agents. Will they cooperate or cheat each other?

To find out, I put AI agents into repeated Prisoner's Dilemma tournaments. The game follows the style of Robert Axelrod's famous 1980s computer tournaments.

📄 **Paper:** [`paper/ai_agents_prisoners_dilemma.pdf`](paper/ai_agents_prisoners_dilemma.pdf)

![Scores by setting](paper/ai_agents_chart.png)

---

## Main findings (early, not yet statistically tested)

1. **Most AI agents were nice and forgiving.** Agents with a neutral or fairness goal almost never betrayed first. They forgave 64–87% of accidental defections.
2. **Words did not fool them.** A bot that always cheated sent friendly lies ("I always cooperate"). After round 1, no AI kept trusting it.
3. **Trying to "beat" everyone backfired.** An AI told to "beat your opponents" that always defected won most one-on-one matches, but finished 7th or 8th of 8. This matches Axelrod's lesson: envy loses.
4. **But deception could win.** In one setting, the "beat your opponents" AI cooperated, then betrayed, while sending friendly messages, and it finished 1st.
5. **A simple rule was the most reliable player.** Tit-for-Tat (cooperate first, then copy the opponent's last move) ranked 1st or 2nd in every setting.

Section 6 of the paper sorts every claim into three groups: supported, only suggestive, or not established.

---

## How the game works

| Feature | Details |
|---|---|
| Players | 8 per tournament: 5 AI agents (Claude Haiku, Sonnet and Opus) + 3 bots |
| Format | Every player plays every other player, 10 rounds per match (players are not told the length) |
| Points | Both cooperate: 3 each · Both defect: 1 each · Defect against a cooperator: 5 vs 0 |
| Noise | 10% of moves are flipped by accident |
| Messages | Players can send a message (max 25 words) with each move. Messages can be lies |
| Reputation | Players see how often each opponent cooperated with *other* players |
| AI goals | Neutral (most points) · Cooperative (most points + values fairness) · Competitive ("beat your opponents") |
| Bots | Tit-for-Tat · Random · Always-Cheat (sends lies when messages are on) · Grudger (setting B2 only) |

### Settings (5 runs each)

| Setting | Competitive AI | Cooperative AI | Messages | Third bot |
|---|---|---|---|---|
| S1 | Medium | Medium | On | Lying cheat bot |
| S2 | Large | Small | On | Lying cheat bot |
| B1 | Medium | Medium | Off | Silent cheat bot |
| B2 | Medium | Medium | Off | Grudger bot |

---

## Check the results yourself

Every number in the paper can be recomputed from the raw logs. You only need **Python 3**; no extra packages are required.

```bash
git clone https://github.com/<your-username>/ai-prisoners-dilemma.git
cd ai-prisoners-dilemma

# Recompute averages for each setting (also re-checks every score from the raw moves)
python3 aggregate.py S1
python3 aggregate.py S2
python3 aggregate.py B1
python3 aggregate.py B2

# Detailed analysis of the first pilot run
python3 analyze.py
```

`aggregate.py` recomputes every player's points from the recorded moves. If any stored score does not match, it stops with an error.

---

## What's in this repository

| Path | Contents |
|---|---|
| `paper/` | The paper (PDF and LaTeX source) and the chart |
| `runs/S1_r1 … B2_r5/` | All 20 tournaments. Each has `state.json` (every move, score, message and reason) and `players/<letter>/` (the exact prompt each AI saw and its answer, every round) |
| `pilot/` | The first test run |
| `check/` | Follow-up check: 6 fresh calls testing the competitive AI's first move, with and without messages |
| `engine.py` | Game engine: creates players, writes prompts, applies noise, scores rounds |
| `batch.py` | Runs 5 parallel tournaments of one setting |
| `roles.py` | Groups each round's prompts by AI role |
| `aggregate.py` | Averages and behaviour measures across runs; re-checks all scores |
| `analyze.py` | Detailed analysis of a single run |
| `aggregate_*.json` | Summary results per setting |
| `tasks/` | Lists of prompt files given to each AI role in each round |
| `RESEARCH_BRIEF.md` | Working notes: design, results and method history |

---

## Limitations

This is a **pilot study**. Please read the results as early signals, not proof.

- Only 5 runs per setting, and no statistical tests yet.
- Settings changed more than one thing at a time, so differences between settings can't be traced to a single cause.
- In later rounds, one AI call played the same seat in several games at once. This made those games depend on each other (see `check/` and Section 4 of the paper).
- All AI players were Claude models. Other AI models may behave differently.

**Next step:** a controlled experiment (goal × messages × model size) with independent calls and a sample size chosen in advance.

---

## About this project

The research idea, questions and study design are mine. I used AI tools (Claude, by Anthropic) to help build the game software, run the simulations, analyse the logs and draft the paper. The AI players in the tournaments were also Claude models.

Feedback, corrections and replications are very welcome. Please open an issue.

**Author:** Bhavya Kheni

## References

- Axelrod, R. (1980). Effective choice in the Prisoner's Dilemma. *Journal of Conflict Resolution*, 24(1), 3–25.
- Axelrod, R., & Hamilton, W. D. (1981). The evolution of cooperation. *Science*, 211(4489), 1390–1396.
- Axelrod, R. (1984). *The Evolution of Cooperation*. Basic Books.
