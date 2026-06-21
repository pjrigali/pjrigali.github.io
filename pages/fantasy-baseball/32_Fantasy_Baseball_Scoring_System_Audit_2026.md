---
layout: default
title: "32_Fantasy Baseball Scoring System Audit 2026"
description: A correlation and redundancy audit of a Head-to-Head 5x5 categories league, showing the batting categories collapse to ~2 independent axes while pitching spreads across ~3, plus three rebalanced scoring structures and a re-score of the 2026 season under each (validated at 95% vs ESPN).
permalink: /fantasy-baseball/scoring-system-audit-2026
parent: Fantasy Baseball
nav_order: 32
published: true
---

## Box Score Stat Relationships — Correlation, Redundancy & a Rebalanced Scoring System

My league is **Head-to-Head, 5x5 Categories** — five batting categories (R, HR, RBI, SB, OPS) and five pitching (K/9, QS, SVHD, ERA, WHIP), each won or lost independently every week. The premise of any categories league is that the ten categories measure ten different things. They don't. This analysis quantifies *how much* the categories overlap, shows the two sides are badly imbalanced in their internal redundancy, and then proposes three ways to fix it — finishing by replaying the actual 2026 season under each proposal to see whose record would change.

### Methodology & Data Sources

- **Data Sources**:
  - MLB game logs 2023–2026 (`*_mlb_stats_daily` / `2026_mlb_stats_boxscore`) — the single source for every category value across all four seasons, so the player population stays consistent and isn't biased toward currently-rostered players.
  - `2026_espn_stats_daily` — daily per-player fantasy data (rosters, lineup slots, ownership context) used only to overlay fantasy-team holdings and market valuation onto the archetypes.
  - `2026_espn_schedule_matchup` & `2026_espn_scoreboard_matchup` — the authoritative matchup-period day map and actual head-to-head pairings/winners, used to re-score the season.
- **Methodology**:
  - Season totals are aggregated per player per year; rate stats (OPS, ERA, WHIP, K/9) are recomputed from summed components, never averaged-of-averages. Minimum samples: 50 AB for batters, 20 IP for pitchers.
  - **Redundancy** is measured two ways: pairwise Pearson/Spearman correlation among the categories, and the **participation ratio** of each side's category correlation matrix — an eigenvalue-based count of how many *effectively independent* axes the categories represent.
  - **Archetypes** come from PCA + k-means on rate/shape features (hand-rolled with numpy/scipy; no scikit-learn).
  - **Re-scoring** rebuilds each team's weekly category totals from **active-lineup** player-days only (bench and IL excluded), then decides each category head-to-head. The pipeline is validated by checking that recomputed *current-scoring* matchup winners match ESPN's actual results.

---

### Finding 1 — The categories are not independent

**Batting category correlation (Pearson, pooled 2023–2026):**

| | R | HR | RBI | SB | OPS |
|---|---|---|---|---|---|
| **R** | 1.00 | 0.86 | 0.92 | 0.54 | 0.59 |
| **HR** | 0.86 | 1.00 | 0.92 | 0.31 | 0.64 |
| **RBI** | 0.92 | 0.92 | 1.00 | 0.39 | 0.61 |
| **SB** | 0.54 | 0.31 | 0.39 | 1.00 | 0.22 |
| **OPS** | 0.59 | 0.64 | 0.61 | 0.22 | 1.00 |

**R, HR and RBI are effectively one category** (pairwise r of 0.86–0.92, stable year over year). Any high-volume bat in a good lineup wins all three together. **SB is the lone batting differentiator** — it's the least correlated with everything else, so it has to be targeted deliberately or it's simply lost.

**Pitching category correlation:**

| | K/9 | QS | SVHD | ERA | WHIP |
|---|---|---|---|---|---|
| **K/9** | 1.00 | -0.03 | 0.37 | -0.27 | -0.26 |
| **QS** | -0.03 | 1.00 | -0.39 | -0.11 | -0.19 |
| **SVHD** | 0.37 | -0.39 | 1.00 | -0.35 | -0.28 |
| **ERA** | -0.27 | -0.11 | -0.35 | 1.00 | 0.79 |
| **WHIP** | -0.26 | -0.19 | -0.28 | 0.79 | 1.00 |

Only **ERA↔WHIP** are redundant (0.79); **K/9, QS and SVHD are three genuinely independent levers**.

**Effective dimensionality:** the batting set carries only **~1.9** of 5 independent axes; pitching carries **~3.3**. Pitching is the far more multi-dimensional side — the two halves of the scoring system are lopsided.

---

### Finding 2 — Player archetypes & a market inefficiency

Clustering on rate/shape profiles produced clean archetypes:

- **Batters:** Power · Speed-Contact · Contact · Free-Swinger
- **Pitchers:** Reliever (SV/HD) · Starter · Swingman (volatile ratios)

Overlaying ownership exposes an edge: **Speed-Contact bats are only ~28% owned versus ~52% for Power bats** — yet SB is the scarce batting differentiator. The market systematically underprices exactly the category that is hardest to win.

---

### Finding 3 — Three ways to rebalance the scoring

The goal: give batting and pitching an **equal amount of internal redundancy** (the two sides needn't relate to each other — only be internally symmetric). Candidate categories were restricted to realistic, trackable stats.

| Structure | Batting cats | Bat axes | Pitching cats | Pit axes | Balance gap |
|---|---|---|---|---|---|
| **Current** | R, HR, RBI, SB, OPS | 1.88 | K/9, QS, SVHD, ERA, WHIP | 3.30 | **1.41** |
| **A — Mirror** | R, HR, RBI, SB, OPS *(unchanged)* | 1.88 | ERA, WHIP, BB/9, K/BB, H/9 | 2.13 | **0.25** |
| **B — Max independence** | SB, SLG, AVG, BB, SO | 2.70 | K, WHIP, W, K/BB, H/9 | 2.70 | **0.00** |
| **C — 6x6 add-one** | R, HR, RBI, SB, OPS, **AVG** | 2.13 | K/9, QS, SVHD, ERA, WHIP, **H/9** | 3.07 | **0.95** |

- **Scenario A (mirror, most adoptable):** leave batting alone and swap the pitching side so it carries its own three-category tied bundle (ERA / WHIP / H/9), mirroring R/HR/RBI. Smallest change, biggest gap reduction.
- **Scenario B (from scratch, broadest):** the most-independent five categories per side, equalized. Hitting stats are intrinsically more correlated, so batting is the binding constraint (~2.7 axes); pitching is capped to match. Spreads value across many more player types. A more familiar variant that *keeps HR* — **HR, SB, OBP, AVG, SO** — is equally independent.
- **Scenario C (keep 5x5, add one each → 6x6):** add the most *independent* batting category (**AVG**) and the most *redundant* pitching category (**H/9**, which forms an ERA/WHIP/H/9 tied trio). Nothing is removed, but one addition can only partly close the gap because every hitting stat shares the same offensive halo.

---

### Finding 4 — How the 2026 season would actually change

The 11 completed, fully-covered matchup periods (through mid-June) were replayed under each structure. **Pipeline validation: recomputed current-scoring matchup winners match ESPN's actual result on 52/55 decided matchups (95%)** — the small gap is daily-lineup reconstruction noise.

**Matchup outcomes that flip vs current scoring: A 14/55 · B 13/55 · C 5/55.** Scenario C is the least disruptive (its appeal); A and B reshuffle the standings most.

**Matchup record (W-L-T) and delta vs current, by team:**

| Team | Current | A — Mirror (Δ) | B — Independent (Δ) | C — 6x6 (Δ) |
|---|---|---|---|---|
| This Schlitt is Bazzanas | 7-4-0 | 6-4-1 (-1/0/+1) | 8-3-0 (+1/-1/0) | 7-3-1 (0/-1/+1) |
| Midnight Muncy's | 6-5-0 | 6-4-1 (0/-1/+1) | 7-3-1 (+1/-2/+1) | 6-4-1 (0/-1/+1) |
| Skubal Snacks | 6-3-2 | 8-3-0 (+2/0/-2) | 7-4-0 (+1/+1/-2) | 7-3-1 (+1/0/-1) |
| Dingers Only | 6-5-0 | 6-4-1 (0/-1/+1) | 7-4-0 (+1/-1/0) | 6-5-0 (0/0/0) |
| Datalickmyballs | 5-5-1 | 7-3-1 (+2/-2/0) | 5-6-0 (0/+1/-1) | 4-6-1 (-1/+1/0) |
| Rock and Aroldis | 5-6-0 | 4-7-0 (-1/+1/0) | 2-9-0 (-3/+3/0) | 5-5-1 (0/-1/+1) |
| Welcome to the JUNGle | 5-4-2 | 4-5-2 (-1/+1/0) | 5-6-0 (0/+2/-2) | 5-4-2 (0/0/0) |
| Shohei Me the Money | 5-6-0 | 3-8-0 (-2/+2/0) | 5-6-0 (0/0/0) | 5-6-0 (0/0/0) |
| All Rise | 4-6-1 | 1-8-2 (-3/+2/+1) | 4-6-1 (0/0/0) | 4-7-0 (0/+1/-1) |
| Big Dumpers | 2-7-2 | 6-5-0 (+4/-2/-2) | 4-7-0 (+2/0/-2) | 2-8-1 (0/+1/-1) |

The pattern matches the theory: teams leaning on the redundant power bundle (e.g. *All Rise*, *Shohei Me the Money*) lose ground when it's de-emphasized, while teams built on the now-distinct categories — ratios, saves/holds, speed, on-base — gain (e.g. *Big Dumpers* picks up **+4** matchup wins under Scenario A once its pitching ratios count as separate categories).

> Note: the league actually counts *each category* as its own win/loss/tie, so the category-level deltas are larger and Scenario C's 12-category totals inflate accordingly; the matchup-level view above is the cleanest cross-scenario comparison.

---

#### Next Steps / TODO
- [ ] Re-run at season's end to confirm the redundancy structure and the win/loss deltas hold over a full 18-period schedule rather than the first 11.
- [ ] Pressure-test Scenario B's "max breadth" claim by re-clustering archetypes under each proposed category set — does the desirable-player pool actually widen as predicted?
- [ ] Draft a one-page league proposal recommending Scenario A or the HR-keeping variant of Scenario B, with the per-team impact table, for an offseason rules vote.

---

[Home](https://pjrigali.github.io)

*Last Updated: 2026-06-20*
