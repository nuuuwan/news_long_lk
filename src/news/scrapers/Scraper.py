import os

from utils import Log

from news.core import Article, ArticleHead
from utils_future import SoupUtils

log = Log('Scraper')


class Scraper:
    DIR_ARTICLES = os.path.join('data', 'articles')
    MIN_PARAGRAPH_LENGTH = 20

    @staticmethod
    def parse_body_paragraphs(content: str) -> list:
        paragraphs = content.split('\n')
        paragraphs = [p.strip() for p in paragraphs]
        paragraphs = [
            p for p in paragraphs if len(p) > Scraper.MIN_PARAGRAPH_LENGTH
        ]
        return paragraphs

    @property
    def is_dynamic(self):
        return False

    @property
    def url_index(self):
        raise NotImplementedError

    def get_article_head_list_from_soup(self, soup) -> list:
        raise NotImplementedError

    def get_article_head_list(self) -> list:
        soup = SoupUtils.get_soup(self.url_index, self.is_dynamic)
        return self.get_article_head_list_from_soup(soup)

    def scrape_article_nocache(
        self, article_head: ArticleHead, soup
    ) -> Article:
        raise NotImplementedError

    def scrape_article(self, article_head: ArticleHead):
        article_file = article_head.article_file
        if article_file.exists:
            log.debug(f'{article_head.article_file.path} exists')
            return Article.from_file(article_file)
        soup = SoupUtils.get_soup(article_head.url, self.is_dynamic)
        log.debug(f'[scrape_article] {article_head=}')
        return self.scrape_article_nocache(article_head, soup)

    def scrape(self, limit: int):
        log.info(f'📰 {self.__class__.__name__}')
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
