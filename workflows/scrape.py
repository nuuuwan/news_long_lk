import os

from news import Scraper


def main():
    limit = 1 if os.name == 'nt' else 30
    Scraper().scrape(limit=limit)


if __name__ == "__main__":
    main()
