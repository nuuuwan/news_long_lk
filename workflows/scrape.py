import os

from news import Article, ScraperFactory


def main():
    limit = 1 if os.name == 'nt' else 5
    for scraper in ScraperFactory.list():
        scraper().scrape(limit=limit)

    Article.build_readme()


if __name__ == "__main__":
    main()
