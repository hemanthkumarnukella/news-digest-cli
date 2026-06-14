# World News Digest CLI

A command-line Python application that fetches live news headlines, lets users save favourite articles to a CSV file, and generates summary reports using Pandas.

## Features
- Fetch top headlines by country using NewsAPI
- Save selected articles to a CSV file with duplicate detection
- Load and view saved articles
- Generate a summary report (total articles, most frequent source, source breakdown) using Pandas

## Tech Stack
- Python
- Requests (API calls)
- Pandas (data analysis)
- CSV module (file storage)

## Project Structure
news_digest/

├── main.py        # Entry point and user interaction

├── api.py         # NewsClient class - fetches and parses news

├── storage.py     # DigestManager class - save/load CSV

└── analysis.py     # Pandas-based report generation
## How to Run
1. Get a free API key from [NewsAPI](https://newsapi.org)
2. Replace the API key in `api.py`
3. Run `main.py`
4. Enter your country code (e.g. `us`, `in`, `gb`) and follow the prompts

## What I Learned
- Object-oriented design across multiple files
- API integration and JSON parsing
- File I/O and CSV handling with error handling
- Data analysis with Pandas (value_counts, DataFrames)
