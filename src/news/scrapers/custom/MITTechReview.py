import json
import re
from utils import Log, TimeFormat

from news.core import Article, ArticleHead
from news.scrapers.Scraper import Scraper

log = Log('MITTechReview')


class MITTechReview(Scraper):
    @property
    def url_index(self):
        return 'https://www.technologyreview.com/'

    @property
    def is_dynamic(self):
        return True

    def get_article_head_list_from_soup(self, soup) -> list:
        div_article_summary_list = soup.find_all(
            'div', {'class': 'swiper-slide'}
        )

        article_head_list = []
        for div_article_summary in div_article_summary_list:
            a = div_article_summary.find('a')
            url = a['href']
            title = div_article_summary.text.strip()
            article_head = ArticleHead(url=url, title=title)
            article_head_list.append(article_head)
        return article_head_list

    def scrape_article_nocache(self, article_head, soup):
        script_news_article = soup.find('script', {'id': 'NewsArticle'})
        content = script_news_article.text
        data = json.loads(content)

        time_str = data['datePublished']
        ut = TimeFormat('%Y-%m-%dT%H:%M:%S%z').parse(time_str).ut
        
        content = soup.find('div', {'id': 'content--body'}).text
        body_paragraphs = [
            paragraph
            for paragraph in content.split('\n')
            if paragraph.strip() != ''
        ]

        return Article(
            url=article_head.url,
            title=article_head.title,
            ut=ut,
            body_paragraphs=body_paragraphs,
        )
