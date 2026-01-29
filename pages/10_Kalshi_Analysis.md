---
layout: default
title: "Kalshi Fed Mention Analysis"
description: In-depth analysis of KXFEDMENTION word performance and availability edge.
permalink: /posts/Kalshi_Fed_Analysis
nav_order: 10
---

## Project Overview

This project analyzes the **Kalshi `KXFEDMENTION`** market series, which speculates on which words will be mentioned during Federal Reserve meetings. By processing historical data from the Kalshi API, we have identified significant patterns in word probability and market timing that can provide a statistical edge.

---

### 1. Word Track Record: Determining the "Safe Bets"

We analyzed the historical performance of specific words to determine their frequency of resulting in "Yes". The data reveals a clear divide between broad economic terms (high probability) and niche or buzzword terms (low probability).

#### Top Winners (Highest "Yes" Rate)
These words are "Safe Bets" — they appear in almost every meeting context.

| Word | Yes % | Total Count | Result |
| :--- | :--- | :--- | :--- |
| **Expectation** | 100% | 6 | ✅ Consistent Winner |
| **Balance of Risk** | 100% | 5 | ✅ Consistent Winner |
| **Energy** | 100% | 5 | ✅ Consistent Winner |
| **Projection** | 87.5% | 8 | ✅ High Probability |
| **Balance Sheet** | 83.3% | 6 | ✅ High Probability |
| **Good Afternoon** | 100% | 8 | ✅ Guaranteed (Salutation) |

#### Top Losers (Highest "No" Rate)
These words are often speculative "buzzwords" that rarely make it into official Fed discourse.

| Word | No % | Total Count | Result |
| :--- | :--- | :--- | :--- |
| **Bitcoin** | 100% | 7 | ❌ Absolute Loser |
| **Gas / Gasoline** | 100% | 7 | ❌ Absolute Loser |
| **Recession** | 71% | 7 | ❌ Poor Performer |
| **Egg** | 100% | 7 | ❌ Absolute Loser |
| **Consumer Confidence** | 100% | 6 | ❌ Absolute Loser |
| **Fort Knox** | 100% | 6 | ❌ Absolute Loser |

**Actionable Insight**: Fade the specific commodities (Gas, Eggs) and crypto-related terms. Long the bureaucratic process words (Expectation, Projection).

---

### 2. The "Late Addition" Trap

We analyzed the performance of markets that were **added after the initial event launch**. These "Late Additions" are often created in response to a news cycle or rumor (e.g., a specific scandal or sudden topic).

#### Key Statistic
> **Only 25.8%** of late additions result in "Yes".

#### Failed Late Additions (Examples)
These markets were added late in the cycle and failed to materialize.

| Event | Word | Result |
| :--- | :--- | :--- |
| KXFEDMENTION-25JUL | **Defense** | No |
| KXFEDMENTION-25JUL | **Genius** | No |
| KXFEDMENTION-25JUL | **Resign** | No |
| KXFEDMENTION-25SEP | **Fraud** | No |
| KXFEDMENTION-25SEP | **Lisa / Cook** | No |

**Actionable Insight**: **Fade the noise.** If a market is added late due to sudden hype, the statistical probability is heavily skewed towards "No".

---

### Actionable Strategy Checklist

Based on this analysis, the following checklist maximizes expected value:

1. **[ ] Long "Bureaucratic" Words**: Betting YES on words like *Expectation*, *Projection*, and *Balance of Risk*.
2. **[ ] Short "Buzzwords"**: Betting NO on *Bitcoin*, *Crypto*, and specific goods like *Eggs*.
3. **[ ] Short Late Additions**: Betting NO on any market added more than 24 hours after the series opens.

---

#### TODO
- [x] Initial historical analysis
- [ ] Automate daily scraping of new markets
- [ ] Build real-time alert bot for "Late Additions"

---

[Home](https://pjrigali.github.io)

*Last Updated: 2026-01-28*
