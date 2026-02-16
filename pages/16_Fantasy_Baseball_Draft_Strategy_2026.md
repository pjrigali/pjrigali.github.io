---
layout: default
title: "16_2026 Fantasy Baseball Draft Strategy"
description: A data-driven draft strategy for the 2026 fantasy baseball season using weighted Z-scores, positional VORP, and ADP value gaps.
permalink: /posts/2026_Draft_Strategy
nav_order: 2.17
---

## 2026 Fantasy Baseball Draft Strategy

**Team:** PJR (Datalickmyballs) | **Draft Position:** Pick 6, Round 1 | **Format:** Snake Draft, 10-team league

**Scoring Categories:**
*   **Batters:** R, HR, RBI, SB, OPS
*   **Pitchers:** ERA, WHIP, K/9, QS, SVHD

---

### Methodology

This analysis produces a **complete draft cheat sheet** by combining four layers of analytics:

1.  **Weighted Z-Scores** — Stats are standardized, then weighted by category scarcity. Categories where value is concentrated in fewer players (higher coefficient of variation) receive a larger weight.
2.  **Positional VORP** — Value Over Replacement Player is calculated *per position*, so a great catcher is worth more than an equally-good outfielder because the replacement-level drop-off is steeper.
3.  **ADP Value Gaps** — Compares each player's VORP rank to their consensus ADP, revealing who is being over- or under-drafted.
4.  **Keeper Removal** — All 50+ kept players are removed from the draft pool, giving a realistic picture of who is actually available.

---

### Category Scarcity Weights

Categories are not created equal. The scarcity weight (coefficient of variation of the top 50 players) determines how much each category contributes to a player's total value.

#### Batters

| Category | Weight | Signal |
|:---|:---|:---|
| SB | 1.458 | 🔴 Most scarce — elite speed is rare |
| HR | 1.173 | 🟡 Concentrated at the top |
| OPS | 0.920 | 🟡 Moderate concentration |
| R  | 0.743 | 🟢 More evenly distributed |
| RBI | 0.706 | 🟢 Widely available |

#### Pitchers

| Category | Weight | Signal |
|:---|:---|:---|
| SVHD | 2.040 | 🔴 Extremely scarce — closers dominate |
| K/9 | 1.121 | 🟡 Moderate concentration |
| ERA | 0.716 | 🟢 Relatively flat |
| WHIP | 0.630 | 🟢 Evenly distributed |
| QS | 0.492 | 🟢 Widely available |

**Key Insight:** Stolen bases for batters and saves+holds for pitchers are the scarcest categories. Drafting elite speed and elite closers gives a disproportionate edge in category leagues.

---

### Top 20 Batters — Weighted Z-Score

| Rank | Player | Team | Pos | R | HR | RBI | SB | OPS | Z-Score |
|:---|:---|:---|:---|---:|---:|---:|---:|---:|---:|
| 1 | **Shohei Ohtani** | LAD | DH | 111 | 44 | 103 | 41 | .909 | 14.88 |
| 2 | **Bobby Witt Jr.** | KC | SS | 103 | 27 | 87 | 42 | .832 | 11.53 |
| 3 | **Aaron Judge** | NYY | OF | 96 | 48 | 122 | 5 | .974 | 11.70 |
| 4 | **Juan Soto** | NYM | OF | 106 | 36 | 91 | 10 | .957 | 11.27 |
| 5 | **Elly De La Cruz** | CIN | SS | 100 | 26 | 72 | 59 | .770 | 10.94 |
| 6 | **Corbin Carroll** | ARI | OF | 94 | 23 | 65 | 42 | .779 | 10.64 |
| 7 | **Jose Ramirez** | CLE | 3B | 87 | 30 | 99 | 26 | .834 | 10.39 |
| 8 | **Ronald Acuna Jr.** | ATL | OF | 85 | 23 | 64 | 49 | .790 | 9.87 |
| 9 | **Julio Rodriguez** | SEA | OF | 86 | 24 | 75 | 34 | .789 | 9.25 |
| 10 | **Jazz Chisholm Jr.** | NYY | 2B | 82 | 25 | 67 | 35 | .770 | 8.82 |
| 11 | **Trea Turner** | PHI | SS | 91 | 18 | 60 | 34 | .782 | 8.60 |
| 12 | **Kyle Tucker** | CHC | OF | 92 | 28 | 86 | 21 | .851 | 8.56 |
| 13 | **Gunnar Henderson** | BAL | SS | 98 | 33 | 87 | 15 | .862 | 8.32 |
| 14 | **Jackson Chourio** | MIL | OF | 83 | 23 | 73 | 30 | .793 | 7.99 |
| 15 | **Francisco Lindor** | NYM | SS | 91 | 26 | 82 | 22 | .794 | 7.96 |
| 16 | **Cal Raleigh** | SEA | C | 74 | 33 | 91 | 5 | .838 | 7.47 |
| 17 | **Fernando Tatis Jr.** | SD | OF | 82 | 27 | 72 | 21 | .821 | 7.29 |
| 18 | **Pete Crow-Armstrong** | CHC | OF | 73 | 19 | 60 | 40 | .721 | 7.09 |
| 19 | **Brice Turang** | MIL | 2B | 77 | 14 | 56 | 42 | .714 | 6.70 |
| 20 | **Zach Neto** | LAA | SS | 86 | 25 | 73 | 20 | .790 | 7.98 |

---

### Top 20 Pitchers — Weighted Z-Score

| Rank | Player | Team | Role | IP | ERA | WHIP | K/9 | QS | SVHD | Z-Score |
|:---|:---|:---|:---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **Edwin Diaz** | NYM | RP | 63 | 2.85 | 0.93 | 13.68 | 0 | 40 | 17.50 |
| 2 | **Mason Miller** | OAK | RP | 65 | 2.73 | 1.01 | 13.23 | 0 | 38 | 17.27 |
| 3 | **Josh Hader** | HOU | RP | 62 | 3.27 | 1.14 | 11.14 | 0 | 37 | 15.48 |
| 4 | **Aroldis Chapman** | FA | RP | 59 | 3.22 | 1.15 | 12.65 | 0 | 32 | 15.03 |
| 5 | **Andres Munoz** | SEA | RP | 65 | 2.84 | 0.99 | 12.46 | 0 | 32 | 14.82 |
| 6 | **Jhoan Duran** | MIN | RP | 67 | 3.12 | 1.06 | 10.60 | 0 | 35 | 14.59 |
| 7 | **Cade Smith** | CLE | RP | 65 | 2.66 | 0.95 | 11.51 | 0 | 33 | 14.47 |
| 8 | **David Bednar** | PIT | RP | 63 | 2.83 | 1.00 | 12.03 | 0 | 32 | 14.45 |
| 9 | **Devin Williams** | NYY | RP | 58 | 2.67 | 1.08 | 12.72 | 0 | 32 | 14.31 |
| 10 | **Carlos Estevez** | PHI | RP | 63 | 3.32 | 1.06 | 9.53 | 0 | 33 | 12.94 |
| 11 | **Daniel Palencia** | CHC | RP | 62 | 3.57 | 1.23 | 9.78 | 0 | 28 | 12.01 |
| 12 | **Ryan Helsley** | STL | RP | 64 | 3.22 | 1.12 | 10.50 | 0 | 27 | 11.63 |
| 13 | **Raisel Iglesias** | ATL | RP | 63 | 3.28 | 1.03 | 9.95 | 0 | 28 | 11.55 |
| 14 | **Emilio Pagan** | NYM | RP | 62 | 3.38 | 1.19 | 10.46 | 0 | 26 | 11.40 |
| 15 | **Pete Fairbanks** | TB | RP | 60 | 3.22 | 1.10 | 10.28 | 0 | 28 | 11.39 |
| 16 | **Jeff Hoffman** | TOR | RP | 64 | 3.68 | 1.17 | 10.81 | 0 | 26 | 11.34 |
| 17 | **Ryan Walker** | SF | RP | 64 | 3.41 | 1.18 | 9.66 | 0 | 25 | 10.66 |
| 18 | **Kenley Jansen** | DET | RP | 59 | 3.92 | 1.20 | 9.11 | 0 | 25 | 10.21 |
| 19 | **Tarik Skubal** | DET | SP | 195 | 2.86 | 0.99 | 10.68 | 21 | 0 | 9.60 |
| 20 | **Dennis Santana** | PIT | RP | 69 | 3.95 | 1.26 | 8.34 | 0 | 24 | 9.42 |

**Key Insight:** Every single one of the top 18 pitchers by Z-Score is a **reliever**. In this scoring format (SVHD), elite closers dominate. Tarik Skubal is the first SP at #19.

---

### Positional Scarcity & Replacement Levels

VORP (Value Over Replacement Player) is the difference between a player's Z-Score and the Z-Score of the last rostered player at that position.

| Position | Rostered | Replacement Z | Scarcity |
|:---|---:|---:|:---|
| C | 10 | 0.15 | 🔴 Very Shallow — elite catchers are gold |
| SS | 10 | 4.37 | 🟡 Deep talent pool — high replacement level |
| 2B | 10 | 1.93 | 🟢 Moderate |
| 3B | 10 | 1.47 | 🟢 Moderate |
| 1B | 10 | 2.70 | 🟡 Moderate |
| OF | 30 | 3.47 | 🟡 Deep pool due to 3 slots |
| SP | 50 | 0.51 | 🟢 Very deep — replacement SPs are easy to find |
| RP | 30 | 3.90 | 🔴 High baseline — need elite closers to stand out |

---

### Top 30 Overall by Positional VORP

| Rank | Player | Pos | Type | Z-Score | VORP |
|:---|:---|:---|:---|---:|---:|
| 1 | **Shohei Ohtani** | UTIL | Batter | 14.88 | 14.88 |
| 2 | **Edwin Diaz** | RP | Pitcher | 17.50 | 13.59 |
| 3 | **Mason Miller** | RP | Pitcher | 17.27 | 13.37 |
| 4 | **Josh Hader** | RP | Pitcher | 15.48 | 11.58 |
| 5 | **Aroldis Chapman** | RP | Pitcher | 15.03 | 11.12 |
| 6 | **Andres Munoz** | RP | Pitcher | 14.82 | 10.92 |
| 7 | **Jhoan Duran** | RP | Pitcher | 14.59 | 10.68 |
| 8 | **Cade Smith** | RP | Pitcher | 14.47 | 10.56 |
| 9 | **David Bednar** | RP | Pitcher | 14.45 | 10.54 |
| 10 | **Devin Williams** | RP | Pitcher | 14.31 | 10.41 |
| 11 | **Carlos Estevez** | RP | Pitcher | 12.94 | 9.04 |
| 12 | **Jose Ramirez** | 3B | Batter | 10.39 | 8.93 |
| 13 | **Aaron Judge** | OF | Batter | 11.70 | 8.23 |
| 14 | **Daniel Palencia** | RP | Pitcher | 12.01 | 8.11 |
| 15 | **Juan Soto** | OF | Batter | 11.27 | 7.80 |
| 16 | **Ryan Helsley** | RP | Pitcher | 11.63 | 7.73 |
| 17 | **Raisel Iglesias** | RP | Pitcher | 11.55 | 7.65 |
| 18 | **Emilio Pagan** | RP | Pitcher | 11.40 | 7.50 |
| 19 | **Pete Fairbanks** | RP | Pitcher | 11.39 | 7.49 |
| 20 | **Jeff Hoffman** | RP | Pitcher | 11.34 | 7.44 |
| 21 | **Cal Raleigh** | C | Batter | 7.47 | 7.33 |
| 22 | **Bobby Witt Jr.** | SS | Batter | 11.53 | 7.17 |
| 23 | **Corbin Carroll** | OF | Batter | 10.64 | 7.17 |
| 24 | **Jazz Chisholm Jr.** | 2B | Batter | 8.82 | 6.90 |
| 25 | **Ryan Walker** | RP | Pitcher | 10.66 | 6.76 |
| 26 | **Elly De La Cruz** | SS | Batter | 10.94 | 6.57 |
| 27 | **Ronald Acuna Jr.** | OF | Batter | 9.87 | 6.40 |
| 28 | **Kenley Jansen** | RP | Pitcher | 10.21 | 6.31 |
| 29 | **Julio Rodriguez** | OF | Batter | 9.25 | 5.78 |
| 30 | **Dennis Santana** | RP | Pitcher | 9.42 | 5.52 |

**Key Insight:** 20 of the top 30 VORP players are relievers. The SVHD scarcity weight makes elite closers the most valuable fantasy asset in this format.

---

### Keeper Impact Analysis

50 players are being kept across 10 teams. These players are **removed from the draft pool**.

#### Keeper Z-Value by Team

| Rank | Team | Total Keeper Z | Assessment |
|:---|:---|---:|:---|
| 1 | CHER | 34.52 | 🏆 Dominant — Judge, Witt, PCA, EDLC, J-Rod |
| 2 | $$$ | 32.56 | 🏆 Ohtani, Ramirez, Lindor, Yelich |
| 3 | DO | 29.95 | Strong — Schwarber, Raleigh, Hader |
| 4 | HILL | 26.21 | Solid |
| 5 | BP | 25.73 | Solid — Chapman, Wheeler core |
| 6 | AFFO | 24.75 | Solid — Skubal, Crochet pitching core |
| **7** | **PJR** | **21.22** | ⚠️ Middle of the pack |
| 8 | GIBB | 20.74 | Soto carries |
| 9 | ELLI | 15.57 | Below average |
| 10 | YBSD | 14.27 | Weakest keeper class |

#### PJR's Keepers

| Player | Position | Z-Score | Key Stats |
|:---|:---|---:|:---|
| Trea Turner | Batter | 4.85 | R:91 / HR:14 / RBI:63 / SB:34 / OPS:.808 |
| Jazz Chisholm Jr. | Batter | 4.36 | R:65 / HR:26 / RBI:67 / SB:25 / OPS:.828 |
| Cody Bellinger | Batter | 4.30 | R:75 / HR:26 / RBI:83 / SB:11 / OPS:.843 |
| Taylor Ward | Batter | 3.86 | R:75 / HR:30 / RBI:94 / SB:3 / OPS:.794 |
| Geraldo Perdomo | Batter | 3.85 | R:80 / HR:14 / RBI:75 / SB:22 / OPS:.829 |

⚠️ **All 5 keepers are batters.** PJR has **zero pitching** heading into the draft. Addressing this is the top priority.

---

### ADP Value Gaps

**Overvalued** (drafted too early relative to projected value):

| Player | Pos | Type | ADP | VORP | Gap |
|:---|:---|:---|---:|---:|---:|
| Max Muncy | SS | Batter | 203.4 | -8.17 | -608 |
| Luis Garcia | RP | Pitcher | 250.0 | -5.98 | -481 |
| Kevin McGonigle | SS | Batter | 311.4 | -6.87 | -468 |
| Ha-Seong Kim | SS | Batter | 313.3 | -6.73 | -454 |
| Nick Castellanos | OF | Batter | 313.0 | -6.60 | -453 |
| Javier Baez | SS | Batter | 378.6 | -8.57 | -427 |
| Jacob Wilson | SS | Batter | 161.0 | -4.40 | -402 |
| JJ Wetherholt | SS | Batter | 248.6 | -5.20 | -393 |

**Undervalued** (drafted later than their value warrants):

| Player | Pos | Type | ADP | VORP | Gap |
|:---|:---|:---|---:|---:|---:|
| Robert Garcia | RP | Pitcher | 306.2 | 3.79 | +216 |
| Victor Vodnik | RP | Pitcher | 396.7 | 2.32 | +287 |
| Clayton Beeter | RP | Pitcher | 411.0 | 0.93 | +260 |
| Seranthony Dominguez | RP | Pitcher | 286.2 | 3.18 | +183 |
| Riley O'Brien | RP | Pitcher | 307.6 | 2.08 | +185 |

**Key Insight:** The overvalued list is dominated by **shortstops** — players being drafted on name recognition despite mediocre projected stats. The undervalued list is all **relievers** with meaningful SVHD upside being ignored.

---

### Draft Strategy

Given that all 5 keepers are batters and the analysis shows elite relievers are the most valuable asset class:

#### Round-by-Round Plan

| Rounds | Strategy | Rationale |
|:---|:---|:---|
| **1–3** | 🔴 PITCHER PRIORITY | Zero pitching kept. Target elite closers (Edwin Diaz, Mason Miller, Jhoan Duran, David Bednar) |
| **4–6** | BPA / Power Bat | Fill HR/RBI needs. Look for high-VORP bats (Ronald Acuna Jr., Gunnar Henderson) |
| **7–10** | Fill Roster Needs | Catcher (Shea Langeliers), remaining IF depth |
| **11+** | High-Upside Fliers | Late-round relievers with closing upside |

#### Tier 1 — Must-Draft (Available, VORP > 8.0)

| Player | Pos | VORP |
|:---|:---|---:|
| Edwin Diaz | RP | 13.59 |
| Mason Miller | RP | 13.37 |
| Jhoan Duran | RP | 10.68 |
| Cade Smith | RP | 10.56 |
| David Bednar | RP | 10.54 |
| Devin Williams | RP | 10.41 |
| Carlos Estevez | RP | 9.04 |
| Daniel Palencia | RP | 8.11 |

#### Tier 2 — Strong Targets (VORP 3.0–8.0)

| Player | Pos | Type | VORP |
|:---|:---|:---|---:|
| Ryan Helsley | RP | Pitcher | 7.73 |
| Raisel Iglesias | RP | Pitcher | 7.65 |
| Emilio Pagan | RP | Pitcher | 7.50 |
| Pete Fairbanks | RP | Pitcher | 7.49 |
| Jeff Hoffman | RP | Pitcher | 7.44 |
| Ronald Acuna Jr. | OF | Batter | 6.40 |
| Ryan Walker | RP | Pitcher | 6.76 |
| Kenley Jansen | RP | Pitcher | 6.31 |
| Gunnar Henderson | SS | Batter | 3.95 |
| Jackson Chourio | OF | Batter | 3.62 |
| Shea Langeliers | C | Batter | 3.33 |

---

### Takeaways

1.  **Relievers are king.** In this scoring format (SVHD weight = 2.04x), elite closers are far more valuable than starting pitchers. Target them aggressively.
2.  **Stolen bases are the scarce batter category.** SB weight (1.46x) is double that of RBI (0.71x). Speed-first batters like Elly De La Cruz and Corbin Carroll are more valuable than sluggers.
3.  **Avoid shortstops on name value.** SS has the deepest replacement level (4.37 Z) — overpaying for middling SS is the biggest trap in this draft.
4.  **PJR's keepers are solid but pitcher-starved.** The all-batter keeper class means Rounds 1-3 must go to elite arms or the season is sunk.
5.  **Catcher is a cheat code.** With a replacement level of just 0.15 Z, drafting Cal Raleigh or Shea Langeliers provides massive positional VORP.

---

#### TODO
- [x] Z-Score projections (weighted by scarcity)
- [x] Positional VORP analysis
- [x] Keeper impact analysis
- [x] ADP value gap identification
- [x] Draft strategy and cheat sheet

---

[Home](https://pjrigali.github.io)

*Last Updated: 2026-02-16*
