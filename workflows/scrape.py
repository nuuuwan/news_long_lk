
from news import NewsLetter


def main():
    # limit = 1 if os.name == 'nt' else 5
    # for scraper in ScraperFactory.list():
    #     scraper().scrape(limit=limit)

    # Article.build_readme()
    NewsLetter().build()


if __name__ == "__main__":
    main()
