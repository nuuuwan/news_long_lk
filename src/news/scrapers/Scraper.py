import os

import requests
from bs4 import BeautifulSoup
from utils import Log

from news.core import Article, ArticleHead

log = Log('Scraper')


class Scraper:
    DIR_ARTICLES = os.path.join('data', 'articles')

    def scrape_article(self, article_head: ArticleHead):
        article_file = article_head.article_file
        if article_file.exists:
            log.debug(f'{article_head.article_file.path} exists')
            return Article.from_file(article_file)

        log.debug(f'[scrape_article] {article_head=}')
        page = requests.get(article_head.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        return self.scrape_article_nocache(article_head, soup)

    def scrape(self, limit: int):
        article_head_list = self.get_article_head_list()
        n_articles = len(article_head_list)
        if n_articles > limit:
            article_head_list = article_head_list[:limit]
        else:
            limit = n_articles

        log.debug(f'Scraping {limit}/{n_articles} articles')

        for article_head in article_head_list:
            article = self.scrape_article(article_head)
            article.save_all()
