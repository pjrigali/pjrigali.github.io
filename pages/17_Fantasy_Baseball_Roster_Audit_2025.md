---
layout: default
title: "2025 Fantasy Baseball Roster Audit (Team PJR)"
description: A deep dive into Team PJR's roster management, identifying missed opportunities and dead roster spots.
permalink: /posts/Fantasy_Baseball_Roster_Audit_2025
nav_order: 2.17
---

## Project Overview

In fantasy baseball, the waiver wire is where leagues are won. But how do you know if you're making the right moves?

I conducted a rigorous audit of my 2025 roster management for Team PJR. Using Python and time-series analysis, I evaluated every roster spot against the available free agent pool to answer two questions:
1. **Who shouldn't have been on my team?** (Dead Spots)
2. **Who should I have picked up?** (Missed Opportunities)

[View League-Wide Analysis & Optimal Strategy >](pages/19_Fantasy_Baseball_League_Analysis_2025.md)

---

### Methodology

- **Data Source**: Daily player stats for the entire 2025 MLB season.
- **Value Metric**: A custom Z-Score model weighted for standard fantasy categories.
- **Evaluation Window**: **42-Day Trailing Value**. (See [League Analysis](pages/19_Fantasy_Baseball_League_Analysis_2025.md) for why this window was chosen).

---

### Key Findings

#### 1. Dead Roster Spots
The most painful insight was the number of roster spots I held that contributed **zero or negative value**. These "zombie" players (often injured or benched) dragged down the team's cumulative score.

**Frequent Offenders:**
- **Carson Kelly**: Effectively zero production from April through August.
- **Trent Grisham**: Held for long stretches with no value.
- **Matthew Boyd**: Held during rehab without production.

**Action Item:** Be more aggressive. A replacement-level streamer is infinitely better than a zero.

#### 2. The One That Got Away: Trevor Story
My analysis flagged **Trevor Story** as a massive missed opportunity. In July, my utility spots were occupied by slumping stars, while Story was putting up 1st-round value on the waiver wire.

| Date | My Drop Candidate | My Value | Better Option (Value) |
|---|---|---|---|
| **2025-07-07** | **Bryce Harper** (Slump) | -0.32 | **Trevor Story** (+1.46) |
| **2025-07-07** | **Willi Castro** | +0.36 | **Trevor Story** (+1.46) |

*Note: The model boldly suggested dropping a slumping Harper. While I wouldn't cut a keeper, this screams "Bench Harper, Pick up Story".*

#### 3. Weekly Audit Results
I ran the model as a "Weekly Checkpoint" simulation. Here is a sample of the missed opportunities it identified:

| Week of | Drop Candidate | Missed Pickup | Value Swing |
|---|---|---|---|
| **May 26** | **George Kirby** (-0.14) | **Carlos Santana** (+0.91) | +1.05 |
| **July 07** | **Willi Castro** (+0.36) | **Trevor Story** (+1.46) | +1.10 |
| **Aug 25** | **Brandon Nimmo** (-0.26) | **Lourdes Gurriel Jr.** (+1.61) | +1.87 |

---

### Conclusion

The data confirms that I was too passive. Using a **42-Day Trailing Value** metric as a weekly "cut bait" signal would have unearthed massive value from the waiver wire. Next season, I will implement an automated weekly audit to force these tough decisions.

---

#### TODO
- [x] Initial Analysis
- [x] Data Processing
- [x] Write-up
- [ ] Automate weekly alerts for 2026

---

[Home](https://pjrigali.github.io)

*Last Updated: 2026-02-16*
