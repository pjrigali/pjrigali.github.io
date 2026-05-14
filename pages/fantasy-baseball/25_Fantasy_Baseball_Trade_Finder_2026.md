---
layout: default
title: "25_Fantasy Baseball Mutually Beneficial Trade Finder 2026"
description: A systematic scan of every roster in the 10-team ESPN H2H 5x5 league to surface 1-for-1 player swaps where both teams improve their projected category rank standings.
permalink: /fantasy-baseball/trade-finder-2026
parent: Fantasy Baseball
nav_order: 12
---

# ⚾ Mutually Beneficial Trade Finder — 2026

*Which trades help both teams? A full-league category simulation that surfaces every 1-for-1 swap where neither side loses ground.*

---

## Project Overview

Most trade analysis is reactive — you receive an offer and evaluate it. This tool flips the question: given every roster in the league, which player swaps could both teams realistically agree to?

The finder scans all 45 team pairs, enumerates every 1-for-1 same-type swap (batter-for-batter or pitcher-for-pitcher), simulates the resulting category standings for all 10 teams, and keeps only trades where **both** sides net-improve — more categories gained than lost.

266 mutually beneficial trades were identified across the league as of **May 13, 2026**.

Trades are reported in two tiers per team:
- **Most Balanced** — sorted to maximize the minimum gain on either side, minimizing the fairness gap between teams
- **Highest Impact** — the top 2 trades by combined category swing (one side may gain more, but both still benefit)

---

## Scoring System

This is a **Head-to-Head Each Category** league. Each week a team wins, loses, or ties each of the 10 categories independently against one opponent. Category rank across the league (1 = best, 10 = worst) determines how often you win that category week-to-week.

| Side | Category | Type | Note |
|------|----------|------|------|
| Batting | R | Counting | Runs scored |
| Batting | HR | Counting | Home runs |
| Batting | RBI | Counting | Runs batted in |
| Batting | SB | Counting | Stolen bases |
| Batting | OPS | Rate | OBP + SLG |
| Pitching | K/9 | Rate | (K × 9) / IP |
| Pitching | QS | Counting | Quality starts |
| Pitching | SVHD | Counting | Saves + holds |
| Pitching | ERA | Rate | Lower is better |
| Pitching | WHIP | Rate | Lower is better |

---

## Data Sources

| File | Contents |
|------|----------|
| `stats_espn_daily_2026.csv` | Per-player per-day stats and roster assignments for all 10 teams (Mar 26 – May 13, 2026) |
| `activity_espn_season_2026.csv` | Every add, drop, and trade since Opening Day — used to confirm current roster membership |
| `player_batter_projections_2026.csv` | Full-season batter projections (R, HR, RBI, SB, OPS components) |
| `player_pitcher_projections_2026.csv` | Full-season pitcher projections (K, IP, ER, H, BB, GS, SV) |

---

## Methodology

### 1. Current roster validation

Player roster membership is confirmed via `activity_espn_season_2026.csv`, not just the daily stats file. A player whose most recent activity is `DROPPED` with no later `FA ADDED` is excluded as a free agent. This removed 102 dropped players from the analysis who still appeared in the daily stats history.

### 2. YTD category aggregation

For each team, batting and pitching stats are summed across all active lineup slots (bench and IL excluded). Rate stats are computed from underlying counting components — never by averaging the pre-calculated rate column:

- **OPS** = (H + BB + HBP) / (AB + BB + HBP + SF) + TB / AB
- **ERA** = (ER × 9) / IP
- **WHIP** = (H + BB) / IP
- **K/9** = (K × 9) / IP
- **SVHD** = SV + HLD

### 3. Player projection vectors

Each rostered player is mapped to a full-season projection. Name matching normalizes `\xa0` separators, strips parenthetical team/position suffixes (e.g. `(LAD - SP,DH)`), and flattens Unicode accents. 276 of 279 active trade candidates matched a projection (3 fell back to YTD stats scaled to full-season equivalent at ×3.9).

Pitcher projections derive QS as 65% of GS and use SV as the SVHD floor (holds are not included in the projection file).

### 4. Team projected totals

Full-season projections are summed across all non-IL rostered players per team to produce projected category totals. For rate stats, underlying components are summed first, then the rate is computed — same approach as the YTD aggregation.

### 5. Trade simulation

For each of the 34,526 same-type swaps evaluated:

1. Remove Player X's projection vector from Team A's aggregate; add Player Y's
2. Remove Player Y's projection vector from Team B's aggregate; add Player X's
3. Recompute category stats for both affected teams
4. Re-rank all 10 teams across all 10 categories
5. Count category rank improvements and worsenings for each side

**A trade is mutually beneficial when both teams net-improve** (categories gained > categories lost).

### 6. Trade scoring and fairness

Trades are evaluated on two axes:

- **Combined net** — total categories gained across both teams (higher = more value created)
- **Balance** — how evenly the gain is split. Sorted by `min(team_a_net, team_b_net)` descending then gap ascending. A +2/+2 trade ranks above a +3/+1 even though the combined score is the same.

---

## Projected Category Standings

*Full-season projections, rank 1 = best in league. As of May 13, 2026.*

| Team | R | HR | RBI | SB | OPS | K/9 | QS | SVHD | ERA | WHIP | Total |
|------|---|----|----|-----|-----|-----|-----|------|-----|------|-------|
| This Schlitt is Bazzanas | 2 | 1 | 2 | 5 | 3 | 2 | 4 | 10 | 5 | 3 | 37 |
| Welcome to the JUNGle | 1 | 2 | 1 | 10 | 4 | 6 | 5 | 9 | 3 | 2 | 43 |
| Shohei Me the Money | 4 | 6 | 5 | 3 | 9 | 1 | 8 | 4 | 1 | 4 | 45 |
| Datalickmyballs | 3 | 3 | 3 | 7 | 5 | 10 | 9 | 2 | 2 | 6 | 50 |
| Dingers Only | 8 | 7 | 7 | 4 | 7 | 5 | 1 | 1 | 6 | 8 | 54 |
| Midnight Muncy's | 7 | 8 | 8 | 1 | 8 | 3 | 7 | 8 | 4 | 1 | 55 |
| Big Dumpers | 6 | 4 | 4 | 8 | 6 | 9 | 2 | 6 | 10 | 5 | 60 |
| All Rise | 10 | 9 | 10 | 2 | 2 | 7 | 3 | 3 | 7 | 7 | 60 |
| Skubal Snacks | 5 | 5 | 6 | 6 | 1 | 4 | 10 | 7 | 8 | 10 | 62 |
| Rock and Aroldis | 9 | 10 | 9 | 9 | 10 | 8 | 6 | 5 | 9 | 9 | 84 |

*Lower total = better overall standing. This Schlitt leads on projections; Rock and Aroldis has the most ground to make up.*

---

## Team Category Profiles

*Strengths and weaknesses for each team based on projected full-season category rankings. Trade targets are categories ranked 7–10 where improvement is most achievable.*

---

### All Rise
**Strengths:** SB (#2), OPS (#2), QS (#3), SVHD (#3)
**Weaknesses:** R (#10), RBI (#10), HR (#9)

All Rise is the rare team that wins pitching saves *and* batting rate (OPS) but gets almost no run production. Their R and RBI ranks are last in the league. The profile suggests a roster full of contact/OBP hitters who don't drive in runs — or a weak middle-of-the-order. **Priority: trade speed/saves surplus for run-producing power bats.**

---

### Big Dumpers
**Strengths:** QS (#2), HR (#4), RBI (#4)
**Weaknesses:** ERA (#10), K/9 (#9), SB (#8)

Big Dumpers has excellent starting pitching volume (QS) and decent power, but their relievers are destroying their ERA and K/9 averages. SB is also a clear hole. **Priority: swap a high-ERA reliever for a K-heavy arm; look for speed-first batters in trades.**

---

### Datalickmyballs
**Strengths:** SVHD (#2), ERA (#2), R (#3), HR (#3), RBI (#3)
**Weaknesses:** K/9 (#10), QS (#9), SB (#7)

One of the most lopsided profiles in the league — dominant in every offensive category and saves/ERA, but essentially non-competitive in starting pitcher categories. Their bullpen is elite but their rotation is thin. **Priority: trade batter depth or a reliever for a high-QS, high-K/9 starter.**

---

### Dingers Only
**Strengths:** QS (#1), SVHD (#1)
**Weaknesses:** R (#8), HR (#7), RBI (#7), OPS (#7), WHIP (#8)

The strongest pitching team in the league by QS and SVHD but among the weakest in batting across the board. They have significant pitching depth to offer. **Priority: trade a starter or reliever for an impact bat that improves R/HR/RBI — a power hitter with solid OBP is the target.**

---

### Midnight Muncy's
**Strengths:** SB (#1), WHIP (#1), K/9 (#3), ERA (#4)
**Weaknesses:** HR (#8), RBI (#8), OPS (#8), SVHD (#8)

Elite in pitching ratios and speed but struggling badly in power and the bullpen save category. Their pitching is genuinely tradeable — their K/9 and WHIP are top-3 in the league. **Priority: trade a K/WHIP starter for an HR/RBI producer; a closer for a power bat.**

---

### Rock and Aroldis
**Strengths:** None above #6 (QS: #6, SVHD: #5)
**Weaknesses:** HR (#10), OPS (#10), R (#9), RBI (#9), ERA (#9), WHIP (#9), SB (#9), K/9 (#8)

The most distressed roster in the league — bottom-3 in 8 of 10 categories. The clearest path forward is **high combined-impact trades** — swapping any player that has slight value for someone who dramatically improves multiple categories simultaneously. Even a +1/+3 trade is acceptable given how much ground needs to be made up.

---

### Shohei Me the Money
**Strengths:** K/9 (#1), ERA (#1), SVHD (#4), SB (#3)
**Weaknesses:** OPS (#9), QS (#8), HR (#6)

Best pitching ratios in the league by a wide margin. The weakness is entirely on the offensive side — especially OPS and home run production. **Priority: trade a K-heavy reliever or K/9 pitcher for an OPS or power bat; acquiring starts (QS) would also help.**

---

### Skubal Snacks
**Strengths:** OPS (#1), K/9 (#4)
**Weaknesses:** QS (#10), WHIP (#10), ERA (#8), SVHD (#7)

Best batting OPS in the league and solid strikeout rate, but the rotation is the worst in the league by QS and WHIP. Their hitting depth is real trade capital. **Priority: trade an elite bat for a durable starter with strong WHIP and QS upside.**

---

### This Schlitt is Bazzanas
**Strengths:** HR (#1), K/9 (#2), R (#2), RBI (#2), OPS (#3), WHIP (#3)
**Weaknesses:** SVHD (#10), QS (#4 — approaching weakness)

The league's best offensive team and a top-2 pitching strikeout squad. The single glaring hole is saves/holds — ranked last in the league. They can afford to trade from their pitching depth. **Priority: trade a starting pitcher for a closer or reliever with saves+holds upside.**

---

### Welcome to the JUNGle
**Strengths:** R (#1), RBI (#1), HR (#2), WHIP (#2), ERA (#3)
**Weaknesses:** SB (#10), SVHD (#9)

The top run-producing team in the league with elite pitching ratios, but completely lacking in stolen bases and saves. They have significant power bat depth to offer. **Priority: trade a power hitter for a speed-first bat; trade a starter for a closer to address SVHD.**

---

## Top Trades by Team

*Top 5 most balanced mutually beneficial trades per team plus the 1–2 highest combined-impact trades. Rank shown as before→after (1=best).*

---

### All Rise

*Strengths: SB (2), OPS (2), QS (3), SVHD (3) — Weaknesses: R (10), RBI (10), HR (9)*

**Most Balanced Trades**

**1. Give Mike Trout → get Brice Turang** *(from Welcome to the JUNGle)* — combined +4
- Mike Trout projections: R:68  HR:25  RBI:68  SB:3  OPS:0.797
- Brice Turang projections: R:79  HR:14  RBI:65  SB:29  OPS:0.713
- All Rise gains: R 10→9, SB 2→1 — net **+2**
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**

**2. Give Munetaka Murakami → get Brice Turang** *(from Welcome to the JUNGle)* — combined +4
- Munetaka Murakami projections: R:69  HR:27  RBI:72  SB:9  OPS:0.755
- Brice Turang projections: R:79  HR:14  RBI:65  SB:29  OPS:0.713
- All Rise gains: R 10→9, SB 2→1 — net **+2**
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**

**3. Give Riley O'Brien → get Michael King** *(from This Schlitt is Bazzanas)* — combined +2
- Riley O'Brien projections: K/9:9.2  QS:0  SVHD:16  ERA:3.668  WHIP:1.301
- Michael King projections: K/9:9.4  QS:20  SVHD:0  ERA:3.831  WHIP:1.234
- All Rise gains: K/9 7→6, QS 3→2 — loses SVHD 3→5 — net **+1**
- This Schlitt is Bazzanas gains: SVHD 10→9, ERA 5→4 — loses QS 4→9 — net **+1**

**4. Give Riley O'Brien → get Edward Cabrera** *(from This Schlitt is Bazzanas)* — combined +2
- Riley O'Brien projections: K/9:9.2  QS:0  SVHD:16  ERA:3.668  WHIP:1.301
- Edward Cabrera projections: K/9:9.7  QS:17  SVHD:0  ERA:3.876  WHIP:1.241
- All Rise gains: K/9 7→5, QS 3→2 — loses SVHD 3→5 — net **+1**
- This Schlitt is Bazzanas gains: SVHD 10→9, ERA 5→4 — loses QS 4→9 — net **+1**

**5. Give Aaron Judge → get Jose Ramirez** *(from Shohei Me the Money)* — combined +2
- Aaron Judge projections: R:110  HR:46  RBI:113  SB:9  OPS:1.028
- Jose Ramirez projections: R:91  HR:27  RBI:89  SB:33  OPS:0.825
- All Rise gains: SB 2→1 — net **+1**
- Shohei Me the Money gains: OPS 9→8 — net **+1**

**Highest Impact Trades**

**1. Give Julio Rodriguez → get Bryce Harper** *(from Datalickmyballs)* — combined +4
- Julio Rodriguez projections: R:93  HR:29  RBI:93  SB:26  OPS:0.794
- Bryce Harper projections: R:84  HR:27  RBI:88  SB:10  OPS:0.850
- All Rise gains: OPS 2→1 — net **+1**
- Datalickmyballs gains: R 3→2, HR 3→2, SB 7→4 — net **+3**

**2. Give Elly De La Cruz → get Jazz Chisholm Jr.** *(from Datalickmyballs)* — combined +4
- Elly De La Cruz projections: R:94  HR:24  RBI:82  SB:40  OPS:0.793
- Jazz Chisholm Jr. projections: R:79  HR:28  RBI:80  SB:31  OPS:0.758
- All Rise gains: HR 9→8 — net **+1**
- Datalickmyballs gains: R 3→2, SB 7→6, OPS 5→4 — net **+3**

---

### Big Dumpers

*Strengths: QS (2), HR (4), RBI (4) — Weaknesses: ERA (10), K/9 (9), SB (8)*

**Most Balanced Trades**

**1. Give Robert Suarez → get Drew Rasmussen** *(from This Schlitt is Bazzanas)* — combined +2
- Robert Suarez projections: K/9:9.4  QS:0  SVHD:9  ERA:3.568  WHIP:1.175
- Drew Rasmussen projections: K/9:8.0  QS:20  SVHD:0  ERA:3.623  WHIP:1.176
- Big Dumpers gains: QS 2→1, ERA 10→9 — loses SVHD 6→7 — net **+1**
- This Schlitt is Bazzanas gains: K/9 2→1, SVHD 10→9 — loses QS 4→9 — net **+1**

**2. Give Cade Smith → get Chris Sale** *(from Datalickmyballs)* — combined +2
- Cade Smith projections: K/9:11.6  QS:0  SVHD:31  ERA:2.911  WHIP:1.069
- Chris Sale projections: K/9:11.0  QS:18  SVHD:0  ERA:3.253  WHIP:1.097
- Big Dumpers gains: ERA 10→9, WHIP 5→4 — loses SVHD 6→8 — net **+1**
- Datalickmyballs gains: SVHD 2→1 — net **+1**

**3. Give Matt Olson → get Bryce Harper** *(from Datalickmyballs)* — combined +2
- Matt Olson projections: R:89  HR:30  RBI:92  SB:1  OPS:0.806
- Bryce Harper projections: R:84  HR:27  RBI:88  SB:10  OPS:0.850
- Big Dumpers gains: SB 8→6 — net **+1**
- Datalickmyballs gains: R 3→2, HR 3→1 — loses SB 7→9 — net **+1**

**4. Give Spencer Torkelson → get Alex Bregman** *(from Datalickmyballs)* — combined +2
- Spencer Torkelson projections: R:76  HR:27  RBI:82  SB:2  OPS:0.755
- Alex Bregman projections: R:81  HR:22  RBI:78  SB:2  OPS:0.754
- Big Dumpers gains: R 6→5 — net **+1**
- Datalickmyballs gains: HR 3→1 — net **+1**

**5. Give Riley Greene → get Shea Langeliers** *(from Datalickmyballs)* — combined +2
- Riley Greene projections: R:82  HR:28  RBI:90  SB:4  OPS:0.794
- Shea Langeliers projections: R:69  HR:28  RBI:78  SB:6  OPS:0.798
- Big Dumpers gains: SB 8→7 — net **+1**
- Datalickmyballs gains: R 3→2, RBI 3→2 — loses SB 7→8 — net **+1**

**Highest Impact Trades**

**1. Give Spencer Torkelson → get George Springer** *(from Datalickmyballs)* — combined +3
- Spencer Torkelson projections: R:76  HR:27  RBI:82  SB:2  OPS:0.755
- George Springer projections: R:83  HR:24  RBI:73  SB:14  OPS:0.784
- Big Dumpers gains: R 6→5, SB 8→6 — net **+2**
- Datalickmyballs gains: HR 3→1, RBI 3→2 — loses SB 7→10 — net **+1**

**2. Give Nolan Arenado → get Brandon Marsh** *(from Datalickmyballs)* — combined +3
- Nolan Arenado projections: R:59  HR:15  RBI:67  SB:3  OPS:0.696
- Brandon Marsh projections: R:57  HR:13  RBI:53  SB:11  OPS:0.744
- Big Dumpers gains: SB 8→6 — net **+1**
- Datalickmyballs gains: R 3→2, HR 3→2, RBI 3→2 — loses SB 7→9 — net **+2**

---

### Datalickmyballs

*Strengths: SVHD (2), ERA (2), R (3), HR (3), RBI (3) — Weaknesses: K/9 (10), QS (9), SB (7)*

**Most Balanced Trades**

**1. Give Bryce Harper → get Jackson Chourio** *(from Welcome to the JUNGle)* — combined +4
- Bryce Harper projections: R:84  HR:27  RBI:88  SB:10  OPS:0.850
- Jackson Chourio projections: R:87  HR:23  RBI:83  SB:24  OPS:0.777
- Datalickmyballs gains: R 3→2, SB 7→4 — net **+2**
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**

**2. Give Shea Langeliers → get Willy Adames** *(from Welcome to the JUNGle)* — combined +4
- Shea Langeliers projections: R:69  HR:28  RBI:78  SB:6  OPS:0.798
- Willy Adames projections: R:82  HR:26  RBI:83  SB:11  OPS:0.733
- Datalickmyballs gains: R 3→2, SB 7→6 — net **+2**
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**

**3. Give Hunter Goodman → get Willy Adames** *(from Welcome to the JUNGle)* — combined +4
- Hunter Goodman projections: R:69  HR:28  RBI:84  SB:2  OPS:0.791
- Willy Adames projections: R:82  HR:26  RBI:83  SB:11  OPS:0.733
- Datalickmyballs gains: R 3→2, SB 7→6 — net **+2**
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**

**4. Give Gavin Williams → get Cam Schlittler** *(from This Schlitt is Bazzanas)* — combined +2
- Gavin Williams projections: K/9:9.2  QS:20  SVHD:0  ERA:3.958  WHIP:1.301
- Cam Schlittler projections: K/9:9.1  QS:16  SVHD:0  ERA:4.043  WHIP:1.284
- Datalickmyballs gains: WHIP 6→5 — net **+1**
- This Schlitt is Bazzanas gains: QS 4→3 — net **+1**

**5. Give Gavin Williams → get Kris Bubic** *(from This Schlitt is Bazzanas)* — combined +2
- Gavin Williams projections: K/9:9.2  QS:20  SVHD:0  ERA:3.958  WHIP:1.301
- Kris Bubic projections: K/9:8.8  QS:16  SVHD:0  ERA:3.761  WHIP:1.254
- Datalickmyballs gains: WHIP 6→4 — net **+1**
- This Schlitt is Bazzanas gains: QS 4→3 — net **+1**

**Highest Impact Trades**

**1. Give Bryce Harper → get Julio Rodriguez** *(from All Rise)* — combined +4
- Bryce Harper projections: R:84  HR:27  RBI:88  SB:10  OPS:0.850
- Julio Rodriguez projections: R:93  HR:29  RBI:93  SB:26  OPS:0.794
- Datalickmyballs gains: R 3→2, HR 3→2, SB 7→4 — net **+3**
- All Rise gains: OPS 2→1 — net **+1**

**2. Give Jazz Chisholm Jr. → get Elly De La Cruz** *(from All Rise)* — combined +4
- Jazz Chisholm Jr. projections: R:79  HR:28  RBI:80  SB:31  OPS:0.758
- Elly De La Cruz projections: R:94  HR:24  RBI:82  SB:40  OPS:0.793
- Datalickmyballs gains: R 3→2, SB 7→6, OPS 5→4 — net **+3**
- All Rise gains: HR 9→8 — net **+1**

---

### Dingers Only

*Strengths: QS (1), SVHD (1) — Weaknesses: R (8), HR (7), RBI (7), OPS (7), WHIP (8)*

**Most Balanced Trades**

**1. Give Clay Holmes → get Cam Schlittler** *(from This Schlitt is Bazzanas)* — combined +2
- Clay Holmes projections: K/9:7.3  QS:18  SVHD:0  ERA:3.955  WHIP:1.345
- Cam Schlittler projections: K/9:9.1  QS:16  SVHD:0  ERA:4.043  WHIP:1.284
- Dingers Only gains: K/9 5→3 — net **+1**
- This Schlitt is Bazzanas gains: QS 4→3, ERA 5→4 — loses K/9 2→4 — net **+1**

**2. Give Abner Uribe → get Jeremiah Estrada** *(from This Schlitt is Bazzanas)* — combined +2
- Abner Uribe projections: K/9:10.6  QS:0  SVHD:16  ERA:3.112  WHIP:1.203
- Jeremiah Estrada projections: K/9:12.3  QS:0  SVHD:2  ERA:3.296  WHIP:1.155
- Dingers Only gains: K/9 5→4 — net **+1**
- This Schlitt is Bazzanas gains: SVHD 10→9, ERA 5→4 — loses K/9 2→3 — net **+1**

**3. Give Raisel Iglesias → get Trevor Megill** *(from Shohei Me the Money)* — combined +2
- Raisel Iglesias projections: K/9:9.7  QS:0  SVHD:27  ERA:3.621  WHIP:1.133
- Trevor Megill projections: K/9:11.1  QS:0  SVHD:19  ERA:3.462  WHIP:1.169
- Dingers Only gains: K/9 5→4 — net **+1**
- Shohei Me the Money gains: SVHD 4→3 — net **+1**

**4. Give Vinnie Pasquantino → get Shea Langeliers** *(from Datalickmyballs)* — combined +2
- Vinnie Pasquantino projections: R:75  HR:27  RBI:92  SB:1  OPS:0.785
- Shea Langeliers projections: R:69  HR:28  RBI:78  SB:6  OPS:0.798
- Dingers Only gains: OPS 7→6 — net **+1**
- Datalickmyballs gains: R 3→2, RBI 3→2 — loses SB 7→8 — net **+1**

**5. Give Austin Riley → get Shea Langeliers** *(from Datalickmyballs)* — combined +2
- Austin Riley projections: R:83  HR:28  RBI:87  SB:3  OPS:0.785
- Shea Langeliers projections: R:69  HR:28  RBI:78  SB:6  OPS:0.798
- Dingers Only gains: OPS 7→6 — net **+1**
- Datalickmyballs gains: R 3→2, RBI 3→2 — loses SB 7→8 — net **+1**

**Highest Impact Trades**

**1. Give Cristopher Sanchez → get Brandon Woodruff** *(from Midnight Muncy's)* — combined +3
- Cristopher Sanchez projections: K/9:8.8  QS:20  SVHD:0  ERA:3.161  WHIP:1.136
- Brandon Woodruff projections: K/9:9.5  QS:18  SVHD:0  ERA:3.753  WHIP:1.128
- Dingers Only gains: K/9 5→4 — net **+1**
- Midnight Muncy's gains: QS 7→6, ERA 4→2 — net **+2**

**2. Give Clay Holmes → get Bryce Elder** *(from Rock and Aroldis)* — combined +3
- Clay Holmes projections: K/9:7.3  QS:18  SVHD:0  ERA:3.955  WHIP:1.345
- Bryce Elder projections: K/9:7.4  QS:11  SVHD:0  ERA:4.496  WHIP:1.364
- Dingers Only gains: K/9 5→4 — net **+1**
- Rock and Aroldis gains: QS 6→3, ERA 9→8 — net **+2**

---

### Midnight Muncy's

*Strengths: SB (1), WHIP (1), K/9 (3), ERA (4) — Weaknesses: HR (8), RBI (8), OPS (8), SVHD (8)*

**Most Balanced Trades**

**1. Give Lucas Erceg → get Drew Rasmussen** *(from This Schlitt is Bazzanas)* — combined +2
- Lucas Erceg projections: K/9:8.5  QS:0  SVHD:3  ERA:3.685  WHIP:1.276
- Drew Rasmussen projections: K/9:8.0  QS:20  SVHD:0  ERA:3.623  WHIP:1.176
- Midnight Muncy's gains: QS 7→2 — net **+1**
- This Schlitt is Bazzanas gains: K/9 2→1, SVHD 10→9 — loses QS 4→9 — net **+1**

**2. Give Brandon Woodruff → get Framber Valdez** *(from Shohei Me the Money)* — combined +2
- Brandon Woodruff projections: K/9:9.5  QS:18  SVHD:0  ERA:3.753  WHIP:1.128
- Framber Valdez projections: K/9:8.3  QS:20  SVHD:0  ERA:3.478  WHIP:1.228
- Midnight Muncy's gains: QS 7→6, ERA 4→3 — loses WHIP 1→2 — net **+1**
- Shohei Me the Money gains: WHIP 4→3 — net **+1**

**3. Give Miguel Vargas → get Alex Bregman** *(from Datalickmyballs)* — combined +2
- Miguel Vargas projections: R:69  HR:17  RBI:64  SB:8  OPS:0.717
- Alex Bregman projections: R:81  HR:22  RBI:78  SB:2  OPS:0.754
- Midnight Muncy's gains: HR 8→7 — net **+1**
- Datalickmyballs gains: SB 7→6 — net **+1**

**4. Give Yoshinobu Yamamoto → get Logan Webb** *(from Datalickmyballs)* — combined +2
- Yoshinobu Yamamoto projections: K/9:9.9  QS:18  SVHD:0  ERA:3.247  WHIP:1.114
- Logan Webb projections: K/9:8.5  QS:21  SVHD:0  ERA:3.273  WHIP:1.167
- Midnight Muncy's gains: QS 7→6 — net **+1**
- Datalickmyballs gains: WHIP 6→5 — net **+1**

**5. Give Samuel Basallo → get Colson Montgomery** *(from Datalickmyballs)* — combined +2
- Samuel Basallo projections: R:49  HR:18  RBI:55  SB:3  OPS:0.743
- Colson Montgomery projections: R:64  HR:23  RBI:72  SB:3  OPS:0.688
- Midnight Muncy's gains: HR 8→7 — net **+1**
- Datalickmyballs gains: OPS 5→3 — net **+1**

**Highest Impact Trades**

**1. Give Zack Wheeler → get Chris Sale** *(from Datalickmyballs)* — combined +3
- Zack Wheeler projections: K/9:10.2  QS:15  SVHD:0  ERA:3.256  WHIP:1.064
- Chris Sale projections: K/9:11.0  QS:18  SVHD:0  ERA:3.253  WHIP:1.097
- Midnight Muncy's gains: K/9 3→2, QS 7→6 — net **+2**
- Datalickmyballs gains: WHIP 6→5 — net **+1**

**2. Give Miguel Vargas → get Colson Montgomery** *(from Datalickmyballs)* — combined +3
- Miguel Vargas projections: R:69  HR:17  RBI:64  SB:8  OPS:0.717
- Colson Montgomery projections: R:64  HR:23  RBI:72  SB:3  OPS:0.688
- Midnight Muncy's gains: HR 8→7 — net **+1**
- Datalickmyballs gains: R 3→2, SB 7→6, OPS 5→4 — loses HR 3→4 — net **+2**

---

### Rock and Aroldis

*Strengths: QS (6), SVHD (5) — Weaknesses: HR (10), OPS (10), R (9), RBI (9), ERA (9), WHIP (9), SB (9), K/9 (8)*

**Most Balanced Trades**

**1. Give Ketel Marte → get Randy Arozarena** *(from Shohei Me the Money)* — combined +2
- Ketel Marte projections: R:89  HR:27  RBI:84  SB:5  OPS:0.840
- Randy Arozarena projections: R:84  HR:22  RBI:74  SB:24  OPS:0.711
- Rock and Aroldis gains: SB 9→5 — net **+1**
- Shohei Me the Money gains: OPS 9→8 — net **+1**

**2. Give Salvador Perez → get Evan Carter** *(from Shohei Me the Money)* — combined +2
- Salvador Perez projections: R:62  HR:26  RBI:86  SB:0  OPS:0.732
- Evan Carter projections: R:55  HR:11  RBI:45  SB:18  OPS:0.704
- Rock and Aroldis gains: SB 9→5 — net **+1**
- Shohei Me the Money gains: RBI 5→4 — net **+1**

**3. Give Salvador Perez → get JJ Wetherholt** *(from Shohei Me the Money)* — combined +2
- Salvador Perez projections: R:62  HR:26  RBI:86  SB:0  OPS:0.732
- JJ Wetherholt projections: R:55  HR:10  RBI:48  SB:11  OPS:0.697
- Rock and Aroldis gains: SB 9→6 — net **+1**
- Shohei Me the Money gains: RBI 5→4 — net **+1**

**4. Give Salvador Perez → get Ernie Clement** *(from Shohei Me the Money)* — combined +2
- Salvador Perez projections: R:62  HR:26  RBI:86  SB:0  OPS:0.732
- Ernie Clement projections: R:65  HR:11  RBI:58  SB:9  OPS:0.690
- Rock and Aroldis gains: SB 9→7 — net **+1**
- Shohei Me the Money gains: RBI 5→4 — net **+1**

**5. Give Salvador Perez → get George Springer** *(from Datalickmyballs)* — combined +2
- Salvador Perez projections: R:62  HR:26  RBI:86  SB:0  OPS:0.732
- George Springer projections: R:83  HR:24  RBI:73  SB:14  OPS:0.784
- Rock and Aroldis gains: SB 9→6 — net **+1**
- Datalickmyballs gains: HR 3→2, RBI 3→2 — loses SB 7→10 — net **+1**

**Highest Impact Trades**

**1. Give Ketel Marte → get George Springer** *(from Datalickmyballs)* — combined +4
- Ketel Marte projections: R:89  HR:27  RBI:84  SB:5  OPS:0.840
- George Springer projections: R:83  HR:24  RBI:73  SB:14  OPS:0.784
- Rock and Aroldis gains: SB 9→7 — net **+1**
- Datalickmyballs gains: R 3→2, HR 3→1, RBI 3→2, OPS 5→3 — loses SB 7→9 — net **+3**

**2. Give Andres Munoz → get Chris Sale** *(from Datalickmyballs)* — combined +3
- Andres Munoz projections: K/9:11.4  QS:0  SVHD:32  ERA:2.812  WHIP:1.109
- Chris Sale projections: K/9:11.0  QS:18  SVHD:0  ERA:3.253  WHIP:1.097
- Rock and Aroldis gains: K/9 8→6, QS 6→2, WHIP 9→8 — loses SVHD 5→7 — net **+2**
- Datalickmyballs gains: SVHD 2→1 — net **+1**

---

### Shohei Me the Money

*Strengths: K/9 (1), ERA (1), SVHD (4), SB (3) — Weaknesses: OPS (9), QS (8), HR (6)*

**Most Balanced Trades**

**1. Give Francisco Alvarez → get Brice Turang** *(from Welcome to the JUNGle)* — combined +4
- Francisco Alvarez projections: R:51  HR:20  RBI:57  SB:1  OPS:0.742
- Brice Turang projections: R:79  HR:14  RBI:65  SB:29  OPS:0.713
- Shohei Me the Money gains: R 4→3, SB 3→2 — net **+2**
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**

**2. Give MacKenzie Gore → get Eury Perez** *(from This Schlitt is Bazzanas)* — combined +2
- MacKenzie Gore projections: K/9:10.2  QS:19  SVHD:0  ERA:3.894  WHIP:1.242
- Eury Perez projections: K/9:9.8  QS:18  SVHD:0  ERA:3.986  WHIP:1.171
- Shohei Me the Money gains: WHIP 4→3 — net **+1**
- This Schlitt is Bazzanas gains: QS 4→3, ERA 5→4 — loses WHIP 3→4 — net **+1**

**3. Give Framber Valdez → get Brandon Woodruff** *(from Midnight Muncy's)* — combined +2
- Framber Valdez projections: K/9:8.3  QS:20  SVHD:0  ERA:3.478  WHIP:1.228
- Brandon Woodruff projections: K/9:9.5  QS:18  SVHD:0  ERA:3.753  WHIP:1.128
- Shohei Me the Money gains: WHIP 4→3 — net **+1**
- Midnight Muncy's gains: QS 7→6, ERA 4→3 — loses WHIP 1→2 — net **+1**

**4. Give Trevor Megill → get Raisel Iglesias** *(from Dingers Only)* — combined +2
- Trevor Megill projections: K/9:11.1  QS:0  SVHD:19  ERA:3.462  WHIP:1.169
- Raisel Iglesias projections: K/9:9.7  QS:0  SVHD:27  ERA:3.621  WHIP:1.133
- Shohei Me the Money gains: SVHD 4→3 — net **+1**
- Dingers Only gains: K/9 5→4 — net **+1**

**5. Give Jose Ramirez → get Aaron Judge** *(from All Rise)* — combined +2
- Jose Ramirez projections: R:91  HR:27  RBI:89  SB:33  OPS:0.825
- Aaron Judge projections: R:110  HR:46  RBI:113  SB:9  OPS:1.028
- Shohei Me the Money gains: OPS 9→8 — net **+1**
- All Rise gains: SB 2→1 — net **+1**

**Highest Impact Trades**

**1. Give Nasim Nunez → get Mike Trout** *(from All Rise)* — combined +3
- Nasim Nunez projections: R:34  HR:4  RBI:24  SB:23  OPS:0.617
- Mike Trout projections: R:68  HR:25  RBI:68  SB:3  OPS:0.797
- Shohei Me the Money gains: R 4→2, RBI 5→4 — net **+2**
- All Rise gains: SB 2→1 — net **+1**

**2. Give Nasim Nunez → get Munetaka Murakami** *(from All Rise)* — combined +3
- Nasim Nunez projections: R:34  HR:4  RBI:24  SB:23  OPS:0.617
- Munetaka Murakami projections: R:69  HR:27  RBI:72  SB:9  OPS:0.755
- Shohei Me the Money gains: R 4→2, RBI 5→4 — net **+2**
- All Rise gains: SB 2→1 — net **+1**

---

### Skubal Snacks

*Strengths: OPS (1), K/9 (4) — Weaknesses: QS (10), WHIP (10), ERA (8)*

**Most Balanced Trades**

**1. Give Tanner Scott → get Eury Perez** *(from This Schlitt is Bazzanas)* — combined +2
- Tanner Scott projections: K/9:10.1  QS:0  SVHD:4  ERA:3.472  WHIP:1.219
- Eury Perez projections: K/9:9.8  QS:18  SVHD:0  ERA:3.986  WHIP:1.171
- Skubal Snacks gains: WHIP 10→9 — net **+1**
- This Schlitt is Bazzanas gains: SVHD 10→9, ERA 5→3 — loses QS 4→9 — net **+1**

**2. Give Eugenio Suarez → get Vladimir Guerrero Jr.** *(from Datalickmyballs)* — combined +2
- Eugenio Suarez projections: R:77  HR:34  RBI:95  SB:3  OPS:0.771
- Vladimir Guerrero Jr. projections: R:94  HR:30  RBI:97  SB:5  OPS:0.888
- Skubal Snacks gains: RBI 6→5 — net **+1**
- Datalickmyballs gains: HR 3→1 — net **+1**

**3. Give Nick Kurtz → get Vladimir Guerrero Jr.** *(from Datalickmyballs)* — combined +2
- Nick Kurtz projections: R:91  HR:36  RBI:94  SB:3  OPS:0.874
- Vladimir Guerrero Jr. projections: R:94  HR:30  RBI:97  SB:5  OPS:0.888
- Skubal Snacks gains: RBI 6→5 — net **+1**
- Datalickmyballs gains: HR 3→1 — net **+1**

**4. Give Yordan Alvarez → get Bryce Harper** *(from Datalickmyballs)* — combined +2
- Yordan Alvarez projections: R:81  HR:30  RBI:85  SB:3  OPS:0.926
- Bryce Harper projections: R:84  HR:27  RBI:88  SB:10  OPS:0.850
- Skubal Snacks gains: RBI 6→5, SB 6→5 — loses OPS 1→2 — net **+1**
- Datalickmyballs gains: HR 3→1, OPS 5→3 — loses SB 7→9 — net **+1**

**5. Give Eugenio Suarez → get Jazz Chisholm Jr.** *(from Datalickmyballs)* — combined +2
- Eugenio Suarez projections: R:77  HR:34  RBI:95  SB:3  OPS:0.771
- Jazz Chisholm Jr. projections: R:79  HR:28  RBI:80  SB:31  OPS:0.758
- Skubal Snacks gains: SB 6→4 — net **+1**
- Datalickmyballs gains: HR 3→1, RBI 3→2 — loses SB 7→10 — net **+1**

**Highest Impact Trades**

**1. Give Yordan Alvarez → get Manny Machado** *(from Midnight Muncy's)* — combined +3
- Yordan Alvarez projections: R:81  HR:30  RBI:85  SB:3  OPS:0.926
- Manny Machado projections: R:79  HR:26  RBI:88  SB:9  OPS:0.770
- Skubal Snacks gains: RBI 6→5, SB 6→5 — loses OPS 1→2 — net **+1**
- Midnight Muncy's gains: HR 8→7, OPS 8→6 — net **+2**

**2. Give Matt McLain → get Bryson Stott** *(from Midnight Muncy's)* — combined +3
- Matt McLain projections: R:67  HR:17  RBI:58  SB:16  OPS:0.705
- Bryson Stott projections: R:68  HR:13  RBI:61  SB:23  OPS:0.708
- Skubal Snacks gains: RBI 6→5, SB 6→5 — net **+2**
- Midnight Muncy's gains: HR 8→7 — net **+1**

---

### This Schlitt is Bazzanas

*Strengths: HR (1), K/9 (2), R (2), RBI (2), OPS (3), WHIP (3) — Weaknesses: SVHD (10)*

**Most Balanced Trades**

**1. Give Eury Perez → get MacKenzie Gore** *(from Shohei Me the Money)* — combined +2
- Eury Perez projections: K/9:9.8  QS:18  SVHD:0  ERA:3.986  WHIP:1.171
- MacKenzie Gore projections: K/9:10.2  QS:19  SVHD:0  ERA:3.894  WHIP:1.242
- This Schlitt is Bazzanas gains: QS 4→3, ERA 5→4 — loses WHIP 3→4 — net **+1**
- Shohei Me the Money gains: WHIP 4→3 — net **+1**

**2. Give Cam Schlittler → get Gavin Williams** *(from Datalickmyballs)* — combined +2
- Cam Schlittler projections: K/9:9.1  QS:16  SVHD:0  ERA:4.043  WHIP:1.284
- Gavin Williams projections: K/9:9.2  QS:20  SVHD:0  ERA:3.958  WHIP:1.301
- This Schlitt is Bazzanas gains: QS 4→3 — net **+1**
- Datalickmyballs gains: WHIP 6→5 — net **+1**

**3. Give Kris Bubic → get Gavin Williams** *(from Datalickmyballs)* — combined +2
- Kris Bubic projections: K/9:8.8  QS:16  SVHD:0  ERA:3.761  WHIP:1.254
- Gavin Williams projections: K/9:9.2  QS:20  SVHD:0  ERA:3.958  WHIP:1.301
- This Schlitt is Bazzanas gains: QS 4→3 — net **+1**
- Datalickmyballs gains: WHIP 6→4 — net **+1**

**4. Give Drew Rasmussen → get Jeff Hoffman** *(from Datalickmyballs)* — combined +2
- Drew Rasmussen projections: K/9:8.0  QS:20  SVHD:0  ERA:3.623  WHIP:1.176
- Jeff Hoffman projections: K/9:10.8  QS:0  SVHD:26  ERA:3.651  WHIP:1.170
- This Schlitt is Bazzanas gains: K/9 2→1, SVHD 10→8 — loses QS 4→9 — net **+1**
- Datalickmyballs gains: QS 9→3, WHIP 6→5 — loses SVHD 2→5 — net **+1**

**5. Give Drew Rasmussen → get Dennis Santana** *(from Datalickmyballs)* — combined +2
- Drew Rasmussen projections: K/9:8.0  QS:20  SVHD:0  ERA:3.623  WHIP:1.176
- Dennis Santana projections: K/9:8.3  QS:0  SVHD:24  ERA:3.907  WHIP:1.259
- This Schlitt is Bazzanas gains: K/9 2→1, SVHD 10→9 — loses QS 4→9 — net **+1**
- Datalickmyballs gains: QS 9→3, WHIP 6→4 — loses SVHD 2→5 — net **+1**

**Highest Impact Trades**

**1. Give Cam Schlittler → get Bubba Chandler** *(from Welcome to the JUNGle)* — combined +3
- Cam Schlittler projections: K/9:9.1  QS:16  SVHD:0  ERA:4.043  WHIP:1.284
- Bubba Chandler projections: K/9:8.5  QS:17  SVHD:0  ERA:4.196  WHIP:1.315
- This Schlitt is Bazzanas gains: QS 4→3 — net **+1**
- Welcome to the JUNGle gains: K/9 6→5, ERA 3→2 — net **+2**

**2. Give Rico Garcia → get Gavin Williams** *(from Datalickmyballs)* — combined +2
- Rico Garcia projections: K/9:9.2  QS:0  SVHD:0  ERA:4.352  WHIP:1.373
- Gavin Williams projections: K/9:9.2  QS:20  SVHD:0  ERA:3.958  WHIP:1.301
- This Schlitt is Bazzanas gains: QS 4→2 — net **+1**
- Datalickmyballs gains: WHIP 6→5 — net **+1**

---

### Welcome to the JUNGle

*Strengths: R (1), RBI (1), HR (2), WHIP (2), ERA (3) — Weaknesses: SB (10), SVHD (9)*

**Most Balanced Trades**

**1. Give Brice Turang → get Francisco Alvarez** *(from Shohei Me the Money)* — combined +4
- Brice Turang projections: R:79  HR:14  RBI:65  SB:29  OPS:0.713
- Francisco Alvarez projections: R:51  HR:20  RBI:57  SB:1  OPS:0.742
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**
- Shohei Me the Money gains: R 4→3, SB 3→2 — net **+2**

**2. Give Jackson Chourio → get Bryce Harper** *(from Datalickmyballs)* — combined +4
- Jackson Chourio projections: R:87  HR:23  RBI:83  SB:24  OPS:0.777
- Bryce Harper projections: R:84  HR:27  RBI:88  SB:10  OPS:0.850
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**
- Datalickmyballs gains: R 3→2, SB 7→4 — net **+2**

**3. Give Willy Adames → get Shea Langeliers** *(from Datalickmyballs)* — combined +4
- Willy Adames projections: R:82  HR:26  RBI:83  SB:11  OPS:0.733
- Shea Langeliers projections: R:69  HR:28  RBI:78  SB:6  OPS:0.798
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**
- Datalickmyballs gains: R 3→2, SB 7→6 — net **+2**

**4. Give Willy Adames → get Hunter Goodman** *(from Datalickmyballs)* — combined +4
- Willy Adames projections: R:82  HR:26  RBI:83  SB:11  OPS:0.733
- Hunter Goodman projections: R:69  HR:28  RBI:84  SB:2  OPS:0.791
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**
- Datalickmyballs gains: R 3→2, SB 7→6 — net **+2**

**5. Give Brice Turang → get Mike Trout** *(from All Rise)* — combined +4
- Brice Turang projections: R:79  HR:14  RBI:65  SB:29  OPS:0.713
- Mike Trout projections: R:68  HR:25  RBI:68  SB:3  OPS:0.797
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**
- All Rise gains: R 10→9, SB 2→1 — net **+2**

**Highest Impact Trades**

**1. Give Jackson Chourio → get George Springer** *(from Datalickmyballs)* — combined +4
- Jackson Chourio projections: R:87  HR:23  RBI:83  SB:24  OPS:0.777
- George Springer projections: R:83  HR:24  RBI:73  SB:14  OPS:0.784
- Welcome to the JUNGle gains: HR 2→1 — net **+1**
- Datalickmyballs gains: R 3→2, RBI 3→2, SB 7→6 — net **+3**

**2. Give Brice Turang → get Munetaka Murakami** *(from All Rise)* — combined +4
- Brice Turang projections: R:79  HR:14  RBI:65  SB:29  OPS:0.713
- Munetaka Murakami projections: R:69  HR:27  RBI:72  SB:9  OPS:0.755
- Welcome to the JUNGle gains: HR 2→1, OPS 4→3 — net **+2**
- All Rise gains: R 10→9, SB 2→1 — net **+2**

---

## Notes & Limitations

- **Positional eligibility not enforced.** The simulation checks player type (batter vs pitcher) but does not verify slot eligibility (e.g. trading your only catcher may create a roster hole). Verify manually before approaching a trade.
- **Pitcher SVHD is understated.** The projection file does not include holds — SVHD projection uses SV only as a floor. Relievers with hold value are undercounted.
- **Projections are full-season, not rest-of-season.** All players are evaluated on the same basis so relative rankings hold, but a player already ahead of their projection pace will appear to regress toward the projection.
- **1-for-1 swaps only.** Multi-player packages are not evaluated.
- **Scripts relocated to `fantasy_baseball/trade_analysis/`.** Run `analyze_trade_finder_espn_2026.py` to regenerate the CSV, then `generate_trade_summary_espn_2026.py` for a fresh markdown report.

---

#### TODO
- [x] Initial draft
- [x] Scoring system table
- [x] Data sources section
- [x] Methodology section
- [x] Projected standings table
- [x] Top 5 trades per team
- [x] Notes and limitations
- [x] Balanced vs high-impact trade tiers
- [x] Team category profiles (strengths, weaknesses, trade targets)
- [x] Scripts moved to `trade_analysis/` subfolder

---

[Home](https://pjrigali.github.io)

*Last Updated: 2026-05-14*
