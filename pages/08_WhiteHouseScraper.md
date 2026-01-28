---
title: 08_WhiteHouseScraper
description: A deep dive into the White House News Scraper logic and design.
permalink: /posts/WhiteHouseScraper
layout: default
nav_order: 2.08
---

# White House News Scraper

A robust, modular Python-based web scraper designed to extract news articles from [whitehouse.gov/news](https://www.whitehouse.gov/news/). 

## Project Overview

The objective was to create a scraper that can efficiently collect article titles, dates, links, and full text content while avoiding duplicate work and maintaining a clean, modular codebase without relying on heavy libraries like `pandas`.

### Key Features:
- **Modular Design**: Core logic is abstracted into `white_house_functions.py` for reusability.
- **Duplicate Prevention**: A CSV-based tracking system ensures no article is scraped twice.
- **Multi-Page Support**: Orchestration logic allows for scraping any range of news pages.
- **Category Extraction**: Extracts and tracks article categories (e.g., "Articles", "Fact Sheets").
- **No Pandas Dependency**: Uses Python's native `csv` and `json` modules for high performance and low overhead.

---

## Core Implementation

### The Scraper Orchestration
The scraper iterates through pages, fetches links, checks for duplicates, and then extracts full content for new items only.

```python
def scrape_news_pages(start_page=1, end_page=1):
    """Orchestrates scraping across a range of pages."""
    init_storage()
    for page_num in range(start_page, end_page + 1):
        url = f"https://www.whitehouse.gov/news/page/{page_num}/" if page_num > 1 else "https://www.whitehouse.gov/news/"
        articles = get_article_links(url)
        
        for article in articles:
            if is_already_collected(article['title']):
                continue
            
            article['content'] = get_article_content(article['link'])
            save_article(article)
```

### Data Tracking & Storage
Individual articles are saved as JSON files in an `01_Outputs` folder. A central `article_tracking.csv` keeps a log of all collected data points.

**Tracking Schema:**
- `date_created`: The article's original published date.
- `date_collected`: Timestamp of when the data was scraped.
- `article_name`: The unique title of the article.
- `category`: The designated news category.

---

## Why No Pandas?
One of the core design constraints was the removal of `pandas`. While powerful, `pandas` is often overkill for simple CSV logging tasks. By utilizing Python's built-in `csv` module, we achieved:
1. **Faster Execution**: Lower startup time and faster write operations for single rows.
2. **Leaner Environment**: Reduced project dependencies and smaller environment footprints.
3. **Better Portability**: The scraper runs on any standard Python installation without needing complex library management.

---

*Last Updated: 2026-01-27*
