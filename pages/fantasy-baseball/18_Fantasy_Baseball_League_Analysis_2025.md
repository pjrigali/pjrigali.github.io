---
layout: default
title: "18_2025 Fantasy Baseball League Analysis"
description: An in-depth analysis of roster management styles across the entire league. Optimal evaluation windows, churn rates, and manager breakdown.
permalink: /fantasy-baseball/league-analysis-2025
parent: Fantasy Baseball
nav_order: 6
---

## League-Wide Roster Analysis

After auditing my own team, I expanded the analysis to all 10 teams in the league to identify the "Optimal Strategy" for our specific league settings.

I tested evaluation windows from **3 to 90 days** and correlated roster moves with final team success.

[< Back to Team PJR Audit](pages/18_Fantasy_Baseball_Roster_Audit_2025.md)

---

### 1. The Optimal Lookback Window

One of the hardest questions in fantasy is: *"How much recent performance history matters?"*

I calculated the predictive power (correlation with future performance) for lookback windows ranging from 3 to 90 days across the entire league.

**Winner: 42 Days**
While a 90-day window technically had the highest correlation, a **42-day window** (6 weeks) captures **92%** of the predictive power but allows you to react nearly **7 weeks** faster.

```mermaid
xychart-beta
    title "Predictive Power vs Lookback Window"
    x-axis "Days" [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]
    y-axis "Correlation" 0.127 --> 0.365
    line [0.1334, 0.1768, 0.2041, 0.2279, 0.2472, 0.2597, 0.2688, 0.2757, 0.2831, 0.2895, 0.2978, 0.3051, 0.3122, 0.3192, 0.3227, 0.3249, 0.3272, 0.3254, 0.3235, 0.3233, 0.3241, 0.3251, 0.3258, 0.3284, 0.3328, 0.3385, 0.3445, 0.3467, 0.3456, 0.3472]
```

**Key Takeaway**: Don't overreact to a bad week (3-15 days is noise). But if a player has been bad for 6 weeks, they are likely to stay bad.

---

### 2. Roster Management Styles

I analyzed the "Manager DNA" of every team by looking at two metrics:
1.  **Churn Rate**: How many adds per week?
2.  **Patience**: How long do they hold a player before dropping? (Avg Hold Days)

#### The "Churn" Correlation
There is a significant positive correlation (`+0.39`) between **Churn** and **Success**. Teams that made more moves generally accrued more value. In contrast, "Patience" was negatively correlated (`-0.47`) with success.

```mermaid
quadrantChart
    title "Roster Management Style"
    x-axis "Patience (Avg Hold Time)" --> "Stubborness"
    y-axis "Low Value" --> "High Value"
    quadrant-1 "Diamond Hands (High Value)"
    quadrant-2 "Churn & Burn (High Value)"
    quadrant-3 "Panic Dropper (Low Value)"
    quadrant-4 "Sleeping at Wheel (Low Value)"
    PJR: [0.36, 0.95]
    HILL: [0.06, 0.82]
    AFFO: [0.15, 0.68]
    DO: [0.66, 0.44]
    CHER: [0.07, 0.40]
    ELLI: [0.31, 0.33]
    BP: [0.05, 0.31]
    YBSD: [0.95, 0.29]
    GIBB: [0.90, 0.29]
    $$$: [0.68, 0.05]
```

**Quadrant Analysis**:
- **Top Left (High Value, High Churn)**: This is the sweet spot. Teams like **HILL** and **AFFO** lived here.
- **Top Right (High Value, High Patience)**: **PJR** (Me) is the outlier here. High value despite stubbornly holding players. This indicates a dominant draft class.
- **Bottom Right (Low Value, High Patience)**: The "Sleeping at the Wheel" quadrant. Teams like **DO**, **YBSD**, and **GIBB** held players for 100+ days and finished at the bottom.

---

### 3. Member Breakdown & Optimal Benchmarks

Based on the **Top 3 Teams**, the "Optimal" strategy for our league is:
- **Target Churn**: `2.2` Adds per Week.
- **Target Hold Limit**: `~60` Days for underperformers.

| Team | Total Value | Adds/Week | vs Optimal | Avg Hold |
|---|---|---|---|---|
| **PJR** (Me) | **1385.6** | 1.2 | <span style="color:red">-1.0 (Too Passive)</span> | 82.0d |
| **HILL** | 1271.4 | **3.1** | +0.9 (Aggressive) | **45.4d** |
| **AFFO** | 1143.9 | 2.3 | +0.1 (Optimal) | 56.7d |
| **DO** | 926.0 | 0.5 | -1.8 | 117.1d |
| **CHER** | 889.2 | 2.8 | +0.6 | 47.2d |
| **ELLI** | 826.5 | 1.4 | -0.8 | 75.6d |
| **BP** | 809.5 | 3.3 | +1.0 | 44.6d |
| **YBSD** | 788.8 | 0.1 | -2.1 | 152.2d |
| **GIBB** | 788.4 | 0.3 | -1.9 | 146.4d |
| **$$$** | 574.3 | 0.5 | -1.8 | 120.1d |

---

[Home](https://pjrigali.github.io)

*Last Updated: 2026-02-16*
