from utils import Log, TimeFormat

from news.core import Article, ArticleHead
from news.scrapers.Scraper import Scraper

log = Log('FTLK')


class FTLK(Scraper):
    @property
    def url_index(self):
        return 'https://www.ft.lk/opinion/14'

    def get_article_head_list_from_soup(self, soup) -> list:
        div_article_summary_list = soup.find_all('div', {'class': 'col-md-6'})
        article_head_list = []
        for div_article_summary in div_article_summary_list:
            a = div_article_summary.find('a')
            url = a['href']
            title = div_article_summary.find('h3').text.strip()
            article_head = ArticleHead(url=url, title=title)
            article_head_list.append(article_head)
        return article_head_list

    def scrape_article_nocache(self, article_head, soup):
        meta_data_published = soup.find(
            'meta', attrs={'itemprop': 'datePublished'}
        )
        time_str = meta_data_published['content']
        ut = TimeFormat('%Y-%m-%d %H:%M:%S').parse(time_str).ut
        content = soup.find('header', {'class': 'inner-content'}).text
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
