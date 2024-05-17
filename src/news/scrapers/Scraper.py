import os

from utils import Log

log = Log('Scraper')


class Scraper:
    DIR_ARTICLES = os.path.join('data', 'articles')

    def scrape(self, limit: int):
        for article_head in self.get_article_head_list(limit):
            article = self.scrape_article(article_head)
            article.save_all()
