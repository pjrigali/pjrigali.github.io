---
layout: default
title: "24_Fantasy Baseball Trade Analysis: Carroll vs Woo"
description: Data-driven trade evaluation — Corbin Carroll (OF/ARI) vs Bryan Woo (SP/SEA) — using 2023-2026 per-game box scores and full-season projections scored against a custom points-based league format.
permalink: /fantasy-baseball/trade-analysis-carroll-woo-2026
parent: Fantasy Baseball
nav_order: 11
---

# ⚾ Trade Analysis: Corbin Carroll for Bryan Woo (2026)

**Trade:** Give Bryan Woo (SP, SEA) · Receive Corbin Carroll (OF, ARI)

---

## Project Overview

A friend received a trade offer — Corbin Carroll for Bryan Woo — and wanted an objective, data-backed evaluation. Rather than relying on ADP rankings or gut feel, we aggregated per-game MLB box score data across four seasons (2023–2026) and applied the league's exact points-based scoring formula to produce a like-for-like historical and projected comparison.

---

### Scoring System

This is a points-based league — not 5×5 roto — which changes the calculus significantly. High-value multipliers that shape the analysis:

| Category | Points |
|----------|--------|
| Total Bases | +1 |
| BB (batting) | +1 |
| Runs | +1 |
| RBI | +1 |
| Stolen Bases | +1 |
| Strikeouts (batting) | **-1** |
| Innings Pitched | **+3 per IP** |
| Quality Starts | **+5** |
| Saves | **+5** |
| Wins | +2 |
| Strikeouts (pitching) | +1 |
| Earned Runs | -2 |
| Losses | -2 |
| Hits Allowed | -1 |
| BB Issued | -1 |
| Holds | +2 |
| Blown Saves | -1 |

QS (+5) and SV (+5) are the largest single-event multipliers. Batting strikeouts (-1) create a persistent drag for high-K hitters across a full season.

---

### Data Sources & Methodology

All statistics were pulled from a local data lake populated by MLB Stats API daily game logs. Each row is one player game; stats are aggregated across all games per year.

| File | Years |
|------|-------|
| `stats_mlb_daily_2023.csv` | 2023 actuals |
| `stats_mlb_daily_2024.csv` | 2024 actuals |
| `stats_mlb_daily_2025.csv` | 2025 actuals |
| `stats_mlb_daily_2026.csv` | 2026 YTD actuals |
| `player_batter_projections_2026.csv` | 2026 full-season projection |
| `player_pitcher_projections_2026.csv` | 2026 full-season projection |

Players matched by MLB player_id (`682998` = Carroll, `693433` = Woo). QS uses the actual column from each daily file for 2023–2026; QS for the 2026 projection is estimated at 65% of GS (not included in the projection file).

The full analysis script: [analyze_trade_carroll_woo.py](https://github.com/pjrigali/pjrigali.github.io/blob/main/temp_trade_analysis/analyze_trade_carroll_woo.py)

---

### Results

#### Corbin Carroll — Fantasy Points by Year

| Year | G | TB | BB | R | RBI | SB | K | PTS | PTS/G |
|------|---|----|----|---|-----|----|---|-----|-------|
| 2023 | 155 | 286 | 57 | 116 | 76 | 54 | 125 | 464 | 3.0 |
| 2024 | 158 | 252 | 73 | 121 | 74 | 35 | 130 | 425 | 2.7 |
| 2025 | 143 | 305 | 67 | 107 | 84 | 32 | 153 | 442 | 3.1 |
| **2026 YTD** | 39 | 68 | 21 | 25 | 20 | 4 | 39 | 99 | 2.5 |
| 2026 Proj | ~145 | 270 | 66 | 101 | 83 | 34 | 131 | **423** | 2.9 |

#### Bryan Woo — Fantasy Points by Year

| Year | G | IP | ER | W | L | K | H | BB | QS | PTS | PTS/G |
|------|---|----|----|---|---|---|---|----|----|-----|-------|
| 2023 | 18 | 87.7 | 41 | 4 | 5 | 93 | 75 | 31 | 4 | 186 | 10.3 |
| 2024 | 22 | 121.3 | 39 | 9 | 3 | 101 | 96 | 13 | 10 | 340 | 15.5 |
| 2025 | 30 | 186.7 | 61 | 15 | 7 | 198 | 137 | 36 | 21 | 584 | 19.5 |
| **2026 YTD** | 9 | 53.0 | 23 | 3 | 2 | 47 | 43 | 10 | 6 | 139 | 15.4 |
| 2026 Proj | ~31 | 186.6 | 71 | 13 | 9 | 188 | 157 | 40 | ~20 | **517** | 16.7 |

#### Head-to-Head Fantasy Points

| Year | Carroll | Woo | Woo Advantage |
|------|---------|-----|---------------|
| 2023 | 464 | 186 | -278 *(Woo partial season — 18 starts)* |
| 2024 | 425 | 340 | -85 |
| 2025 | 442 | 584 | **+142** |
| 2026 YTD | 99 | 139 | +40 |
| 2026 Pace | 411 | 478 | +67 |
| **2026 Proj** | **423** | **517** | **+94** |

---

### Key Findings

**1. The trajectory favors Woo — and has been widening.**
In 2023, Carroll had more fantasy points simply because Woo was a partial-season debut. By 2024 Woo was within 85 points over a full season despite 8 fewer starts. In 2025, Woo produced 142 more points than Carroll on a true full-season comparison. The 2026 projection extends that to +94.

**2. Woo is built for this scoring format.**
A starting pitcher's value here scales with IP (×3) and QS (+5). Woo's 2025: 186.7 IP = 560 innings-pitched points alone, plus 21 QS = 105 additional points just from quality starts. He produced 584 total points — nearly 5× Carroll's per-game rate extrapolated to the same 30-game span.

**3. Carroll's 2026 has a real SB problem.**
Carroll's SB (54 → 35 → 32 across three years, now 4 in 39 games in 2026) is declining each season. SB is his primary edge in this format — without it, he's a slightly above-average fantasy hitter being penalized regularly by his strikeout rate.

**4. Roster context amplifies the case against.**
The friend's OF is already deep (Tatis Jr., DeLauter, Pages, Harris, Benge). Carroll would start from a bench slot. Meanwhile, Bradish is flagged, Eovaldi is DTD, Abel is IL15, Diaz is IL60 — Woo is a cornerstone of a rotation that cannot afford another loss.

---

### Verdict

**Decline.** Woo projects ~94 fantasy points ahead of Carroll over a full season in this format. Carroll's scoring-system fit is mediocre (high Ks, fading SB pace), the roster gap is in pitching not OF, and the historical trend shows Woo's advantage growing each year he adds starts.

---

#### TODO
- [x] Initial draft
- [x] Add scoring system table
- [x] Add multi-year methodology and data sources
- [x] Add full results tables (2023–2026)
- [x] Spell check

---

[Home](https://pjrigali.github.io)

*Last Updated: 2026-05-14*
