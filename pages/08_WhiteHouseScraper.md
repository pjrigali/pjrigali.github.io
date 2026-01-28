---
title: 08_WhiteHouseScraper
description: A deep dive into the White House News Scraper logic and design.
permalink: /posts/WhiteHouseScraper
layout: default
nav_order: 2.08
---

# White House News Scraper

A robust, modular Python-based web scraper designed to extract news articles from [whitehouse.gov/news](https://www.whitehouse.gov/news/).

## Project Logic & Workflow

The scraper follows a structured workflow to ensure data integrity, efficiency, and reusability. By separating the orchestration from the utility functions, the project remains easy to maintain and extend.

### 1. Initialization
The process begins by ensuring the environment is ready. The `init_storage` function creates necessary directories and initializes the tracking CSV with the correct headers. It also handles migrations for existing CSV files.

```python
def init_storage():
    """Initializes the output folder and tracking CSV if they don't exist."""
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    
    headers = ['date_created', 'date_collected', 'article_name', 'category']
    # If the file exists, we verify headers and migrate if necessary
    # Otherwise, we create a fresh one
    if not os.path.exists(TRACKING_FILE):
        with open(TRACKING_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
```

### 2. Scraping Article Links
On any news catalog page, the scraper identifies individual article blocks and extracts the title, link, date, and category.

```python
def get_article_links(url):
    """Scrapes article metadata from a list page."""
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('li.wp-block-post')
    
    data = []
    for article in articles:
        title_tag = article.select_one('.wp-block-post-title a')
        meta = article.select_one('.wp-block-whitehouse-post-template__meta')
        
        data.append({
            'title': title_tag.get_text(strip=True),
            'link': title_tag['href'],
            'date': meta.find('time').get_text(strip=True),
            'category': meta.select_one('.taxonomy-category a').get_text(strip=True)
        })
    return data
```

### 3. Protecting Against Duplicates
To prevent redundant network requests and duplicate files, the scraper checks every article title against a local database (`article_tracking.csv`) before proceeding to the full-page scrape.

```python
def is_already_collected(title):
    """Checks if an article with the given title has already been collected."""
    if not os.path.exists(TRACKING_FILE):
        return False
    
    with open(TRACKING_FILE, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['article_name'] == title:
                return True
    return False
```

### 4. Fetching Full Content
For new articles, the scraper navigates to the individual article page and extracts the clean body text, removing navigation and layout elements.

```python
def get_article_content(url):
    """Scrapes the main text content of an individual article."""
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    content_div = soup.select_one('.wp-block-post-content') or soup.select_one('article')
    
    return content_div.get_text(separator='\n', strip=True) if content_div else ""
```

### 5. Data Capture & Storage
Finally, the data is saved as a version-controlled JSON file, and the central tracking CSV is updated to prevent future re-scraping.

```python
def save_article(article_data):
    """Saves article data to a JSON file and updates tracking CSV."""
    filename = f"{slugify(article_data['title'][:50])}.json"
    filepath = os.path.join(OUTPUT_FOLDER, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(article_data, f, indent=4, ensure_ascii=False)
    
    update_tracking_csv(article_data['title'], article_data['date'], article_data['category'])
```

### 6. Multi-Page Orchestration
All the above steps are managed by the orchestration function, which provides a high-level API for scraping ranges of pages.

```python
def scrape_news_pages(start_page=1, end_page=1):
    """Orchestrates scraping across a range of pages."""
    init_storage()
    for page_num in range(start_page, end_page + 1):
        url = f".../news/page/{page_num}/" if page_num > 1 else ".../news/"
        articles = get_article_links(url)
        
        for article in articles:
            if is_already_collected(article['title']):
                continue
            
            article['content'] = get_article_content(article['link'])
            save_article(article)
```

## Summary of Design
The scraper's architecture prioritizes **minimizing network overhead** by performing local checks before every external request. By using native Python modules, it remains highly performant and portable across different environments.

---

*Last Updated: 2026-01-27*
