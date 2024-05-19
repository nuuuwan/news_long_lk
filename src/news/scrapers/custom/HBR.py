from utils import Log, TimeFormat

from news.core import Article, ArticleHead
from news.scrapers.Scraper import Scraper

log = Log('HBR')


class HBR(Scraper):
    @property
    def url_index(self):
        return 'https://hbr.org/the-latest'

    @property
    def is_dynamic(self):
        return True

    def get_article_head_list_from_soup(self, soup) -> list:
        elem_article_summary_list = soup.find_all('stream-item')

        article_head_list = []
        for elem_article_summary in elem_article_summary_list:
            a = elem_article_summary.find('a')
            url_base = a['href']
            url = f'https://hbr.org{url_base}'
            title = elem_article_summary.text.strip().split('\n')[0]
            article_head = ArticleHead(url=url, title=title)
            article_head_list.append(article_head)
        return article_head_list

    def scrape_article_nocache(self, article_head, soup):
        elem_meta = soup.find(
            'meta', attrs={'property': 'article:published_time'}
        )
        time_str = elem_meta['content']
        ut = TimeFormat('%Y-%m-%dT%H:%M:%S%z').parse(time_str).ut
        log.debug(f'{ut=}')

        content = soup.find('div', {'class': 'standard--container'}).text
        body_paragraphs = Scraper.parse_body_paragraphs(content)

        return Article(
            url=article_head.url,
            title=article_head.title,
            ut=ut,
            body_paragraphs=body_paragraphs,
        )
