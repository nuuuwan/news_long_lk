import os

from news import Scraper


def main():
    limit = 5 if os.name == 'nt' else 60
    print(Scraper().scrape(limit=limit))


if __name__ == "__main__":
    main()
