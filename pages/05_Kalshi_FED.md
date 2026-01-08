---
title: 05_Kalshi Jerome Powell Speech Prediction
description: A test run for predicting Powell verbiage.
permalink: /posts/05_Kalshi_Fed
layout: default
nav_order: 2.05
---
# Prediction Markets: Probability of Jerome Powell using Kalshi words in FOMC speech.

> [Kalshi: Expected Words Said](https://kalshi.com/markets/kxfedmention/fed-mention/kxfedmention-26jan)

Essentially, what we are looking to dtermine the likelyhood Jerome Powell will say certian words.

> [Kalshi: Expected Rate Change](https://kalshi.com/markets/kxfeddecision/fed-meeting/kxfeddecision-26jan)

Keep in mind that people expect the Fed to maintain rates as they are.


## Data
We sourced the files directly from the FOMC website. These are downloaded as PDF's, opened and parsed. Most of this was done by refactoring an existing repo (noted just below)

Our data includes speeches from 2020 to present. 43 files to be exact.

> [Link to the repo used](https://github.com/BigJonP/fed-press-conference-dataset/tree/main)

> Note, Q&A is included. Though, if the word is in the question it is not counted. Only words from Jerome Powell are used.

## Code Overview

This script analyzes Federal Reserve press conference transcripts to measure how often specific words (defined by a Kalshi prediction market) are spoken by **Chair Jerome Powell**, then aggregates those results and saves them to a CSV file.

---

## Step-by-Step Description

### 1. Imports and Constants
- Imports standard libraries for regex processing, dates, and file handling.
- Imports custom Kalshi helper functions (`event`, `save_csv`).
- Defines Kalshi tickers for a word-based prediction market related to Fed mentions.

```python
import re
import datetime
from pathlib import Path
from kalshi_functions import save_csv, event

WORD_SERIES = 'KXFEDMENTION'
WORD_EVENT = 'KXFEDMENTION-26JAN'
WORD_MARKET = 'KXFEDMENTION-26JAN-PROJ'

# link -> https://kalshi.com/markets/kxfedmention/fed-mention/kxfedmention-26jan
```

---

### 2. Load and Parse Transcript Files
- Reads all `.txt` files from a directory containing FOMC press conference transcripts.
- Extracts the date from each filename and converts it into a `datetime` object.
- Stores each transcript’s:
  - filename  
  - date  
  - full text content  
  - placeholder for Jerome Powell–only text  

### 3. Extract Jerome Powell’s Speech
- Splits the transcript text using `<NAME>...</NAME>` tags.
- Identifies sections following `<NAME>CHAIR POWELL</NAME>.`.
- Concatenates only Jerome Powell’s spoken text into a single string per transcript.

```python
# Open TXT files
p = Path('..\\fed_test\\fed_press_conferences')

files = []
for file_path in p.glob('*.txt'):
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
        date_str = file_path.name.replace('FOMCpresconf', '').replace('.txt', '')
        files.append({'file_name': file_path.name, 
                      'date': datetime.datetime(year=int(float(date_str[:4])), month=int(float(date_str[4:6])), day=int(float(date_str[6:]))), 
                      'content': content,
                      'j_text': []})

# get Jerome only text.
for d in files:
    str_lst = re.split(r'(<NAME>.*?</NAME>. )', files[0]['content'])
    j_text = []
    for i, s in enumerate(str_lst):
        if s:
            if s == '<NAME>CHAIR POWELL</NAME>. ':
                j_text.append(str_lst[i + 1].strip())
    d['j_text'] = ' '.join(j_text)
```

---

### 4. Retrieve Kalshi Market Words
- Queries the Kalshi API for the specified event.
- Extracts the list of words tied to individual markets.
- Handles compound words (e.g., `"inflation / inflationary"`) by splitting them.
- Associates each word with its current market price.

```python
# Kalshi
# Get even words
categories = event(event_ticker=WORD_EVENT)

# Collect Words. Split where necessary.
word_lst = []
for c in categories['markets']:
    if '/' in c['custom_strike']['Word']:
        ws = c['custom_strike']['Word'].split(' / ')
        for w in ws:
            word_lst.append({'word': w, 'cost': float(c['last_price_dollars'])})
    else:
        word_lst.append({'word': c['custom_strike']['Word'], 'cost': float(c['last_price_dollars'])})
```

---

### 5. Count Word Mentions Per Speech
- For each transcript:
  - Initializes a counter for every tracked word.
  - Counts how many times each word appears in Jerome Powell’s text (case-insensitive).
  - Stores per-speech word counts.

```python
# Parse how many words appear in the individual speeches.
for i in files:
    word_cnt = {i['word'].lower(): 0 for i in word_lst}

    for w in word_cnt:
        word_cnt[w] += i['j_text'].lower().count(w)
    i['word_cnt'] = word_cnt
```
> Note, we are applying .lower() to the speeches and Kalshi words.
---

### 6. Aggregate Statistics Across All Speeches
- For each word:
  - Counts how many speeches included the word at least once (`said`).
  - Counts how many speeches did not (`not_said`).
  - Sums total occurrences across all speeches.
  - Computes the percentage of speeches where the word was said.

### 7. Export Results
- Merges Kalshi market data with the aggregated word statistics.
- Saves the final dataset to `2025_01_07_Fed_words.csv`.

```python
# Calc Odds and reformat for output.
final_word_cnt = {i['word'].lower(): {'said': 0, 'not_said': 0, 'count': 0, 'pct_said': 0.0} for i in word_lst}
for i in files:
    for k, v in i['word_cnt'].items():
        if v:
            final_word_cnt[k]['said'] += 1
            final_word_cnt[k]['count'] += v
        else:
            final_word_cnt[k]['not_said'] += 1


for k, v in final_word_cnt.items():
    v['pct_said'] = v['said'] / len(files)
    # print(f'{k}: ({v['said']}, {v['not_said']}, {v['count']}), ({v['said'] / len(files)})')

save_csv(file_path='2025_01_07_Fed_words.csv', data=[i | final_word_cnt[i['word'].lower()] for i in word_lst])
```

---

## Purpose

The script combines **natural language analysis** of Fed press conferences with **Kalshi market data** to estimate how frequently Jerome Powell mentions specific words and how consistently those words appear across speeches, enabling comparison with market-implied expectations.

---

## Results

Since the markets work in a binary function, the cost can be inferred as the percent likelyhood the word or phase will be said. This means where there is a delta between Cost and Pct Said, we have some alpha.

High level, its clear that there are words/phases Powell has decided not to say. We know he is very cautious about what he says so this sorta makes sense.

A few caveats, words like AI or Anchor (Probably **Anchored**) could be part of other words. Be mindful of that, the searching for the word in the speeches does not factor this in.

Key standouts are where Pct_said is greater or less than the Cost.

| Word                    | Cost | Said | Not Said | Count | Pct Said |
|-------------------------|------|------|----------|-------|----------|
| Egg                     | 0.05 | 0    | 43       | 0     | 0.0      |
| Trade War               | 0.05 | 0    | 43       | 0     | 0.0      |
| Soft Landing            | 0.07 | 4    | 39       | 8     | 0.093    |
| Bitcoin                 | 0.07 | 2    | 41       | 2     | 0.047    |
| National Debt           | 0.08 | 0    | 43       | 0     | 0.0      |
| ADP                     | 0.09 | 1    | 42       | 1     | 0.023    |
| Stagflation             | 0.10 | 1    | 42       | 3     | 0.023    |
| Anchor                  | 0.11 | 42   | 1        | 113   | 0.977    |
| Gold                    | 0.12 | 1    | 42       | 1     | 0.023    |
| Pardon                  | 0.13 | 5    | 38       | 6     | 0.116    |
| Trump                   | 0.14 | 2    | 41       | 2     | 0.047    |
| Gas                     | 0.16 | 10   | 33       | 18    | 0.233    |
| Gasoline                | 0.16 | 7    | 36       | 9     | 0.163    |
| Natural Gas             | 0.16 | 1    | 42       | 2     | 0.023    |
| Yield Curve             | 0.16 | 6    | 37       | 11    | 0.14     |
| Consumer Confidence     | 0.18 | 3    | 40       | 3     | 0.07     |
| Dot Plot                | 0.20 | 5    | 38       | 9     | 0.116    |
| Recession               | 0.23 | 23   | 20       | 56    | 0.535    |
| QE                      | 0.24 | 6    | 37       | 8     | 0.14     |
| Quantitative Easing     | 0.24 | 4    | 39       | 4     | 0.093    |
| Tax                     | 0.31 | 7    | 36       | 13    | 0.163    |
| Beige Book              | 0.33 | 6    | 37       | 10    | 0.14     |
| Volatility              | 0.35 | 6    | 37       | 8     | 0.14     |
| Probability             | 0.36 | 7    | 36       | 8     | 0.163    |
| QT                      | 0.40 | 11   | 32       | 15    | 0.256    |
| Quantitative Tightening | 0.40 | 0    | 43       | 0     | 0.0      |
| Median                  | 0.42 | 30   | 13       | 160   | 0.698    |
| Dissent                 | 0.42 | 7    | 36       | 19    | 0.163    |
| Projection              | 0.50 | 29   | 14       | 180   | 0.674    |
| Pandemic                | 0.57 | 41   | 2        | 234   | 0.953    |
| Shutdown                | 0.59 | 12   | 31       | 21    | 0.279    |
| Shut Down               | 0.59 | 2    | 41       | 3     | 0.047    |
| Tariff Inflation        | 0.59 | 4    | 39       | 13    | 0.093    |
| Softening               | 0.61 | 19   | 24       | 51    | 0.442    |
| Credit                  | 0.63 | 22   | 21       | 99    | 0.512    |
| Goods inflation         | 0.69 | 12   | 31       | 33    | 0.279    |
| AI                      | 0.80 | 43   | 0        | 2966  | 1.0      |
| Artificial Intelligence | 0.80 | 1    | 42       | 1     | 0.023    |
| Layoff                  | 0.83 | 11   | 32       | 25    | 0.256    |
| Balance Sheet           | 0.84 | 39   | 4        | 183   | 0.907    |
| Uncertainty             | 0.84 | 34   | 9        | 112   | 0.791    |
| Restrictive             | 0.85 | 30   | 13       | 199   | 0.698    |
| Unchanged               | 0.89 | 18   | 25       | 21    | 0.419    |
| Balance of Risk         | 0.94 | 24   | 19       | 66    | 0.558    |
| Expectation             | 0.95 | 43   | 0        | 322   | 1.0      |
| Good Afternoon          | 0.97 | 43   | 0        | 43    | 1.0      |

## Next Steps
Further analysis can be done around the following question: 
- *_We are assuming rates will stay the same, what is the word distribution for speeches prior to when the Fed was in that position?_*