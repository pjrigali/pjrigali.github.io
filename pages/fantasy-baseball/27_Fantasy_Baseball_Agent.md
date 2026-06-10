---
layout: default
title: "27_Fantasy Baseball Agent"
description: An AI-powered fantasy baseball agent that automates daily data collection, roster analysis, trade evaluation, streamer finding, keeper analysis, and weekly prep reports for ESPN H2H leagues.
permalink: /fantasy-baseball/fantasy-baseball-agent
parent: Fantasy Baseball
nav_order: 27
nav_exclude: true
---

# ⚾ Fantasy Baseball Agent

An open-source, AI-powered agent built for ESPN H2H 5×5 category leagues. Automates everything from daily data collection to weekly prep reports — so you spend less time pulling numbers and more time making decisions.

**Repository:** [github.com/pjrigali/fantasy-baseball-agent](https://github.com/pjrigali/fantasy-baseball-agent)

---

## Project Overview

Managing a competitive fantasy baseball team requires constant attention — daily waiver wire checks, matchup previews, trade evaluation, keeper decisions. This agent centralizes all of that into a single Python codebase backed by the ESPN Fantasy API and MLB Stats API.

The agent is modular by design. Each component (data collection, scoring, team management, trade analysis, draft) works independently but chains together into automated workflows. It supports any ESPN H2H league with any scoring configuration — settings are fetched dynamically from your league rather than hardcoded.

---

## Key Features

- **Live matchup preview** — real-time H2H category standings with close-category detection
- **Roster analysis** — season and 28-day z-scores, flagged underperformers, add/drop recommendations
- **SP/RP replacement analysis** — 3-window stats (season/28d/14d), flag criteria, ranked FA replacements
- **Trade evaluator** — simulates category rank impact across all 10 league teams for any 1-for-1 swap
- **Trade finder** — scans all team pairs to surface mutually beneficial trades
- **Streamer finder** — SP streamers ranked by upcoming starts × opponent weakness, RP streamers by SVHD rate
- **Player trends** — hot/cold detection across 7/14/30 day windows
- **Keeper analysis** — z-score based keeper valuation with dynamic cost rules (round+N, auction salary, etc.)
- **Draft board** — full-season projected rankings across all 10 scoring categories
- **Weekly prep workflow** — one command that runs all of the above and saves a markdown report

---

## League Configuration

The agent reads your league's exact settings from ESPN on first run — no hardcoding required.

| Setting | What's captured |
|---|---|
| Scoring categories | R, HR, RBI, SB, OPS, ERA, WHIP, K/9, QS, SVHD (or whatever your league uses) |
| Lower-is-better flags | ERA, WHIP correctly inverted in all rankings |
| Lineup slots | C×1, 1B×1, 2B×1, SS×1, 3B×1, OF×4, 2B/SS×1, 1B/3B×1, UTIL×2, SP×5, RP×3, P×1 |
| Roster rules | Bench unlimited, move limit, lineup locktime |
| Keeper rules | Count, cost method (round+N or auction salary), deadline |
| Waiver rules | Type, process day, FAAB flag |
| Draft settings | Type (snake/auction), keeper count, draft order |
| Trade settings | Deadline, veto rules |
| Schedule | 18-week structure, matchup periods, playoff teams |

Custom league rules not tracked by ESPN (keeper cost increment, house rules, veto process) are captured interactively during first-run setup.

---

## Data Captured

### ESPN Fantasy API
| File | Content | Frequency |
|---|---|---|
| `roster_espn_season_{year}.csv` | All team rosters — player, position, injury status, lineup slot | Daily |
| `standings_espn_season_{year}.csv` | League W/L/T standings snapshot | Daily |
| `schedule_espn_season_{year}.csv` | Full 18-week matchup schedule with results | Once |
| `rankings_espn_daily_{year}.csv` | Player ownership % and start % for top 500 FAs | Daily |
| `draft_espn_season_{year}.csv` | Draft results — round, pick, player, team, keeper flag | Once |
| `settings_espn_season_{year}.json` | Full league configuration | Once per season |

### MLB Stats API
| File | Content | Frequency |
|---|---|---|
| `stats_mlb_daily_{year}.csv` | Per-game hitting and pitching stats for all MLB players — one row per player per game | Daily |

All data is stored locally in `data/raw/` and never committed to git.

---

## First-Run Setup

### 1. Install dependencies
```bash
pip install -e ".[dev]"
```

### 2. Set up ESPN credentials

The agent needs your ESPN session cookies to access your private league. See [CREDENTIALS_GUIDE.md](https://github.com/pjrigali/fantasy-baseball-agent/blob/main/CREDENTIALS_GUIDE.md) for step-by-step instructions on finding them in your browser's dev tools.

```bash
python scripts/credentials/setup_credentials.py
```

This creates `config.ini` with your ESPN `s2` cookie, `SWID`, league ID, team ID, and season year.

### 3. Fetch league settings ⚠️ Required
```bash
python scripts/data/fetch_settings_espn_season.py
```

Pulls your league's scoring categories, lineup slots, roster rules, keeper settings, and schedule from ESPN. Must be run before any scoring or analysis features work. Re-run at the start of each new season.

### 4. Run the first data collection
```bash
python scripts/workflows/run_daily_collection.py
```

Pulls current ESPN rosters and MLB boxscore stats into `data/raw/`. Schedule this to run daily.

### 5. Configure an LLM (optional)

Add to `config.ini` to enable natural language summaries:

```ini
[llm]
provider = anthropic       # anthropic | openai | google | ollama
model    = claude-sonnet-4-5

[anthropic]
api_key = sk-ant-...
```

Test the connection:
```bash
python scripts/llm/test_llm.py
```

---

## Use Cases

### Weekly Prep (Monday morning)
Run everything in one command before the matchup week starts:
```bash
python scripts/workflows/run_weekly_prep.py
```
Produces a markdown report covering: live matchup standings, hot/cold roster players, SP/RP replacement candidates, and streamer picks for the week.

### Trade Evaluation
Evaluate any proposed trade by name — partial team name matching supported:
```bash
python scripts/trade/evaluate_trade.py \
  --team-a "My Team" --player-a "Jazz Chisholm" \
  --team-b "Skubal" --player-b "Gunnar Henderson"
```
Simulates the category rank impact across all 10 league teams and returns a verdict (mutual benefit / one-sided / no benefit).

### Trade Finder
Scan the entire league for mutually beneficial 1-for-1 swaps:
```bash
python scripts/trade/find_trades.py --my-team
```

### Roster Analysis
Full add/drop recommendations with season and 28-day z-scores:
```bash
python scripts/team/analyze_roster.py
```

### Keeper Analysis
Rank keeper candidates by surplus value (implied ADP round vs keeper cost):
```bash
python scripts/draft/analyze_keepers.py
```

### Draft Board
Project all available players to a full season and rank by total category z-score:
```bash
python scripts/draft/build_draft_board.py --top 50
```

### SP / RP Replacements
Deep-dive pitcher analysis with 3-window stats and ranked FA options:
```bash
python scripts/team/analyze_sp_replacements.py
python scripts/team/analyze_rp_replacements.py
```

### Streamer Finder
Find streamable SPs by upcoming starts and opponent weakness; RPs by SVHD rate:
```bash
python scripts/analysis/find_streamers.py
```

---

## Architecture

```
agent/
├── credentials/   Load config.ini — ESPN cookies, LLM keys
├── data/          Fetch from ESPN API and MLB Stats API
├── scoring/       Dynamic category loader, z-score engine, H2H comparator
├── team/          Roster, z-score valuation, add/drop, SP/RP analysis
├── trade/         Projection engine, league-wide simulation, evaluator, finder
├── draft/         Keeper analysis, draft board rankings
├── analysis/      Matchup preview, player trends, streamer finder
├── llm/           Provider-agnostic LLM layer (Anthropic, OpenAI, Gemini, Ollama)
└── workflows/     Daily collection, weekly prep, trade scan, draft prep

scripts/           CLI entry points mirroring agent/ structure
data/raw/          Collected data (gitignored)
data/processed/    Derived outputs (gitignored)
logs/              Per-script JSONL run logs (gitignored)
reports/           Generated markdown reports (gitignored)
```

---

[Home](https://pjrigali.github.io) · [Fantasy Baseball](https://pjrigali.github.io/fantasy-baseball)

*Last Updated: 2026-06-09*
