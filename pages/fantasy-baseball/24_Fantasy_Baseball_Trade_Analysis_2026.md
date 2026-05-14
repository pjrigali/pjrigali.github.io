---
layout: default
title: "24_Fantasy Baseball Trade Analysis: Carroll vs Woo"
description: Data-driven trade evaluation — Corbin Carroll (OF/ARI) vs Bryan Woo (SP/SEA) — using 2025 actuals, 2026 YTD, and full-season projections scored against a custom points-based league format.
permalink: /fantasy-baseball/trade-analysis-carroll-woo-2026
parent: Fantasy Baseball
nav_order: 11
---

# ⚾ Trade Analysis: Corbin Carroll for Bryan Woo (2026)

**Trade:** Give Bryan Woo (SP, SEA) · Receive Corbin Carroll (OF, ARI)

---

## Project Overview

A friend received a trade offer — Corbin Carroll for Bryan Woo — and wanted an objective, data-backed evaluation. Rather than relying on ADP rankings or gut feel, we pulled 2025 full-season actuals, 2026 YTD game logs, and full-season projections, then scored every player directly against the league's custom points format to produce a like-for-like comparison.

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

QS (+5) and SV (+5) are disproportionately valuable. Batting strikeouts (-1) punish high-K hitters meaningfully over a full season.

---

### Data Sources & Methodology

All player statistics were pulled from a local data lake populated by MLB Stats API and ESPN API feeds.

| File | Used For |
|------|----------|
| `mlb_hitting_2025_20260215.csv` | Carroll 2025 season batting totals |
| `mlb_pitching_2025_20260215.csv` | Woo 2025 season pitching totals |
| `stats_mlb_daily_2026.csv` | 2026 YTD game logs (aggregated by player) |
| `player_batter_projections_2026.csv` | Carroll 2026 full-season projection |
| `player_pitcher_projections_2026.csv` | Woo 2026 full-season projection |

Fantasy points were calculated by applying the exact league scoring weights to raw box score stats — no approximations for batting (TB, BB, R, RBI, SB, K). For pitching, Quality Starts in the 2025 file were estimated at 65% of GS (consistent with Woo's actual 2026 rate of 67%).

The full analysis script is available here: [analyze_trade_carroll_woo.py](https://github.com/pjrigali/pjrigali.github.io/blob/main/temp_trade_analysis/analyze_trade_carroll_woo.py)

---

### Results

| | 2025 Season | 2026 YTD | 2026 Full Season Proj |
|---|---|---|---|
| **Corbin Carroll** | 442 pts (3.1/game, G=143) | 99 pts (2.5/game, G=39) | **423 pts** |
| **Bryan Woo** | 577 pts (19.3/start, GS=30) | 139 pts (15.4/start, G=9) | **517 pts** |
| **Woo Advantage** | +135 pts | +67 pts (pace) | **+94 pts** |

---

### Key Findings

**1. Bryan Woo is an ideal fit for this scoring format.**
IP ×3 rewards pure workload, and QS +5 heavily favors consistent starters over flashy ones. Woo's 2025 season — 2.94 ERA, 15 wins, 186.2 IP, ~20 QS — scored 577 points, nearly 5x the fantasy point production of an average hitter. His 2026 is tracking identically (15.4 pts/start, 6 QS in 9 starts).

**2. Carroll's 2026 is underperforming his 2025 breakout.**
Carroll had a genuine breakout in 2025 (.259 AVG, 31 HR, 32 SB, 442 pts). But through 39 games in 2026, he's on a 411-pt pace — below last year — with only 4 stolen bases and 39 strikeouts. In a -1 K format, his strikeout rate is a persistent drag.

**3. The roster context makes it worse.**
The friend offering Woo already has deep OF (Tatis Jr., DeLauter, Pages + 3–4 UTIL bats). Carroll would be a 6th or 7th OF with no clear path to a meaningful start. Meanwhile, Bradish is flagged, Eovaldi is DTD, Abel is on IL15, and Diaz is on IL60 — Woo is one of the few healthy, reliable starters holding the rotation together.

---

### Verdict

**Decline.** Woo projects ~94 fantasy points ahead of Carroll over a full season in this format. The friend's roster needs pitching, not outfield — and Carroll's scoring-system fit (high Ks, slow SB pace) makes him less valuable here than in a standard 5×5 league.

---

#### TODO
- [x] Initial draft
- [x] Add scoring system table
- [x] Add methodology and data sources
- [x] Add results table
- [x] Spell check

---

[Home](https://pjrigali.github.io)

*Last Updated: 2026-05-14*
