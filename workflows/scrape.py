import os

from news import Scraper, Article


def main():
    limit = 1 if os.name == 'nt' else 5
    Scraper().scrape(limit=limit)
    Article.build_readme()

if __name__ == "__main__":
    main()
