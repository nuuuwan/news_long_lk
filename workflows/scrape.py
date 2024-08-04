import os

from news import Article, ScraperFactory


def main():
    TEST_MODE = os.name == "nt"
    limit = 1 if TEST_MODE else 5
    for scraper in ScraperFactory.list():
        scraper().scrape(limit=limit)
        if TEST_MODE:
            break

    Article.build_readme()
    Article.build_metadata()


if __name__ == "__main__":
    main()
