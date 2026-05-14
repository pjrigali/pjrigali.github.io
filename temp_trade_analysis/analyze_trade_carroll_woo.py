"""
Description:
    Trade analysis for Corbin Carroll (OF, ARI) vs Bryan Woo (SP, SEA).
    Calculates fantasy points using the friend's league scoring system for:
    - 2025 full season actuals
    - 2026 YTD actuals
    - 2026 full season projections (extrapolated + projected file)

Source Data:
    - data-lake/01_Bronze/fantasy_baseball/stats_mlb_daily_2026.csv
    - data-lake/01_Bronze/fantasy_baseball/mlb_hitting_2025_20260215.csv
    - data-lake/01_Bronze/fantasy_baseball/mlb_pitching_2025_20260215.csv
    - data-lake/01_Bronze/fantasy_baseball/player_batter_projections_2026.csv
    - data-lake/01_Bronze/fantasy_baseball/player_pitcher_projections_2026.csv

Outputs:
    Printed summary table to console.
"""

import csv
from collections import defaultdict

BASE = r"C:\Users\peter.rigali\Desktop\acn_repo\data-lake\01_Bronze\fantasy_baseball"

# ---------------------------------------------------------------------------
# Scoring system (friend's league)
# ---------------------------------------------------------------------------
# Batting:  TB +1, BB +1, R +1, RBI +1, SB +1, K -1
# Pitching: IP +3 (= OUTS×1), ER -2, W +2, L -2, SV +5, BS -1,
#           K +1, H -1, BB -1, QS +5, HD +2

def batter_pts(tb, bb, r, rbi, sb, k):
    return tb + bb + r + rbi + sb - k

def pitcher_pts(outs, er, w, l, sv, bs, k, h, bb, qs, hd):
    return outs - (er * 2) + (w * 2) - (l * 2) + (sv * 5) - bs + k - h - bb + (qs * 5) + (hd * 2)

def safe(val, default=0.0):
    try:
        return float(val) if val not in ("", None) else default
    except (ValueError, TypeError):
        return default

# ---------------------------------------------------------------------------
# 2026 YTD — aggregate from stats_mlb_daily_2026.csv
# ---------------------------------------------------------------------------
CARROLL_ID = "682998"
WOO_ID     = "693433"

batter_cols = ["TB", "B_BB", "R", "RBI", "SB", "SO"]   # SO = batter strikeouts
pitcher_cols = ["OUTS", "ER", "W", "L", "SV", "SVHD", "K", "P_H", "P_BB", "QS", "HLD"]

carroll_2026 = defaultdict(float)
woo_2026     = defaultdict(float)

with open(f"{BASE}\\stats_mlb_daily_2026.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        pid = row.get("player_id", "")
        borp = row.get("b_or_p", "")
        if pid == CARROLL_ID and borp == "batter":
            for col in batter_cols:
                carroll_2026[col] += safe(row.get(col, 0))
            carroll_2026["G"] += 1
        elif pid == WOO_ID and borp == "pitcher":
            for col in pitcher_cols:
                woo_2026[col] += safe(row.get(col, 0))
            woo_2026["GS"] += safe(row.get("GS", 0))
            woo_2026["G"]  += 1

# Blown saves: SVHD includes saves+holds; SV is separate saves — approximate BS from data
# The mlb_daily file doesn't have a direct BS column; use 0 as placeholder
carroll_pts_2026 = batter_pts(
    carroll_2026["TB"], carroll_2026["B_BB"], carroll_2026["R"],
    carroll_2026["RBI"], carroll_2026["SB"], carroll_2026["SO"]
)
woo_pts_2026 = pitcher_pts(
    woo_2026["OUTS"], woo_2026["ER"], woo_2026["W"], woo_2026["L"],
    woo_2026["SV"], 0, woo_2026["K"], woo_2026["P_H"],
    woo_2026["P_BB"], woo_2026["QS"], woo_2026["HLD"]
)

games_carroll = int(carroll_2026["G"]) or 1
starts_woo    = int(woo_2026["G"]) or 1

# ---------------------------------------------------------------------------
# 2025 actuals — mlb_hitting/pitching_2025
# ---------------------------------------------------------------------------
carroll_2025 = {}
with open(f"{BASE}\\mlb_hitting_2025_20260215.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get("player_id") == CARROLL_ID or row.get("player_name") == "Corbin Carroll":
            carroll_2025 = row
            break

woo_2025 = {}
with open(f"{BASE}\\mlb_pitching_2025_20260215.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get("player_id") == WOO_ID or row.get("player_name") == "Bryan Woo":
            woo_2025 = row
            break

def carroll_pts_from_season(row):
    tb  = safe(row.get("totalBases"))
    bb  = safe(row.get("baseOnBalls"))
    r   = safe(row.get("runs"))
    rbi = safe(row.get("rbi"))
    sb  = safe(row.get("stolenBases"))
    k   = safe(row.get("strikeOuts"))
    return batter_pts(tb, bb, r, rbi, sb, k), tb, bb, r, rbi, sb, k

def woo_pts_from_season(row):
    ip   = safe(row.get("inningsPitched"))
    outs = ip * 3
    er   = safe(row.get("earnedRuns"))
    w    = safe(row.get("wins"))
    l    = safe(row.get("losses"))
    sv   = safe(row.get("saves"))
    k    = safe(row.get("strikeOuts"))
    h    = safe(row.get("hits"))
    bb   = safe(row.get("baseOnBalls"))
    gs   = safe(row.get("gamesStarted"))
    # qualityStarts not in mlb_pitching file — estimate at 65% of GS for a sub-3 ERA SP
    qs   = round(gs * 0.65)
    hd   = safe(row.get("holds", 0))
    bs   = safe(row.get("blownSaves", 0))
    return pitcher_pts(outs, er, w, l, sv, bs, k, h, bb, qs, hd), ip, er, w, l, sv, k, h, bb, qs, hd

pts_carroll_2025, tb25, bb25, r25, rbi25, sb25, k25 = carroll_pts_from_season(carroll_2025)
pts_woo_2025, ip25, er25, w25, l25, sv25, k25p, h25, bb25p, qs25, hd25 = woo_pts_from_season(woo_2025)

g25_c = safe(carroll_2025.get("gamesPlayed", 162)) or 162
gs25_w = safe(woo_2025.get("gamesStarted", 30)) or 30

# ---------------------------------------------------------------------------
# 2026 projections
# ---------------------------------------------------------------------------
carroll_proj = {}
with open(f"{BASE}\\player_batter_projections_2026.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row.get("Player", "").replace("\xa0", " ")
        if "Carroll" in name:
            carroll_proj = row
            break

woo_proj = {}
with open(f"{BASE}\\player_pitcher_projections_2026.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row.get("Player", "").replace("\xa0", " ")
        if "Woo" in name and "Bryan" in name:
            woo_proj = row
            break

def carroll_pts_from_proj(row):
    # Projection file headers: Player,AB,R,HR,RBI,SB,AVG,OBP,H,2B,3B,BB,SO,SLG,OPS
    h   = safe(row.get("H"))
    hr  = safe(row.get("HR"))
    b2  = safe(row.get("2B"))
    b3  = safe(row.get("3B"))
    tb  = h + b2 + (2 * b3) + (3 * hr)   # TB = H + 2B + 2*3B + 3*HR
    bb  = safe(row.get("BB"))
    r   = safe(row.get("R"))
    rbi = safe(row.get("RBI"))
    sb  = safe(row.get("SB"))
    k   = safe(row.get("SO"))
    return batter_pts(tb, bb, r, rbi, sb, k), tb, bb, r, rbi, sb, k

def woo_pts_from_proj(row):
    # Projection file headers: Player,IP,K,W,SV,ERA,WHIP,ER,H,BB,HR,G,GS,L,CG
    ip   = safe(row.get("IP"))
    outs = ip * 3
    er   = safe(row.get("ER"))
    w    = safe(row.get("W"))
    l    = safe(row.get("L"))
    sv   = safe(row.get("SV"))
    k    = safe(row.get("K"))
    h    = safe(row.get("H"))
    bb   = safe(row.get("BB"))
    gs   = safe(row.get("GS"))
    qs   = gs * 0.65   # approx QS as 65% of GS for a good SP
    hd   = 0
    bs   = 0
    return pitcher_pts(outs, er, w, l, sv, bs, k, h, bb, qs, hd), ip, er, w, l, sv, k, h, bb, qs

pts_carroll_proj, tb_p, bb_p, r_p, rbi_p, sb_p, k_p = carroll_pts_from_proj(carroll_proj)
pts_woo_proj, ip_p, er_p, w_p, l_p, sv_p, k_p2, h_p, bb_p2, qs_p = woo_pts_from_proj(woo_proj)
gs_proj_woo = safe(woo_proj.get("GS", 31))

# ---------------------------------------------------------------------------
# Per-game pace calculations
# ---------------------------------------------------------------------------
ppg_carroll_2026 = carroll_pts_2026 / games_carroll
ppg_woo_2026     = woo_pts_2026 / starts_woo
ppg_carroll_2025 = pts_carroll_2025 / g25_c
ppg_woo_2025     = pts_woo_2025 / gs25_w

# ---------------------------------------------------------------------------
# Print report
# ---------------------------------------------------------------------------
SEP = "=" * 70

print(SEP)
print("TRADE ANALYSIS: Corbin Carroll (OF/ARI)  vs  Bryan Woo (SP/SEA)")
print("Scoring: TB+1 BB+1 R+1 RBI+1 SB+1 K-1 | IP×3 ER-2 W+2 L-2 SV+5 BS-1 K+1 H-1 BB-1 QS+5 HD+2")
print(SEP)

print("\n--- CORBIN CARROLL (batter) ---")
print(f"  2025 Season  : G={int(g25_c)}, TB={int(safe(carroll_2025.get('totalBases')))}, BB={int(bb25)}, R={int(r25)}, RBI={int(rbi25)}, SB={int(sb25)}, K={int(k25)}  →  {int(pts_carroll_2025)} pts  ({ppg_carroll_2025:.1f} pts/game)")
print(f"  2026 YTD     : G={games_carroll}, TB={int(carroll_2026['TB'])}, BB={int(carroll_2026['B_BB'])}, R={int(carroll_2026['R'])}, RBI={int(carroll_2026['RBI'])}, SB={int(carroll_2026['SB'])}, K={int(carroll_2026['SO'])}  →  {int(carroll_pts_2026)} pts  ({ppg_carroll_2026:.1f} pts/game)")
print(f"  2026 Proj    : TB={int(tb_p)}, BB={int(bb_p)}, R={int(r_p)}, RBI={int(rbi_p)}, SB={int(sb_p)}, K={int(k_p)}  →  {int(pts_carroll_proj)} pts proj season")

print("\n--- BRYAN WOO (starter) ---")
print(f"  2025 Season  : GS={int(gs25_w)}, IP={ip25:.1f}, ER={int(er25)}, W={int(w25)}, L={int(l25)}, SV={int(sv25)}, K={int(k25p)}, H={int(h25)}, BB={int(bb25p)}, QS={int(qs25)}, HD={int(hd25)}  →  {int(pts_woo_2025)} pts  ({ppg_woo_2025:.1f} pts/start)")
print(f"  2026 YTD     : G={starts_woo}, OUTS={int(woo_2026['OUTS'])}, ER={int(woo_2026['ER'])}, W={int(woo_2026['W'])}, L={int(woo_2026['L'])}, K={int(woo_2026['K'])}, H={int(woo_2026['P_H'])}, BB={int(woo_2026['P_BB'])}, QS={int(woo_2026['QS'])}  →  {int(woo_pts_2026)} pts  ({ppg_woo_2026:.1f} pts/start)")
print(f"  2026 Proj    : GS={int(gs_proj_woo)}, IP={ip_p:.1f}, ER={int(er_p)}, W={int(w_p)}, L={int(l_p)}, K={int(k_p2)}, H={int(h_p)}, BB={int(bb_p2)}, QS~{int(qs_p)}  →  {int(pts_woo_proj)} pts proj season")

print("\n--- PROJECTED FULL SEASON FANTASY POINTS COMPARISON ---")
print(f"  Carroll 2026 pace  : {ppg_carroll_2026:.1f} pts/game × 162 games = {int(ppg_carroll_2026 * 162)} pts")
print(f"  Woo 2026 pace      : {ppg_woo_2026:.1f} pts/start × {int(gs_proj_woo)} starts = {int(ppg_woo_2026 * gs_proj_woo)} pts")
print(f"  Carroll proj file  : {int(pts_carroll_proj)} pts")
print(f"  Woo proj file      : {int(pts_woo_proj)} pts")

print("\n--- VERDICT ---")
diff_proj = pts_woo_proj - pts_carroll_proj
diff_pace = (ppg_woo_2026 * gs_proj_woo) - (ppg_carroll_2026 * 162)
print(f"  Projected pts advantage (Woo over Carroll): {int(diff_proj)} pts (projection file)")
print(f"  2026 pace advantage   (Woo over Carroll):   {int(diff_pace)} pts")
print(SEP)
