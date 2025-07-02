# python-regex-webscraper

## Overview

**python-regex-webscraper** is a Python project focused on custom web scraping using only standard libraries and regular expressions (RegEx). This repository is designed for learners and developers interested in building robust, ethical, and efficient web scrapers without relying on third-party modules like BeautifulSoup or Scrapy. By leveraging Python’s built-in modules and the power of RegEx, you can extract data from web pages, automate information retrieval, and structure content for further analysis.

This project is ideal for:
- Students practicing data extraction and pattern matching.
- Developers working in restricted environments (e.g., university assignments) where external libraries are disallowed.
- Anyone interested in understanding the fundamentals of HTML parsing and web automation from scratch.

---

## Features

- **Standard Library Only:** No external dependencies—works “out of the box” with any Python installation.
- **Customizable RegEx Extraction:** Learn to craft and use regular expressions for flexible data extraction.
- **GUI Integration Example:** Includes a Tkinter-based GUI (see `Scraping_GUI.py`) for interactive scraping and data review.
- **Database Storage:** Save and manage scraped data using SQLite.
- **Ethical Scraping Practices:** Encourages users to respect robots.txt, terms of service, and server load.
- **Sample Projects:** Real-world examples, such as headline extraction from news sites, included for learning and adaptation.
- **Open Source:** Licensed under the GNU General Public License v3.0 (GPL-3.0).

---

## Getting Started

### Prerequisites

- Python 3.x (Tested with 3.6+)
- No external libraries required.

### Usage

1. **Clone the Repository**
    ```bash
    git clone https://github.com/avro1199/python-regex-webscraper.git
    cd python-regex-webscraper
    ```

2. **Run the Example GUI**
    ```bash
    python Scraping_GUI.py
    ```

   This will launch a Tkinter application where you can select news sources, view headlines, and save reliability ratings to a local SQLite database.

3. **Customize Scrapers**
   - Modify or create RegEx patterns in your scripts to extract custom data from any web page.
   - Adapt code to suit different HTML structures or new websites.

4. **Explore Code Examples**
   - `Scraping_GUI.py` — Main GUI application with multiple sources and real RegEx scraping logic.
   - `regex_examples.py` — (Optional) Standalone RegEx extraction script templates for CLI use.

---

## Sample: Extracting Headlines with RegEx

```python
from urllib.request import urlopen
from re import findall

url = 'https://www.news.com.au/'
web_data = urlopen(url).read().decode('utf-8')
headline_regex = r'<h4 class="storyblock_title"><a.*?>([^<>]+)</a></h4>'
headlines = findall(headline_regex, web_data)
print(headlines)
```

---

## Ethical Web Scraping

- Always check the website’s robots.txt and terms of service before scraping.
- Limit request frequency to avoid overloading servers.
- Use scraping for academic, research, or personal purposes—avoid commercial use without permission.

---

## Project Structure

- `README.md`           — Project documentation (this file)
- `Scraping_GUI.py`     — Example GUI app for scraping and reviewing news headlines ![image1](image1)
- `regex_examples.py`   — (Optional) Script with command-line RegEx web scraping examples
- `LICENSE`             — GNU General Public License v3.0
- `reliability_ratings.db` — SQLite database for storing ratings (auto-created)
- `AIRobot.png`         — Themed project image for GUI

---

## Contributing

Pull requests, issues, and suggestions are welcome. Share your own custom scraping scripts or RegEx patterns!

---

## License

This project is licensed under the [GNU General Public License v3.0 (GPL-3.0)](LICENSE).

---

## Acknowledgements

- Python Software Foundation for the language and standard library.
- QUT IFB104 for the original assignment scaffolding and project inspiration.
