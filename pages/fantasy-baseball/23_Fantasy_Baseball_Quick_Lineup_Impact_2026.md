---
layout: default
title: "23_ESPN Quick Lineup Impact Analysis 2026"
description: Quantifying how much production each team left on the bench — broken down by whether the bench placement was made by Quick Lineup or by the manager — through the first 36 scoring periods of the 2026 season.
permalink: /fantasy-baseball/quick-lineup-impact-2026
parent: Fantasy Baseball
nav_order: 10
---

# ⚾ ESPN Quick Lineup Impact — 2026 Season

*Who is actually putting good players on the bench? A player-by-player audit of bench placement decisions across all 10 teams through scoring period 36 (Apr 30, 2026).*

---

## Methodology

**Data sources:** `activity_espn_season_2026.csv` (lineup move log) and `stats_espn_daily_2026.csv` (daily player box scores), both pulled from the ESPN API.

**Bench placement attribution** operates at the individual player level. For each bench or IL batter on each day, the analysis finds the most recent move recorded in the activity log that placed that player in their current bench slot, then attributes the bench decision to that source:

| Source value | Attribution | Explanation |
|---|---|---|
| `CPU` | **Quick Lineup** | User pressed the Quick Lineup button — all moves fire at the same millisecond |
| `NightlyLeagueUpdateTaskProcessor` | **Quick Lineup** | ESPN's nightly automated lineup backend |
| `CPU_USER_INITIATED` | **Manual** | User manually applied their own lineup changes |
| `{GUID}` strings | **Manual** | Device-session individual drag-and-drop moves |
| No recorded move | **Default/carried-over** | Player has been on bench since a prior move or was acquired directly onto bench |

**Missed stats** = counting stats (R, HR, RBI, SB) produced by that bench player on the day they were benched. A bench player who had no game that day contributes zero regardless of attribution.

**Avg missed / day** = season total missed divided by the number of days in that classification (QL days for QL-placed, manual days for manually-placed). This represents the average daily cost of each placement type.

**Pitching scope:** QS and SVHD are measured from active pitcher slots (SP, RP, P) and compared across Quick Lineup vs Manual *days* (day-level classification). Bench pitcher slot data is only available from April 28 onward due to an ESPN API limitation.

---

## League-Wide Summary

### Batting: Bench Misses by Placement Type

| Team | QL Days | % QL | QL-Placed Missed | Manual-Placed Missed |
|---|---|---|---|---|
| Big Dumpers | 20/36 | 55.6% | **58** | 14 |
| Datalickmyballs | 20/36 | 55.6% | **35** | 26 |
| Big Papi | 19/36 | 52.8% | 24 | **42** |
| Midnight Muncy's | 20/36 | 55.6% | 6 | **1** |
| All Rise | 16/36 | 44.4% | 6 | **57** |
| Skubal Snacks | 11/36 | 30.6% | 4 | **31** |
| This Schlitt is Bazzanas | 9/36 | 25.0% | 1 | **15** |
| Dingers Only | 6/36 | 16.7% | 3 | **67** |
| Shohei Me the Money | 2/36 | 5.6% | 0 | **34** |
| Welcome to the JUNGle | 1/36 | 2.8% | 2 | **70** |

*Missed = R + HR + RBI + SB produced by bench/IL batters who had a game. Bold = larger of the two for that team.*

**Key finding:** For 8 of 10 teams, **manual bench placement decisions cost more production than Quick Lineup does**. Big Dumpers is the clear exception — QL is systematically benching their best hitters. Midnight Muncy's is essentially lossless on both sides: just 7 total missed counting stats all season across 36 days.

### Pitching: QS and SVHD Production (Active Slots, through Apr 30)

QS and SVHD come from active pitcher slots (SP, RP, P) only, compared across Quick Lineup vs Manual *days* (day-level classification). League-wide, manual days outperform Quick Lineup days on both pitching stats.

| Team | QL QS/day | Man QS/day | QS Gap | QL SVHD/day | Man SVHD/day | SVHD Gap |
|---|---|---|---|---|---|---|
| This Schlitt is Bazzanas | 0.222 | 0.750 | Manual +0.528 | 0.444 | 0.625 | Manual +0.181 |
| Big Papi | 0.211 | 0.412 | Manual +0.201 | 0.421 | 0.765 | Manual +0.344 |
| Big Dumpers | 0.350 | 0.625 | Manual +0.275 | 0.300 | 0.500 | Manual +0.200 |
| Midnight Muncy's | 0.350 | 0.562 | Manual +0.213 | 0.750 | 0.750 | Tied |
| Skubal Snacks | 0.545 | 0.400 | QL +0.145 | 0.545 | 0.680 | Manual +0.135 |
| Datalickmyballs | 0.650 | 0.500 | QL +0.150 | 0.750 | 0.812 | Manual +0.062 |
| Dingers Only | 0.500 | 0.333 | QL +0.167 | 0.833 | 0.633 | QL +0.200 |
| All Rise | 0.562 | 0.250 | QL +0.312 | 0.375 | 0.350 | QL +0.025 |
| Shohei Me the Money* | 1.000 | 0.353 | — | 1.000 | 0.647 | — |
| Welcome to the JUNGle* | 0.000 | 0.312 | — | 2.000 | 0.594 | — |
| **League avg** | **0.427** | **0.436** | **Manual +0.009** | **0.556** | **0.640** | **Manual +0.084** |

*\* Shohei Me the Money (2 QL days) and Welcome to the JUNGle (1 QL day) have too few Quick Lineup days for meaningful rate comparison.*

---

## Per-Team Breakdown

---

### All Rise

**Quick Lineup usage:** 16 of 36 days (44.4%)

#### Bench Misses: Quick Lineup-Placed

| Metric | Value |
|---|---|
| Season R missed | 3 |
| Season HR missed | 0 |
| Season RBI missed | 1 |
| Season SB missed | 2 |
| **Total counting missed** | **6** |
| Avg R missed / QL day | 0.19 |
| Avg HR missed / QL day | 0.00 |
| Avg RBI missed / QL day | 0.06 |
| Avg SB missed / QL day | 0.13 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-03-29 | Max Muncy | 1 | 0 | 0 | 1 | 0.400 | 2 |
| 2026-03-29 | Chandler Simpson | 1 | 0 | 0 | 0 | 1.000 | 1 |
| 2026-03-31 | Chandler Simpson | 0 | 0 | 0 | 1 | 0.500 | 1 |
| 2026-04-01 | Justin Crawford | 1 | 0 | 0 | 0 | 0.667 | 1 |
| 2026-04-02 | Justin Crawford | 0 | 0 | 1 | 0 | 1.400 | 1 |

Quick Lineup benched minor contributors — Chandler Simpson and Justin Crawford are depth pieces whose bench placement cost little. Only 6 total missed counting stats from QL decisions all season.

#### Bench Misses: Manually Placed

| Metric | Value |
|---|---|
| Season R missed | 29 |
| Season HR missed | 3 |
| Season RBI missed | 22 |
| Season SB missed | 3 |
| **Total counting missed** | **57** |
| Avg R missed / manual day | 1.45 |
| Avg HR missed / manual day | 0.15 |
| Avg RBI missed / manual day | 1.10 |
| Avg SB missed / manual day | 0.15 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-04 | Chase DeLauter | 1 | 1 | 3 | 0 | 2.250 | 5 |
| 2026-04-15 | Munetaka Murakami | 2 | 1 | 2 | 0 | 1.933 | 5 |
| 2026-04-22 | Sam Antonacci | 1 | 1 | 3 | 0 | 1.800 | 5 |
| 2026-04-13 | Mike Trout | 3 | 0 | 1 | 0 | 1.350 | 4 |
| 2026-04-18 | Matt Chapman | 1 | 0 | 3 | 0 | 1.200 | 4 |

All Rise's real bench problem is manual decisions — nine times the damage of QL. Mike Trout producing 3 R on 2026-04-13 while benched was a manual call, not Quick Lineup. The same applies to Murakami, Antonacci, and Chapman.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 16 | 20 | — |
| QS total | 9 | 5 | QL +4 |
| QS avg/day | 0.562 | 0.250 | QL +0.312/day |
| SVHD total | 6 | 7 | Manual +1 |
| SVHD avg/day | 0.375 | 0.350 | QL +0.025/day |

All Rise's pitching staff performs better on Quick Lineup days. No pitching cost from QL — the QS gap reflects when starts happen to fall, not a lineup decision effect.

---

### Big Dumpers

**Quick Lineup usage:** 20 of 36 days (55.6%)

#### Bench Misses: Quick Lineup-Placed

| Metric | Value |
|---|---|
| Season R missed | 21 |
| Season HR missed | 9 |
| Season RBI missed | 25 |
| Season SB missed | 3 |
| **Total counting missed** | **58** |
| Avg R missed / QL day | 1.05 |
| Avg HR missed / QL day | 0.45 |
| Avg RBI missed / QL day | 1.25 |
| Avg SB missed / QL day | 0.15 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-02 | Jonathan India | 1 | 1 | 5 | 0 | 1.400 | 7 |
| 2026-04-29 | Pete Crow-Armstrong | 2 | 1 | 3 | 0 | 1.400 | 6 |
| 2026-04-07 | Jonathan India | 1 | 1 | 3 | 0 | 1.750 | 5 |
| 2026-03-31 | Ian Happ | 2 | 1 | 1 | 0 | 1.400 | 4 |
| 2026-04-15 | Jordan Beck | 2 | 1 | 1 | 0 | 1.400 | 4 |

Big Dumpers is the clearest case in the league of Quick Lineup causing real damage. Jonathan India benched by QL twice — 12 combined counting stats across those two games (1 HR, 8 RBI) — is a category-swinging cost on RBI. At 1.25 RBI/QL day missed, QL is consistently leaving runs on the bench.

#### Bench Misses: Manually Placed

| Metric | Value |
|---|---|
| Season R missed | 5 |
| Season HR missed | 1 |
| Season RBI missed | 7 |
| Season SB missed | 1 |
| **Total counting missed** | **14** |
| Avg R missed / manual day | 0.31 |
| Avg HR missed / manual day | 0.06 |
| Avg RBI missed / manual day | 0.44 |
| Avg SB missed / manual day | 0.06 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-16 | Trevor Story | 1 | 1 | 5 | 0 | 2.100 | 7 |
| 2026-04-18 | Marcus Semien | 1 | 0 | 1 | 0 | 1.250 | 2 |
| 2026-04-15 | Zach McKinstry | 1 | 0 | 0 | 0 | 1.000 | 1 |
| 2026-04-16 | Marcus Semien | 0 | 0 | 1 | 0 | 0.833 | 1 |
| 2026-04-17 | Jonathan India | 1 | 0 | 0 | 0 | 0.750 | 1 |

Trevor Story's 2026-04-16 (1 HR, 5 RBI, 2.100 OPS) while manually benched is the standout single miss. Manual decisions account for about a quarter of total damage — QL is the primary culprit here.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 20 | 16 | — |
| QS total | 7 | 10 | Manual +3 |
| QS avg/day | 0.350 | 0.625 | Manual +0.275/day |
| SVHD total | 6 | 8 | Manual +2 |
| SVHD avg/day | 0.300 | 0.500 | Manual +0.200/day |
| Season opp cost | — | — | ~5.5 QS, ~4.0 SVHD |

Big Dumpers compounds the batting cost with a pitching cost — manual days produce significantly more QS and SVHD. Across 20 QL days the rate gap represents roughly 5–6 missed Quality Starts.

---

### Big Papi

**Quick Lineup usage:** 19 of 36 days (52.8%)

#### Bench Misses: Quick Lineup-Placed

| Metric | Value |
|---|---|
| Season R missed | 12 |
| Season HR missed | 3 |
| Season RBI missed | 5 |
| Season SB missed | 4 |
| **Total counting missed** | **24** |
| Avg R missed / QL day | 0.63 |
| Avg HR missed / QL day | 0.16 |
| Avg RBI missed / QL day | 0.26 |
| Avg SB missed / QL day | 0.21 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-02 | Otto Lopez | 3 | 1 | 1 | 0 | 2.350 | 5 |
| 2026-04-02 | Ramon Laureano | 2 | 1 | 2 | 0 | 1.750 | 5 |
| 2026-04-09 | Ramon Laureano | 1 | 0 | 0 | 2 | 0.800 | 3 |
| 2026-04-11 | Wyatt Langford | 1 | 1 | 1 | 0 | 1.667 | 3 |
| 2026-03-29 | Otto Lopez | 1 | 0 | 0 | 1 | 0.500 | 2 |

Ramon Laureano appears twice in QL misses — QL repeatedly undervalues his mixed-category contributions. Otto Lopez's 2026-04-02 game (5 counting stats, 2.350 OPS) is the single biggest QL miss on this team.

#### Bench Misses: Manually Placed

| Metric | Value |
|---|---|
| Season R missed | 18 |
| Season HR missed | 4 |
| Season RBI missed | 17 |
| Season SB missed | 3 |
| **Total counting missed** | **42** |
| Avg R missed / manual day | 1.06 |
| Avg HR missed / manual day | 0.24 |
| Avg RBI missed / manual day | 1.00 |
| Avg SB missed / manual day | 0.18 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-15 | Jake Bauers | 1 | 1 | 3 | 0 | 1.400 | 5 |
| 2026-04-26 | Salvador Perez | 2 | 1 | 2 | 0 | 1.800 | 5 |
| 2026-04-06 | TJ Rumfield | 1 | 1 | 2 | 0 | 1.250 | 4 |
| 2026-04-19 | Lawrence Butler | 1 | 0 | 1 | 2 | 1.267 | 4 |
| 2026-04-22 | Maikel Garcia | 2 | 0 | 1 | 1 | 0.933 | 4 |

Manual decisions account for nearly double the missed production of QL. At 1.00 RBI/manual day missed, the bench audit habit would have the biggest impact for this team.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 19 | 17 | — |
| QS total | 4 | 7 | Manual +3 |
| QS avg/day | 0.211 | 0.412 | Manual +0.201/day |
| SVHD total | 8 | 13 | Manual +5 |
| SVHD avg/day | 0.421 | 0.765 | Manual +0.344/day |
| Season opp cost | — | — | ~3.8 QS, ~6.5 SVHD |

The largest SVHD gap in the league. Big Papi's bullpen produces nearly half the holds/saves on QL days — roughly 6–7 missed SVHD at the season level.

---

### Datalickmyballs

**Quick Lineup usage:** 20 of 36 days (55.6%)

#### Bench Misses: Quick Lineup-Placed

| Metric | Value |
|---|---|
| Season R missed | 18 |
| Season HR missed | 2 |
| Season RBI missed | 10 |
| Season SB missed | 5 |
| **Total counting missed** | **35** |
| Avg R missed / QL day | 0.90 |
| Avg HR missed / QL day | 0.10 |
| Avg RBI missed / QL day | 0.50 |
| Avg SB missed / QL day | 0.25 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-09 | Hunter Goodman | 3 | 1 | 1 | 1 | 2.800 | 6 |
| 2026-04-05 | Giancarlo Stanton | 1 | 0 | 2 | 1 | 0.933 | 4 |
| 2026-04-05 | Gleyber Torres | 2 | 1 | 1 | 0 | 1.850 | 4 |
| 2026-03-29 | Trent Grisham | 1 | 0 | 0 | 1 | 0.833 | 2 |
| 2026-03-31 | Brenton Doyle | 2 | 0 | 0 | 0 | 1.667 | 2 |

Hunter Goodman's 3 R / 1 HR / 1 RBI / 1 SB (OPS 2.800) on 2026-04-09 while QL-benched is the biggest single-day QL miss in the entire league. Giancarlo Stanton in the top 5 suggests a recurring slot management problem.

#### Bench Misses: Manually Placed

| Metric | Value |
|---|---|
| Season R missed | 14 |
| Season HR missed | 3 |
| Season RBI missed | 7 |
| Season SB missed | 2 |
| **Total counting missed** | **26** |
| Avg R missed / manual day | 0.88 |
| Avg HR missed / manual day | 0.19 |
| Avg RBI missed / manual day | 0.44 |
| Avg SB missed / manual day | 0.13 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-27 | Gleyber Torres | 3 | 1 | 2 | 0 | 1.800 | 6 |
| 2026-04-16 | Jacob Wilson | 1 | 1 | 2 | 0 | 1.750 | 4 |
| 2026-04-19 | Jacob Wilson | 2 | 1 | 1 | 0 | 1.167 | 4 |
| 2026-04-25 | Brenton Doyle | 1 | 0 | 0 | 1 | 0.833 | 2 |
| 2026-04-30 | Jacob Wilson | 2 | 0 | 0 | 0 | 1.750 | 2 |

Jacob Wilson appears three times in the manual miss list — a recurring failure to start an ascending hitter. Torres appearing in both QL and manual top 5 suggests a systemic slot management issue with that player regardless of how the lineup is set.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 20 | 16 | — |
| QS total | 13 | 8 | QL +5 |
| QS avg/day | 0.650 | 0.500 | QL +0.150/day |
| SVHD total | 15 | 13 | QL +2 |
| SVHD avg/day | 0.750 | 0.812 | Manual +0.062/day |

One of the few teams where QL days outperform on QS. The pitching side is neutral-to-positive for QL; the damage is entirely on batting bench placement.

---

### Dingers Only

**Quick Lineup usage:** 6 of 36 days (16.7%)

#### Bench Misses: Quick Lineup-Placed

| Metric | Value |
|---|---|
| Season R missed | 0 |
| Season HR missed | 0 |
| Season RBI missed | 3 |
| Season SB missed | 0 |
| **Total counting missed** | **3** |
| Avg R missed / QL day | 0.00 |
| Avg HR missed / QL day | 0.00 |
| Avg RBI missed / QL day | 0.50 |
| Avg SB missed / QL day | 0.00 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-15 | Xander Bogaerts | 0 | 0 | 3 | 0 | 1.500 | 3 |

Only one QL-placed bench batter with a game all season. Quick Lineup is not the problem for this team.

#### Bench Misses: Manually Placed

| Metric | Value |
|---|---|
| Season R missed | 34 |
| Season HR missed | 5 |
| Season RBI missed | 25 |
| Season SB missed | 3 |
| **Total counting missed** | **67** |
| Avg R missed / manual day | 1.13 |
| Avg HR missed / manual day | 0.17 |
| Avg RBI missed / manual day | 0.83 |
| Avg SB missed / manual day | 0.10 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-14 | Jake Burger | 2 | 2 | 4 | 0 | 2.600 | 8 |
| 2026-03-29 | Ezequiel Tovar | 1 | 1 | 2 | 0 | 1.250 | 4 |
| 2026-04-01 | Max Muncy | 2 | 1 | 1 | 0 | 2.417 | 4 |
| 2026-04-06 | Carlos Correa | 2 | 0 | 1 | 1 | 0.900 | 4 |
| 2026-04-25 | Wilyer Abreu | 2 | 1 | 1 | 0 | 2.000 | 4 |

Jake Burger's 2026-04-14 game (2 HR, 4 RBI, 2.600 OPS) — the single largest missed performance in the entire league — was a **manual bench decision**, not Quick Lineup. At 1.13 R/manual day missed, Dingers Only's manager decisions are consistently leaving runs on the table.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 6 | 30 | — |
| QS avg/day | 0.500 | 0.333 | QL +0.167/day |
| SVHD avg/day | 0.833 | 0.633 | QL +0.200/day |

With only 6 QL days the pitching sample is thin. Pitching production is not a concern — the issue is entirely manual batting bench decisions.

---

### Midnight Muncy's

**Quick Lineup usage:** 20 of 36 days (55.6%)

#### Bench Misses: Quick Lineup-Placed

| Metric | Value |
|---|---|
| Season R missed | 2 |
| Season HR missed | 1 |
| Season RBI missed | 3 |
| Season SB missed | 0 |
| **Total counting missed** | **6** |
| Avg R missed / QL day | 0.10 |
| Avg HR missed / QL day | 0.05 |
| Avg RBI missed / QL day | 0.15 |
| Avg SB missed / QL day | 0.00 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-18 | Jeremiah Jackson | 1 | 1 | 3 | 0 | 1.250 | 5 |
| 2026-03-31 | Colton Cowser | 1 | 0 | 0 | 0 | 1.167 | 1 |
| 2026-03-31 | Coby Mayo | 0 | 0 | 0 | 0 | 0.000 | 0 |
| 2026-04-23 | Juan Soto | 0 | 0 | 0 | 0 | 0.833 | 0 |
| 2026-04-25 | Juan Soto | 0 | 0 | 0 | 0 | 0.500 | 0 |

Jeremiah Jackson's 2026-04-18 game (5 counting stats) is the only meaningful QL-placed miss all season. Juan Soto appearing twice with zero counting stats in either game shows that even the near-misses are low-cost.

#### Bench Misses: Manually Placed

| Metric | Value |
|---|---|
| Season R missed | 0 |
| Season HR missed | 0 |
| Season RBI missed | 1 |
| Season SB missed | 0 |
| **Total counting missed** | **1** |
| Avg R missed / manual day | 0.00 |
| Avg HR missed / manual day | 0.00 |
| Avg RBI missed / manual day | 0.06 |
| Avg SB missed / manual day | 0.00 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-03-29 | Kyle Manzardo | 0 | 0 | 1 | 0 | 0.400 | 1 |

**The benchmark team.** Midnight Muncy's uses Quick Lineup 55.6% of days — tied for most in the league — and loses essentially nothing from either placement type. 7 total missed counting stats across all 36 days combined. This is what optimal roster management looks like.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 20 | 16 | — |
| QS total | 7 | 9 | Manual +2 |
| QS avg/day | 0.350 | 0.562 | Manual +0.213/day |
| SVHD total | 15 | 12 | QL +3 |
| SVHD avg/day | 0.750 | 0.750 | Tied |

SVHD is exactly tied. Even the benchmark team shows a slight QS edge for manual days — the one area with room to improve.

---

### Shohei Me the Money

**Quick Lineup usage:** 2 of 36 days (5.6%)

#### Bench Misses: Quick Lineup-Placed

| Metric | Value |
|---|---|
| Season R missed | 0 |
| Season HR missed | 0 |
| Season RBI missed | 0 |
| Season SB missed | 0 |
| **Total counting missed** | **0** |
| Avg R missed / QL day | 0.00 |
| Avg HR missed / QL day | 0.00 |
| Avg RBI missed / QL day | 0.00 |
| Avg SB missed / QL day | 0.00 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-16 | Francisco Alvarez | 0 | 0 | 0 | 0 | 0.500 | 0 |
| 2026-04-30 | Francisco Alvarez | 0 | 0 | 0 | 0 | 0.000 | 0 |

Zero missed production from QL placements. The two QL days both benched Alvarez, who produced nothing in either game.

#### Bench Misses: Manually Placed

| Metric | Value |
|---|---|
| Season R missed | 16 |
| Season HR missed | 3 |
| Season RBI missed | 14 |
| Season SB missed | 1 |
| **Total counting missed** | **34** |
| Avg R missed / manual day | 0.47 |
| Avg HR missed / manual day | 0.09 |
| Avg RBI missed / manual day | 0.41 |
| Avg SB missed / manual day | 0.03 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-25 | Will Smith | 1 | 1 | 3 | 0 | 1.250 | 5 |
| 2026-04-22 | Adley Rutschman | 1 | 1 | 2 | 0 | 1.750 | 4 |
| 2026-04-30 | Ernie Clement | 1 | 1 | 2 | 0 | 1.000 | 4 |
| 2026-04-30 | Willi Castro | 2 | 0 | 1 | 0 | 1.350 | 3 |
| 2026-04-11 | Ernie Clement | 1 | 0 | 1 | 0 | 1.250 | 2 |

An additional 42 missed counting stats come from "default/carried-over" placements — Heliot Ramos (6, 5, and 3-count games) and Willi Castro (5-count game) sitting on a persistent bench state that was never revisited. That carried-over bench cost exceeds the manual cost.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 2 | 34 | — |
| QS avg/day | 1.000 | 0.353 | (2 QL days — not comparable) |
| SVHD avg/day | 1.000 | 0.647 | (2 QL days — not comparable) |

Two QL days is too small a sample. Pitching production is essentially entirely manual at 0.353 QS/day and 0.647 SVHD/day.

---

### Skubal Snacks

**Quick Lineup usage:** 11 of 36 days (30.6%)

#### Bench Misses: Quick Lineup-Placed

| Metric | Value |
|---|---|
| Season R missed | 1 |
| Season HR missed | 0 |
| Season RBI missed | 2 |
| Season SB missed | 1 |
| **Total counting missed** | **4** |
| Avg R missed / QL day | 0.09 |
| Avg HR missed / QL day | 0.00 |
| Avg RBI missed / QL day | 0.18 |
| Avg SB missed / QL day | 0.09 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-03-31 | Jordan Lawlar | 1 | 0 | 1 | 1 | 1.417 | 3 |
| 2026-03-29 | Nolan Gorman | 0 | 0 | 1 | 0 | 0.500 | 1 |
| 2026-03-29 | Noelvi Marte | 0 | 0 | 0 | 0 | 0.000 | 0 |
| 2026-04-08 | Josh Naylor | 0 | 0 | 0 | 0 | 0.000 | 0 |
| 2026-04-09 | Carson Benge | 0 | 0 | 0 | 0 | 0.500 | 0 |

Minimal QL damage — just 4 counting stats total across 6 QL-placed bench appearances with games.

#### Bench Misses: Manually Placed

| Metric | Value |
|---|---|
| Season R missed | 13 |
| Season HR missed | 2 |
| Season RBI missed | 11 |
| Season SB missed | 5 |
| **Total counting missed** | **31** |
| Avg R missed / manual day | 0.52 |
| Avg HR missed / manual day | 0.08 |
| Avg RBI missed / manual day | 0.44 |
| Avg SB missed / manual day | 0.20 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-02 | Eugenio Suarez | 1 | 1 | 2 | 0 | 2.500 | 4 |
| 2026-04-08 | Matt McLain | 1 | 0 | 2 | 1 | 1.200 | 4 |
| 2026-03-31 | Nolan Gorman | 1 | 1 | 1 | 0 | 1.250 | 3 |
| 2026-03-29 | Owen Caissie | 0 | 0 | 1 | 1 | 1.750 | 2 |
| 2026-03-31 | Carson Benge | 1 | 0 | 0 | 1 | 1.000 | 2 |

Note: Carson Benge's opening-week 5-count game (2026-03-27, 1.933 OPS) is in "default/carried-over" since no recorded move placed him there. Manual decisions still account for the bulk: 31 total vs 4 from QL.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 11 | 25 | — |
| QS avg/day | 0.545 | 0.400 | QL +0.145/day |
| SVHD avg/day | 0.545 | 0.680 | Manual +0.135/day |

Mixed pitching picture — QL days slightly better on QS, manual days better on SVHD. Net effect close to neutral.

---

### This Schlitt is Bazzanas

**Quick Lineup usage:** 9 of 36 days (25.0%)

#### Bench Misses: Quick Lineup-Placed

| Metric | Value |
|---|---|
| Season R missed | 1 |
| Season HR missed | 0 |
| Season RBI missed | 0 |
| Season SB missed | 0 |
| **Total counting missed** | **1** |
| Avg R missed / QL day | 0.11 |
| Avg HR missed / QL day | 0.00 |
| Avg RBI missed / QL day | 0.00 |
| Avg SB missed / QL day | 0.00 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-09 | Bo Bichette | 1 | 0 | 0 | 0 | 1.000 | 1 |
| 2026-04-08 | Jac Caglianone | 0 | 0 | 0 | 0 | 0.000 | 0 |
| 2026-04-22 | Jac Caglianone | 0 | 0 | 0 | 0 | 0.000 | 0 |
| 2026-04-29 | Jac Caglianone | 0 | 0 | 0 | 0 | 0.000 | 0 |

Near-zero QL batting cost. Caglianone appearing three times with no production in any game keeps QL damage negligible.

#### Bench Misses: Manually Placed

| Metric | Value |
|---|---|
| Season R missed | 7 |
| Season HR missed | 0 |
| Season RBI missed | 7 |
| Season SB missed | 1 |
| **Total counting missed** | **15** |
| Avg R missed / manual day | 0.26 |
| Avg HR missed / manual day | 0.00 |
| Avg RBI missed / manual day | 0.26 |
| Avg SB missed / manual day | 0.04 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-02 | Jac Caglianone | 3 | 0 | 0 | 0 | 1.800 | 3 |
| 2026-03-31 | Moises Ballesteros | 0 | 0 | 2 | 0 | 0.500 | 2 |
| 2026-04-11 | Luis Garcia Jr. | 1 | 0 | 1 | 0 | 0.500 | 2 |
| 2026-04-12 | Fernando Tatis Jr. | 0 | 0 | 1 | 1 | 1.800 | 2 |
| 2026-04-15 | Luis Garcia Jr. | 1 | 0 | 1 | 0 | 1.167 | 2 |

Modest overall numbers. Luis Garcia Jr. appearing twice in manual misses is a recurring slot decision worth revisiting.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 9 | 27 | — |
| QS total | 2 | 18 | Manual +16 |
| QS avg/day | 0.222 | 0.750 | Manual +0.528/day |
| SVHD total | 4 | 15 | Manual +11 |
| SVHD avg/day | 0.444 | 0.625 | Manual +0.181/day |
| Season opp cost | — | — | ~4.8 QS, ~1.6 SVHD |

The worst pitching gap in the league. Despite minimal batting cost from QL, active pitchers produce far less on QL days. The biggest Quick Lineup opportunity cost for this team is on the mound, not at the plate.

---

### Welcome to the JUNGle

**Quick Lineup usage:** 1 of 36 days (2.8%)

#### Bench Misses: Quick Lineup-Placed

| Metric | Value |
|---|---|
| Season R missed | 2 |
| Season HR missed | 0 |
| Season RBI missed | 0 |
| Season SB missed | 0 |
| **Total counting missed** | **2** |
| Avg R missed / QL day | 2.00 |
| Avg HR missed / QL day | 0.00 |
| Avg RBI missed / QL day | 0.00 |
| Avg SB missed / QL day | 0.00 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-04-18 | Michael Busch | 2 | 0 | 0 | 0 | 1.100 | 2 |
| 2026-04-19 | Michael Busch | 0 | 0 | 0 | 0 | 0.500 | 0 |
| 2026-04-20 | Michael Busch | 0 | 0 | 0 | 0 | 0.000 | 0 |

The team uses Quick Lineup on just 1 day all season. QL cost is negligible.

#### Bench Misses: Manually Placed

| Metric | Value |
|---|---|
| Season R missed | 25 |
| Season HR missed | 5 |
| Season RBI missed | 33 |
| Season SB missed | 7 |
| **Total counting missed** | **70** |
| Avg R missed / manual day | 0.71 |
| Avg HR missed / manual day | 0.14 |
| Avg RBI missed / manual day | 0.94 |
| Avg SB missed / manual day | 0.20 |

| Date | Player | R | HR | RBI | SB | OPS | Total |
|---|---|---|---|---|---|---|---|
| 2026-03-29 | Royce Lewis | 2 | 1 | 2 | 1 | 1.833 | 6 |
| 2026-04-06 | Tyler Soderstrom | 3 | 0 | 3 | 0 | 1.250 | 6 |
| 2026-04-25 | Konnor Griffin | 1 | 1 | 3 | 1 | 2.250 | 6 |
| 2026-04-04 | Tyler Soderstrom | 2 | 0 | 2 | 0 | 1.350 | 4 |
| 2026-04-04 | Alec Bohm | 1 | 0 | 3 | 0 | 0.800 | 4 |

The highest manual-placement missed total in the league (70 counting stats). Tyler Soderstrom appears twice — a recurring failure to start a productive bat. At 0.94 RBI/manual day missed, this is one of the costliest bench management patterns in the league.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 1 | 35 | — |
| QS avg/day | 0.000 | 0.312 | (1 QL day — not comparable) |
| SVHD avg/day | 2.000 | 0.594 | (1 QL day — not comparable) |

One Quick Lineup day is insufficient for rate comparison. Pitching production is essentially entirely manual at 0.312 QS/day and 0.594 SVHD/day.

---

## The Better Approach: Replacing Quick Lineup

### How Quick Lineup Actually Works

Before replacing it, it helps to understand exactly what Quick Lineup does — and what it doesn't do.

**What ESPN officially states:**
- It only considers players who have a game scheduled that day
- It fills all eligible roster slots automatically
- It prioritizes players based on ESPN's own player rankings

That's the complete published mechanic. Everything else is inferred from observed behavior.

**The underlying data inputs:**

| Input | Role | Notes |
|---|---|---|
| Daily MLB schedule | Hard filter — players with no game are excluded entirely | The one thing QL does well |
| Position eligibility | Constrains which slots each player can fill | Respects multi-position designations |
| ESPN player rankings | Primary ranking signal driving who starts | Blends season projections, recent performance, and scoring format |
| Probable pitcher tags | Secondary signal for SP slots | Inferred from behavior, not officially confirmed |
| Injury / status flags | Excludes OUT and IL-listed players | Confirmed behavior |

**What the algorithm likely looks like in practice:**

```python
# Step 1 — Filter to players with a game today
eligible = [p for p in roster if p.has_game_today and p.status not in ("OUT", "IL")]

# Step 2 — Score by ESPN ranking (lower rank number = higher priority)
eligible.sort(key=lambda p: p.espn_ranking)

# Step 3 — Greedy slot fill: place each player in their best available slot
for player in eligible:
    place_in_best_available_slot(player)
```

This is a **greedy assignment algorithm** — not a combinatorial optimizer. It does not evaluate all possible lineup combinations. It fills slots one player at a time in ranking order, which means early placements can block better combinations later.

**What it explicitly does NOT do:**

- Optimize for category balance — it has no concept of H2H category margins
- Simulate matchup outcomes or consider what the opponent is doing
- Account for hot/cold streaks beyond what's already baked into ESPN's rankings
- Consider slot efficiency (e.g., whether a high-SB player is placed in the best slot to maximize SB contribution)
- Evaluate player correlations or stacking

The data makes this concrete: Jake Burger (2 HR, 4 RBI, 2.600 OPS on 2026-04-14) was manually benched — a human decision that failed the same way the greedy algorithm can. The difference is that manual decisions *can* incorporate category awareness and matchup context; Quick Lineup structurally cannot.

---

### The Manual Process: A Better Five-Step Approach

Quick Lineup's ranking-driven greedy fill is fast but blind to your specific situation. This process takes 5–10 minutes each morning and directly addresses the gaps:

#### Step 1 — Games-played filter
Any player whose MLB team is **not playing that day** sits automatically. This is the one thing Quick Lineup does correctly. Check the MLB daily schedule each morning and move all no-game players to bench before anything else.

#### Step 2 — Injury and lineup-card check
Pull Rotowire or ESPN news by 11am ET. Scratch any player listed as resting, day-to-day, or a late scratch. Confirm SPs are tagged as probable starters before sliding them into SP slots — Quick Lineup uses "PP" tags but those aren't always updated in time.

#### Step 3 — Identify your weekly category deficits
This is the step Quick Lineup skips entirely. Check your current H2H matchup standings. Find the 1–3 categories where you are losing or within striking distance. Rank your available players by their 14-day rolling stats in those specific categories, not by overall ESPN ranking. A player producing 0.400 OPS with 2 SB is more valuable in a SB-deficit week than a 0.900 OPS player with zero speed.

#### Step 4 — Fill active slots by position eligibility from that ranked list
Work through your active slots using the category-aware ranked list from step 3. Start with your most position-constrained slots (C, 2B/SS) and fill from the top of the list. If two players are ranked equally, start the one with multi-position eligibility to keep the bench flexible for later in the week.

#### Step 5 — Bench audit
Final check: every benched player either has no game today, or was explicitly ranked below the player in their slot in step 3. If any bench player with a game ranks above an active player at a compatible slot, swap them. This catches the greedy-algorithm failure mode directly — and the manual-decision failure mode too.

The data shows that for most teams in this league, the bigger problem isn't Quick Lineup — it's manual decisions that leave productive players on the bench for multiple days without revisiting. Big Dumpers is the exception where QL is clearly the culprit (58 QL-placed missed counting stats). For everyone else, Step 5's bench audit applied to manual decisions is the highest-leverage habit change.

---

*Data through scoring period 36 (Apr 30, 2026). Player-level bench placement attribution uses the ESPN activity log. Analysis source: [`analyze_quick_lineup_impact.py`](https://github.com/pjrigali/acn_repo/blob/main/fantasy_baseball/analyze_quick_lineup_impact.py)*

*[Home](https://pjrigali.github.io)*

*Last updated: 2026-04-30*
