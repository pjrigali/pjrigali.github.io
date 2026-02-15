---
layout: default
title: "14_2025 Fantasy Baseball Impact Analysis"
description: An in-depth analysis of the 2025 Fantasy Baseball season, focusing on the impact of the Draft vs. Free Agency.
permalink: /posts/2025_Fantasy_Impact
nav_order: 2.15
---

## Project Overview

This analysis evaluates the roster management strategies of the 2025 Fantasy Baseball season. By leveraging daily player statistics and transaction history, we determine the relative importance of the Draft versus Free Agency and identify which teams were most effective at managing their rosters.

The core metric used is a **Volume-Weighted Impact Z-Score**. This method converts all counting and rate statistics into standardized impact values relative to the league average, rewarding both quality and volume of play.

---


### Key Findings


#### 1. Draft vs. Free Agency Importance
The 2025 season data overwhelmingly suggests that the **Draft** is the primary driver of positive team value, while the aggregate impact of Free Agency is negative.

*   **Draft**: Generated a Net Z-Score of **+137.0**, with **56** players converting positive value.
*   **Free Agency**: Generated a Net Z-Score of **-137.0**, with only **38** players providing positive value.

The chart below visualizes this massive disparity. Most teams show a strong positive blue bar (Draft value) and a negative orange bar (Free Agent value), indicating that their roster churn actually hurt their overall categorical standing.

![Draft vs Free Agent Impact](/assets/images/impact_2025_draft_vs_fa.png)

This stark contrast highlights the difficulty of streaming players. While finding a "diamond in the rough" is possible, the average free agent pickup performs significantly below the league replacement level, often hurting team ratios (ERA, WHIP) or failing to accumulate meaningful counting stats.



#### 2. Best Draft Picks
The draft builds the foundation. These were the monsters that anchored their respective teams.

| Rank | Player | Team | Total Z-Score |
|:---|:---|:---|:---|
| 1 | **Tarik Skubal** | AFFO | 13.15 |
| 2 | **Zack Wheeler** | BP | 12.50 |
| 3 | **Paul Skenes** | ELLI | 11.91 |
| 4 | **Garrett Crochet** | AFFO | 10.13 |
| 5 | **Hunter Brown** | AFFO | 9.37 |
| 6 | Aroldis Chapman | BP | 9.22 |
| 7 | Nathan Eovaldi | BP | 8.70 |
| 8 | Joe Ryan | $$$ | 7.87 |
| 9 | Bryan Abreu | $$$ | 7.84 |
| 10 | Yoshinobu Yamamoto | GIBB | 7.79 |

#### 3. Best Free Agent Pickups
Despite the general difficulty of free agency, several impact players were acquired off the wire. The top pickups by Total Impact Z-Score were:

| Rank | Player | Team | Total Z-Score |
|:---|:---|:---|:---|
| 1 | **Nick Pivetta** | AFFO | 7.67 |
| 2 | **Abner Uribe** | AFFO | 5.97 |
| 3 | **Emilio Pagan** | ELLI | 4.07 |
| 4 | **Jeremiah Estrada** | HILL | 3.70 |
| 5 | **Carlos Estevez** | PJR | 3.12 |
| 6 | Griffin Jax | HILL | 2.69 |
| 7 | Merrill Kelly | CHER | 2.68 |
| 8 | Jacob Misiorowski | CHER | 2.65 |
| 9 | Nick Lodolo | DO | 2.61 |
| 10 | Ranger Suarez | ELLI | 2.54 |

**Nick Pivetta's** dominance as a free agent pickup suggests a scenario where a high-strikeout starter was dropped (perhaps due to injury or a bad stretch) and then provided elite production upon return.

#### 4. Best Teams at Free Agency
Efficacy in the free agent market varied widly by team. **AFFO** stands out as the *only* team to generate significant positive net value from their free agent moves.

| Rank | Team | Source Impact (Z-Score) | Analysis |
|:---|:---|:---|:---|
| 1 | **AFFO** | **+5.19** | The clear winner of the waiver wire, finding multiple high-impact arms. |
| 2 | YBSD | -1.21 | Neutral/Slightly Negative. churned roster without imploding ratios. |
| 3 | DO | -2.45 | Minor negative impact. |
| 4 | GIBB | -3.74 | Minor negative impact. |
| 5 | CHER | -12.10 | Struggled to find consistent contributors. |
| 6 | ELLI | -12.53 | Negative impact despite finding Pagan/Suarez. |
| 7 | $$$ | -15.73 | Significant value lost to churn. |
| 8 | PJR | -16.99 | Significant value lost to churn. |
| 9 | HILL | -38.71 | High activity led to accumulation of poor stats. |
| 10 | BP | -38.76 | High activity led to accumulation of poor stats. |

---

## 4. Team-by-Team Breakdown

Below is a snapshot of each team's best and worst moves from the Draft and Waiver Wire, along with a completely unsolicited performance review.

### Team: $$$
*Drafted like a pro, managed like an intern. You set yourself up for success and then tried your hardest to trade it away for magic beans on the waiver wire.*
*   **Best Draft Pick**: Joe Ryan (7.87)
*   **Worst Draft Pick**: Tanner Houck (-6.42)
*   **Best Free Agent**: Ben Joyce (-1.50)
*   **Worst Free Agent**: Luis Severino (-3.83)

### Team: AFFO
*A masterclass in roster construction. The draft was solid, and the moves actually made sense. We're all very impressed (and slightly annoyed).*
*   **Best Draft Pick**: Tarik Skubal (13.15)
*   **Worst Draft Pick**: Reese Olson (-1.46)
*   **Best Free Agent**: Nick Pivetta (7.67)
*   **Worst Free Agent**: Jeffrey Springs (-1.95)

### Team: BP
*Drafted like a pro, managed like an intern. You set yourself up for success and then tried your hardest to trade it away for magic beans on the waiver wire.*
*   **Best Draft Pick**: Zack Wheeler (12.50)
*   **Worst Draft Pick**: Ryan Pressly (-2.94)
*   **Best Free Agent**: Trevor Rogers (1.04)
*   **Worst Free Agent**: Michael Wacha (-2.92)

### Team: CHER
*Middling. Forgettable. The beige of fantasy baseball performances. Neither good enough to brag nor bad enough to be funny.*
*   **Best Draft Pick**: Bryan Woo (5.74)
*   **Worst Draft Pick**: Luis Castillo (-2.32)
*   **Best Free Agent**: Merrill Kelly (2.68)
*   **Worst Free Agent**: Mitch Keller (-3.48)

### Team: DO
*Middling. Forgettable. The beige of fantasy baseball performances. Neither good enough to brag nor bad enough to be funny.*
*   **Best Draft Pick**: Josh Hader (7.37)
*   **Worst Draft Pick**: Bailey Ober (-4.29)
*   **Best Free Agent**: Nick Lodolo (2.61)
*   **Worst Free Agent**: Chris Bassitt (-2.83)

### Team: ELLI
*Middling. Forgettable. The beige of fantasy baseball performances. Neither good enough to brag nor bad enough to be funny.*
*   **Best Draft Pick**: Paul Skenes (11.91)
*   **Worst Draft Pick**: Bryce Miller (-3.77)
*   **Best Free Agent**: Emilio Pagan (4.07)
*   **Worst Free Agent**: Jose Soriano (-3.30)

### Team: GIBB
*Middling. Forgettable. The beige of fantasy baseball performances. Neither good enough to brag nor bad enough to be funny.*
*   **Best Draft Pick**: Yoshinobu Yamamoto (7.79)
*   **Worst Draft Pick**: Brandon Pfaadt (-4.97)
*   **Best Free Agent**: Blake Treinen (-0.87)
*   **Worst Free Agent**: Yennier Cano (-2.86)

### Team: HILL
*Stop touching your roster. Seriously. Every time you picked up a free agent, an angel lost its wings (and your team lost ERA points).*
*   **Best Draft Pick**: Cade Smith (6.64)
*   **Worst Draft Pick**: Spencer Strider (-2.61)
*   **Best Free Agent**: Jeremiah Estrada (3.70)
*   **Worst Free Agent**: Lucas Giolito (-4.27)

### Team: PJR
*Middling. Forgettable. The beige of fantasy baseball performances. Neither good enough to brag nor bad enough to be funny.*
*   **Best Draft Pick**: Logan Webb (4.88)
*   **Worst Draft Pick**: Yusei Kikuchi (-2.85)
*   **Best Free Agent**: Carlos Estevez (3.12)
*   **Worst Free Agent**: Matthew Liberatore (-5.96)

### Team: YBSD
*Middling. Forgettable. The beige of fantasy baseball performances. Neither good enough to brag nor bad enough to be funny.*
*   **Best Draft Pick**: Cristopher Sanchez (6.75)
*   **Worst Draft Pick**: Sandy Alcantara (-7.33)
*   **Best Free Agent**: Nick Martinez (-1.21)
*   **Worst Free Agent**: Nick Martinez (-1.21)

---


### Methodology

The analysis was conducted using a custom Python pipeline:
1.  **Data Collection**:
    *   Daily player statistics (`daily_player_stats_2025.csv`).
    *   Transaction mapping via `roster_history_2025.csv` to determine if a player stint was from the Draft or Free Agency.
2.  **Impact Calculation**:
    *   All 10 scoring categories (R, HR, RBI, SB, OPS, K/9, QS, SVHD, ERA, WHIP) were analyzed.
    *   **Rate Stats (ERA, WHIP, OPS, K/9)** were converted to "Impact Units" based on volume (e.g., an ERA beater is worth more over 100 IP than 10 IP).
    *   **Z-Scores** were calculated for each category based on the active player population to standardize value.
3.  **Aggregation**:
    *   Z-Scores were summed by Player, Team, and Acquisition Source to determine the "Effective Season Impact".

---

## 5. The 'One That Got Away' Awards (Worst Drops)

These players were on a roster, sent packing, and then immediately made their former managers regret everything.

| Player | Dropped By | Picked Up By | Value Gained by New Team |
|:---|:---|:---|:---|
| **Nick Pivetta** | BP | AFFO | **7.67** |
| **Nick Lodolo** | AFFO | DO | **2.61** |
| **Trevor Megill** | PJR | CHER | **1.98** |
| **Jesus Luzardo** | CHER | BP | **1.03** |

***Analysis**: The Drop of the Year goes to **BP**, who released **Nick Pivetta**. Pivetta went on to become the single most impactful Free Agent pickup of the entire season for **AFFO**. Ouch.*

---

---

#### TODO
- [x] Initial analysis and data processing
- [ ] Add visualizations (Bar charts for Draft vs FA split)
- [ ] Deep dive into "Worst Drops" (players drafted, dropped, and then performed well elsewhere)

---

[Home](https://pjrigali.github.io)

*Last Updated: 2026-02-15*
