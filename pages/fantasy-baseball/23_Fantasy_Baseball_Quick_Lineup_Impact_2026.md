---
layout: default
title: "23_ESPN Quick Lineup Impact Analysis 2026"
description: Quantifying how much production each team left on the bench by relying on ESPN's Quick Lineup feature through the first 33 scoring periods of the 2026 season.
permalink: /fantasy-baseball/quick-lineup-impact-2026
parent: Fantasy Baseball
nav_order: 10
---

# ⚾ ESPN Quick Lineup Impact — 2026 Season

*How much production is Quick Lineup leaving on the bench? A day-by-day audit across all 10 teams through scoring period 33 (Apr 27, 2026).*

---

## Methodology

**Data sources:** `activity_espn_season_2026.csv` (lineup move log) and `stats_espn_daily_2026.csv` (daily player box scores), both pulled from the ESPN API.

**Quick Lineup classification** uses the `source` field in the activity log:

| Source value | Classification | Explanation |
|---|---|---|
| `CPU` | Quick Lineup | User pressed the Quick Lineup button in the ESPN app — all moves fire at the same millisecond |
| `NightlyLeagueUpdateTaskProcessor` | Quick Lineup | ESPN's nightly automated lineup backend |
| `CPU_USER_INITIATED` | Manual | User manually applied their own lineup changes and saved them |
| `{GUID}` strings | Manual | Device-session individual drag-and-drop moves (median: 1–2 moves per batch) |

A day is classified as **Quick Lineup** if any `CPU` or `NightlyLeagueUpdateTaskProcessor` move was recorded for that team on that date. A day is **Manual** otherwise.

**Missed stats** = counting stats (R, HR, RBI, SB) produced by bench-slot batters who actually had plate appearances on a Quick Lineup day. These are stats the team's active lineup did not capture because the player was sitting on the bench when the algorithm set the lineup. Rate stats (OPS) are reported for context but not summed.

**Batting scope:** Missed stats are calculated from bench-slot batters only, as described above.

**Pitching scope:** QS and SVHD are measured from active pitcher slots (SP, RP, P) and compared across Quick Lineup vs Manual days. A data fix was applied to the collection script (`collect_stats_espn_daily.py`) to add a secondary `mRoster` API call and capture bench/IL pitchers — the ESPN `mMatchupScore` view silently omits them. Bench/IL pitcher data is therefore only available from April 28 onward; the QS/SVHD analysis for earlier dates reflects active slots only. The one bench pitcher with measurable production in the available window (Taj Bradley, 1 QS on April 30 for All Rise, manual day) confirms the gap is real but small in the early-season sample.

---

## League-Wide Summary

| Team | QL Days | Manual Days | % Quick | Season R Missed | Season HR Missed | Season RBI Missed | Season SB Missed | Total Counting Missed |
|---|---|---|---|---|---|---|---|---|
| Big Dumpers | 21 | 12 | 63.6% | 13 | 4 | 17 | 3 | **37** |
| Datalickmyballs | 21 | 12 | 63.6% | 17 | 2 | 10 | 4 | **33** |
| Big Papi | 20 | 13 | 60.6% | 14 | 2 | 9 | 7 | **32** |
| Midnight Muncy's | 21 | 12 | 63.6% | 0 | 0 | 1 | 0 | **1** |
| All Rise | 16 | 17 | 48.5% | 14 | 2 | 8 | 1 | **25** |
| Skubal Snacks | 11 | 22 | 33.3% | 4 | 1 | 7 | 3 | **15** |
| Dingers Only | 6 | 27 | 18.2% | 7 | 2 | 11 | 1 | **21** |
| This Sh!t is Bazzana | 9 | 24 | 27.3% | 3 | 0 | 2 | 0 | **5** |
| Shohei Me the Money | 2 | 31 | 6.1% | 2 | 0 | 2 | 0 | **4** |
| Long Bohms Away | 1 | 32 | 3.0% | 0 | 0 | 0 | 0 | **0** |

**Key observation:** Midnight Muncy's uses Quick Lineup at the same rate as Big Dumpers and Datalickmyballs (~63% of days) but misses almost nothing — just 1 RBI across the entire season. This is the benchmark: Quick Lineup can be nearly lossless if the roster is deep and the algorithm has clear best-player choices. The teams at the top of the missed-stats column are paying a material cost.

### Pitching: QS and SVHD Production (Active Slots, through Apr 30)

QS and SVHD come from active pitcher slots (SP, RP, P) only. Data covers through April 30 (36 scoring periods), three days beyond the batting analysis, enabled by the bench/IL pitcher backfill fix. League-wide, manual days outperform Quick Lineup days on both pitching counting stats — the gap is small on QS (Manual +0.009/day) but more visible on SVHD (Manual +0.084/day).

| Team | QL QS/day | Man QS/day | QS Gap | QL SVHD/day | Man SVHD/day | SVHD Gap |
|---|---|---|---|---|---|---|
| This Sh!t is Bazzana | 0.222 | 0.750 | Manual +0.528 | 0.444 | 0.625 | Manual +0.181 |
| Big Papi | 0.211 | 0.412 | Manual +0.201 | 0.421 | 0.765 | Manual +0.344 |
| Big Dumpers | 0.350 | 0.625 | Manual +0.275 | 0.300 | 0.500 | Manual +0.200 |
| Midnight Muncy's | 0.350 | 0.562 | Manual +0.213 | 0.750 | 0.750 | Tied |
| Skubal Snacks | 0.545 | 0.400 | QL +0.145 | 0.545 | 0.680 | Manual +0.135 |
| Datalickmyballs | 0.650 | 0.500 | QL +0.150 | 0.750 | 0.812 | Manual +0.062 |
| Dingers Only | 0.500 | 0.333 | QL +0.167 | 0.833 | 0.633 | QL +0.200 |
| All Rise | 0.562 | 0.250 | QL +0.312 | 0.375 | 0.350 | QL +0.025 |
| Shohei Me the Money* | 1.000 | 0.353 | QL +0.647 | 1.000 | 0.647 | QL +0.353 |
| Long Bohms Away* | 0.000 | 0.312 | Manual +0.312 | 2.000 | 0.594 | — |
| **League avg** | **0.427** | **0.436** | **Manual +0.009** | **0.556** | **0.640** | **Manual +0.084** |

*\* Shohei Me the Money (2 QL days) and Long Bohms Away (1 QL day) have too few Quick Lineup days for meaningful per-rate comparison.*

**Pitching takeaway:** Three teams show a clear Quick Lineup penalty on the mound — This Sh!t is Bazzana misses ~5 QS and ~1.6 SVHD to the rate gap across 9 QL days; Big Papi loses ~3.8 QS and ~6.5 SVHD across 19 QL days; Big Dumpers gives up ~5.5 QS and ~4.0 SVHD across 20 QL days. The mechanism here isn't a bench pitcher being left idle (as with batters) — pitchers can't just be slotted in for an extra start. The more likely driver is that Quick Lineup misplaces relief pitchers into the wrong slots (or leaves SVHD-eligible closers/holders buried) based on overall ranking rather than role.

---

## Per-Team Breakdown

---

### All Rise

**Quick Lineup days:** 16 of 33 (48.5%)

| Metric | Value |
|---|---|
| Season R missed | 14 |
| Season HR missed | 2 |
| Season RBI missed | 8 |
| Season SB missed | 1 |
| **Total counting missed** | **25** |
| Avg R missed / QL day | 0.88 |
| Avg HR missed / QL day | 0.12 |
| Avg RBI missed / QL day | 0.50 |
| Avg SB missed / QL day | 0.06 |

#### 🔴 Top 5 Missed Performances (Quick Lineup days)

| Date | Player | R | HR | RBI | SB | OPS | Counting Total |
|---|---|---|---|---|---|---|---|
| 2026-04-22 | Sam Antonacci | 1 | 1 | 3 | 0 | 1.800 | 5 |
| 2026-04-15 | Munetaka Murakami | 2 | 1 | 2 | 0 | 1.933 | 5 |
| 2026-04-13 | Mike Trout | 3 | 0 | 1 | 0 | 1.350 | 4 |
| 2026-04-06 | Julio Rodriguez | 1 | 0 | 1 | 0 | 0.400 | 2 |
| 2026-03-29 | Max Muncy | 1 | 0 | 0 | 1 | 0.400 | 2 |

Mike Trout producing 3 R on 2026-04-13 while benched is the standout single-day miss — the algorithm left an elite player idle when he had a game.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 16 | 20 | — |
| QS total | 9 | 5 | QL +4 |
| QS avg/day | 0.562 | 0.250 | QL +0.312/day |
| SVHD total | 6 | 7 | Manual +1 |
| SVHD avg/day | 0.375 | 0.350 | QL +0.025/day |

All Rise's pitching staff performs better on Quick Lineup days — the QS gap (+0.312/day) suggests the starting rotation lines up better with games on those days rather than Quick Lineup conferring an advantage. SVHD is essentially flat. No pitching cost to note.

---

### Big Dumpers

**Quick Lineup days:** 21 of 33 (63.6%)

| Metric | Value |
|---|---|
| Season R missed | 13 |
| Season HR missed | 4 |
| Season RBI missed | 17 |
| Season SB missed | 3 |
| **Total counting missed** | **37** |
| Avg R missed / QL day | 0.62 |
| Avg HR missed / QL day | 0.19 |
| Avg RBI missed / QL day | 0.81 |
| Avg SB missed / QL day | 0.14 |

#### 🔴 Top 5 Missed Performances (Quick Lineup days)

| Date | Player | R | HR | RBI | SB | OPS | Counting Total |
|---|---|---|---|---|---|---|---|
| 2026-04-02 | Jonathan India | 1 | 1 | 5 | 0 | 1.400 | 7 |
| 2026-04-07 | Jonathan India | 1 | 1 | 3 | 0 | 1.750 | 5 |
| 2026-03-31 | Ian Happ | 2 | 1 | 1 | 0 | 1.400 | 4 |
| 2026-04-11 | Trevor Story | 1 | 0 | 1 | 1 | 0.000 | 3 |
| 2026-04-12 | Jorge Polanco | 1 | 1 | 1 | 0 | 1.000 | 3 |

Jonathan India is the story here — benched by Quick Lineup twice and produced 12 combined counting stats (1 HR, 8 RBI across the two games). That's a category-swinging miss on RBI, the stat Big Dumpers rank 1st in by projection. Quick Lineup repeatedly benched one of their best bats.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 20 | 16 | — |
| QS total | 7 | 10 | Manual +3 |
| QS avg/day | 0.350 | 0.625 | Manual +0.275/day |
| SVHD total | 6 | 8 | Manual +2 |
| SVHD avg/day | 0.300 | 0.500 | Manual +0.200/day |
| Season opp cost | — | — | ~5.5 QS, ~4.0 SVHD |

Big Dumpers has the second-worst pitching cost in the league from Quick Lineup. Across 20 QL days, the rate gap translates to roughly 5–6 fewer Quality Starts and 4 fewer holds/saves compared to what manual days produce. On a team that also ranks near the top in batting misses, the compounding effect is the most damaging in the league.

---

### Big Papi

**Quick Lineup days:** 20 of 33 (60.6%)

| Metric | Value |
|---|---|
| Season R missed | 14 |
| Season HR missed | 2 |
| Season RBI missed | 9 |
| Season SB missed | 7 |
| **Total counting missed** | **32** |
| Avg R missed / QL day | 0.70 |
| Avg HR missed / QL day | 0.10 |
| Avg RBI missed / QL day | 0.45 |
| Avg SB missed / QL day | 0.35 |

#### 🔴 Top 5 Missed Performances (Quick Lineup days)

| Date | Player | R | HR | RBI | SB | OPS | Counting Total |
|---|---|---|---|---|---|---|---|
| 2026-04-06 | TJ Rumfield | 1 | 1 | 2 | 0 | 1.250 | 4 |
| 2026-04-19 | Lawrence Butler | 1 | 0 | 1 | 2 | 1.267 | 4 |
| 2026-04-22 | Maikel Garcia | 2 | 0 | 1 | 1 | 0.933 | 4 |
| 2026-04-09 | Ramon Laureano | 1 | 0 | 0 | 2 | 0.800 | 3 |
| 2026-04-11 | Wyatt Langford | 1 | 1 | 1 | 0 | 1.667 | 3 |

Big Papi's biggest Quick Lineup cost is in SB — 7 stolen bases missed across the season, a category where rate stats make individual missed days more impactful at the margins. Lawrence Butler (2 SB), Ramon Laureano (2 SB), and Maikel Garcia (1 SB) were all benched on days they ran.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 19 | 17 | — |
| QS total | 4 | 7 | Manual +3 |
| QS avg/day | 0.211 | 0.412 | Manual +0.201/day |
| SVHD total | 8 | 13 | Manual +5 |
| SVHD avg/day | 0.421 | 0.765 | Manual +0.344/day |
| Season opp cost | — | — | ~3.8 QS, ~6.5 SVHD |

The largest SVHD gap in the league. Big Papi's bullpen production on Quick Lineup days is nearly half what manual days produce — losing 0.344 SVHD per day across 19 QL days adds up to roughly 6–7 missed holds/saves at the season level. Combined with the SB batting miss, this team is being hurt in three separate categories by Quick Lineup.

---

### Datalickmyballs

**Quick Lineup days:** 21 of 33 (63.6%)

| Metric | Value |
|---|---|
| Season R missed | 17 |
| Season HR missed | 2 |
| Season RBI missed | 10 |
| Season SB missed | 4 |
| **Total counting missed** | **33** |
| Avg R missed / QL day | 0.81 |
| Avg HR missed / QL day | 0.10 |
| Avg RBI missed / QL day | 0.48 |
| Avg SB missed / QL day | 0.19 |

#### 🔴 Top 5 Missed Performances (Quick Lineup days)

| Date | Player | R | HR | RBI | SB | OPS | Counting Total |
|---|---|---|---|---|---|---|---|
| 2026-04-09 | Hunter Goodman | 3 | 1 | 1 | 1 | 2.800 | 6 |
| 2026-04-05 | Gleyber Torres | 2 | 1 | 1 | 0 | 1.850 | 4 |
| 2026-04-05 | Giancarlo Stanton | 1 | 0 | 2 | 1 | 0.933 | 4 |
| 2026-04-01 | Giancarlo Stanton | 0 | 0 | 2 | 0 | 1.250 | 2 |
| 2026-04-04 | Trent Grisham | 1 | 0 | 1 | 0 | 0.600 | 2 |

Hunter Goodman's 3 R / 1 HR / 1 RBI / 1 SB (OPS 2.800) on 2026-04-09 is the single worst Quick Lineup miss in the entire league. Goodman was sitting on the bench during one of his best games of the season. Giancarlo Stanton appears twice in the top 5, suggesting a recurring slot management problem where Quick Lineup consistently misplaces him.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 20 | 16 | — |
| QS total | 13 | 8 | QL +5 |
| QS avg/day | 0.650 | 0.500 | QL +0.150/day |
| SVHD total | 15 | 13 | QL +2 |
| SVHD avg/day | 0.750 | 0.812 | Manual +0.062/day |

Datalickmyballs is one of the few teams where Quick Lineup days outperform manual days on QS — the pitching staff actually posts more quality starts per day when the algorithm sets the lineup. SVHD is essentially tied. The damage here is all on the batting side, not the mound.

---

### Dingers Only

**Quick Lineup days:** 6 of 33 (18.2%)

| Metric | Value |
|---|---|
| Season R missed | 7 |
| Season HR missed | 2 |
| Season RBI missed | 11 |
| Season SB missed | 1 |
| **Total counting missed** | **21** |
| Avg R missed / QL day | 1.17 |
| Avg HR missed / QL day | 0.33 |
| Avg RBI missed / QL day | 1.83 |
| Avg SB missed / QL day | 0.17 |

#### 🔴 Top 5 Missed Performances (Quick Lineup days)

| Date | Player | R | HR | RBI | SB | OPS | Counting Total |
|---|---|---|---|---|---|---|---|
| 2026-04-14 | Jake Burger | 2 | 2 | 4 | 0 | 2.600 | 8 |
| 2026-04-06 | Carlos Correa | 2 | 0 | 1 | 1 | 0.900 | 4 |
| 2026-04-14 | Adolis Garcia | 2 | 0 | 1 | 0 | 1.250 | 3 |
| 2026-04-20 | Xander Bogaerts | 1 | 0 | 1 | 0 | 1.250 | 2 |
| 2026-04-09 | Mark Vientos | 0 | 0 | 1 | 0 | 0.000 | 1 |

Dingers Only uses Quick Lineup least frequently of the heavy-impact teams, but when it fires it causes real damage. The 2026-04-14 Jake Burger game — 2 HR, 4 RBI, 2.600 OPS — is the single biggest missed performance in the entire league this season. On the same day Adolis Garcia also went 2 R / 1 RBI from the bench, meaning Quick Lineup benched two productive players simultaneously. That single day cost 11 counting stats.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 6 | 30 | — |
| QS total | 3 | 10 | — |
| QS avg/day | 0.500 | 0.333 | QL +0.167/day |
| SVHD total | 5 | 19 | — |
| SVHD avg/day | 0.833 | 0.633 | QL +0.200/day |

With only 6 Quick Lineup days the sample is thin, but both pitching stats favor QL days. The predominantly manual approach is working across all dimensions — batting misses are 21 counting stats across just 6 QL days (3.5/day), while the pitching side shows no Quick Lineup penalty.

---

### Long Bohms Away

**Quick Lineup days:** 1 of 33 (3.0%)

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

Almost entirely manual. The one Quick Lineup day (2026-04-16) produced zero bench stat output — all benched players had no plate appearances, so no production was missed.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 1 | 32 | — |
| QS total | 0 | 10 | — |
| QS avg/day | 0.000 | 0.312 | (1 QL day — not comparable) |
| SVHD total | 2 | 19 | — |
| SVHD avg/day | 2.000 | 0.594 | (1 QL day — not comparable) |

One Quick Lineup day is insufficient for rate comparison. The 2 SVHD on that single QL day is a small-sample outlier. Long Bohms Away's pitching performance is essentially entirely manual and performing well at 0.312 QS/day and 0.594 SVHD/day.

---

### Midnight Muncy's

**Quick Lineup days:** 21 of 33 (63.6%)

| Metric | Value |
|---|---|
| Season R missed | 0 |
| Season HR missed | 0 |
| Season RBI missed | 1 |
| Season SB missed | 0 |
| **Total counting missed** | **1** |
| Avg R missed / QL day | 0.00 |
| Avg HR missed / QL day | 0.00 |
| Avg RBI missed / QL day | 0.05 |
| Avg SB missed / QL day | 0.00 |

#### ✅ Top Bench Performances on Quick Lineup Days (effectively none)

| Date | Player | R | HR | RBI | SB | OPS | Counting Total |
|---|---|---|---|---|---|---|---|
| 2026-03-29 | Kyle Manzardo | 0 | 0 | 1 | 0 | 0.400 | 1 |
| 2026-03-29 | Spencer Steer | 0 | 0 | 0 | 0 | 0.200 | 0 |
| 2026-04-23 | Juan Soto | 0 | 0 | 0 | 0 | 0.833 | 0 |

**The benchmark team.** Midnight Muncy's uses Quick Lineup on 63.6% of days — tied for first in the league — and loses essentially nothing. One RBI across 21 Quick Lineup days. This is what optimal Quick Lineup usage looks like: a deep roster with clear starter/bench separations, where the algorithm has enough signal to put the right players in every day. Juan Soto had an 0.833 OPS in a bench appearance on 2026-04-23 but produced zero counting stats — even the misses are low-cost.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 20 | 16 | — |
| QS total | 7 | 9 | Manual +2 |
| QS avg/day | 0.350 | 0.562 | Manual +0.213/day |
| SVHD total | 15 | 12 | QL +3 |
| SVHD avg/day | 0.750 | 0.750 | Tied |

A slight QS edge for manual days, but SVHD is exactly tied. Unlike batting where Midnight Muncy's is essentially lossless, Quick Lineup does suppress quality starts somewhat — 4.3 fewer QS over the course of the season at the current rate gap. Not a crisis, but it shows even the benchmark team has room to improve on the pitching side.

---

### Shohei Me the Money

**Quick Lineup days:** 2 of 33 (6.1%)

| Metric | Value |
|---|---|
| Season R missed | 2 |
| Season HR missed | 0 |
| Season RBI missed | 2 |
| Season SB missed | 0 |
| **Total counting missed** | **4** |
| Avg R missed / QL day | 1.00 |
| Avg HR missed / QL day | 0.00 |
| Avg RBI missed / QL day | 1.00 |
| Avg SB missed / QL day | 0.00 |

#### 🔴 Top 5 Missed Performances (Quick Lineup days)

| Date | Player | R | HR | RBI | SB | OPS | Counting Total |
|---|---|---|---|---|---|---|---|
| 2026-04-15 | Ernie Clement | 1 | 0 | 1 | 0 | 0.400 | 2 |
| 2026-03-29 | Ernie Clement | 0 | 0 | 1 | 0 | 0.667 | 1 |
| 2026-03-29 | Willi Castro | 1 | 0 | 0 | 0 | 0.500 | 1 |
| 2026-03-29 | Heliot Ramos | 0 | 0 | 0 | 0 | 0.833 | 0 |
| 2026-04-15 | Willi Castro | 0 | 0 | 0 | 0 | 0.000 | 0 |

Very low Quick Lineup usage minimizes the damage. Ernie Clement appears in both QL days — a depth piece being benched rather than a star, keeping the impact low.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 2 | 34 | — |
| QS total | 2 | 12 | — |
| QS avg/day | 1.000 | 0.353 | (2 QL days — not comparable) |
| SVHD total | 2 | 22 | — |
| SVHD avg/day | 1.000 | 0.647 | (2 QL days — not comparable) |

Two Quick Lineup days is too small a sample to draw conclusions. The 1.000 QS/day and 1.000 SVHD/day on QL days are coincidental. Shohei Me the Money's pitching production is essentially entirely manual and running at a healthy 0.353 QS/day, 0.647 SVHD/day.

---

### Skubal Snacks

**Quick Lineup days:** 11 of 33 (33.3%)

| Metric | Value |
|---|---|
| Season R missed | 4 |
| Season HR missed | 1 |
| Season RBI missed | 7 |
| Season SB missed | 3 |
| **Total counting missed** | **15** |
| Avg R missed / QL day | 0.36 |
| Avg HR missed / QL day | 0.09 |
| Avg RBI missed / QL day | 0.64 |
| Avg SB missed / QL day | 0.27 |

#### 🔴 Top 5 Missed Performances (Quick Lineup days)

| Date | Player | R | HR | RBI | SB | OPS | Counting Total |
|---|---|---|---|---|---|---|---|
| 2026-03-27 | Carson Benge | 2 | 1 | 1 | 1 | 1.933 | 5 |
| 2026-04-08 | Matt McLain | 1 | 0 | 2 | 1 | 1.200 | 4 |
| 2026-03-29 | Owen Caissie | 0 | 0 | 1 | 1 | 1.750 | 2 |
| 2026-03-29 | Nolan Gorman | 0 | 0 | 1 | 0 | 0.500 | 1 |
| 2026-04-06 | Kyle Tucker | 0 | 0 | 1 | 0 | 0.000 | 1 |

Carson Benge's opening-week performance (5 counting stats, 1.933 OPS) while sitting the bench on a Quick Lineup day is particularly costly — that was scoring period 2 and a large chunk of the season's total missed SB came from Benge and McLain. Kyle Tucker benched on 2026-04-06 is the headline miss: a projected top-10 hitter sitting while producing.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 11 | 25 | — |
| QS total | 6 | 10 | — |
| QS avg/day | 0.545 | 0.400 | QL +0.145/day |
| SVHD total | 6 | 17 | — |
| SVHD avg/day | 0.545 | 0.680 | Manual +0.135/day |

Mixed pitching picture: Quick Lineup days show slightly more QS, but manual days outperform on SVHD. Net effect is close to neutral — the real cost for Skubal Snacks is on the batting side where bench production is being missed, not the pitching configuration.

---

### This Sh!t is Bazzana

**Quick Lineup days:** 9 of 33 (27.3%)

| Metric | Value |
|---|---|
| Season R missed | 3 |
| Season HR missed | 0 |
| Season RBI missed | 2 |
| Season SB missed | 0 |
| **Total counting missed** | **5** |
| Avg R missed / QL day | 0.33 |
| Avg HR missed / QL day | 0.00 |
| Avg RBI missed / QL day | 0.22 |
| Avg SB missed / QL day | 0.00 |

#### 🔴 Top 5 Missed Performances (Quick Lineup days)

| Date | Player | R | HR | RBI | SB | OPS | Counting Total |
|---|---|---|---|---|---|---|---|
| 2026-04-19 | Luis Garcia Jr. | 0 | 0 | 2 | 0 | 0.667 | 2 |
| 2026-04-08 | Mauricio Dubon | 1 | 0 | 0 | 0 | 1.250 | 1 |
| 2026-04-13 | Jac Caglianone | 1 | 0 | 0 | 0 | 0.750 | 1 |
| 2026-04-23 | Bo Bichette | 1 | 0 | 0 | 0 | 0.750 | 1 |
| 2026-04-06 | Byron Buxton | 0 | 0 | 0 | 0 | 0.000 | 0 |

Modest total impact. Bo Bichette benched on 2026-04-23 is the notable name — a top-tier SS who scored but produced only 1 R. Byron Buxton benched on 2026-04-06 produced nothing on that day, limiting the damage.

#### Pitching (Active Slots): QS and SVHD

| Metric | Quick Lineup | Manual | Gap |
|---|---|---|---|
| Days | 9 | 24 | — |
| QS total | 2 | 18 | Manual +16 |
| QS avg/day | 0.222 | 0.750 | Manual +0.528/day |
| SVHD total | 4 | 15 | Manual +11 |
| SVHD avg/day | 0.444 | 0.625 | Manual +0.181/day |
| Season opp cost | — | — | ~4.8 QS, ~1.6 SVHD |

The worst pitching gap in the league. On Quick Lineup days, This Sh!t is Bazzana's active pitchers post just 0.222 QS/day — less than a third of the 0.750/day rate on manual days. The 0.528/day QS gap across 9 QL days translates to roughly 5 missed Quality Starts at the season level. Combined with a small batting miss, the biggest opportunity cost for this team is entirely on the pitching side: more frequent manual lineup setting would be the highest-leverage change they can make.

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

This is why you see cases like Jake Burger (2 HR, 4 RBI, 2.600 OPS) sitting the bench: his ESPN ranking on that day placed him below the active batters in the greedy pass, and the algorithm moved on without reconsidering. A full optimizer would have caught it; a greedy ranker doesn't.

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
Final check: every benched player either has no game today, or was explicitly ranked below the player in their slot in step 3. If any bench player with a game ranks above an active player at a compatible slot, swap them. This catches the greedy-algorithm failure mode directly.

The key difference: steps 3 and 5 give your lineup **category awareness** that Quick Lineup structurally cannot provide. That's what closes the gap between the 37 counting stats Big Dumpers left on the bench and the 1 RBI that Midnight Muncy's left — the latter's roster is deep enough that the greedy algorithm works by accident. For everyone else, manual category-aware decisions are the edge.

---

*Batting data through scoring period 33 (Apr 27, 2026). Pitching (QS/SVHD) data through scoring period 36 (Apr 30, 2026). Analysis source: [`analyze_quick_lineup_impact.py`](https://github.com/pjrigali/acn_repo/blob/main/fantasy_baseball/analyze_quick_lineup_impact.py)*

*[Home](https://pjrigali.github.io)*

*Last updated: 2026-04-30*
