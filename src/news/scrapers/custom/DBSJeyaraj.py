from utils import Log, TimeFormat

from news.core import Article, ArticleHead
from news.scrapers.Scraper import Scraper

log = Log('DBSJeyaraj')


class DBSJeyaraj(Scraper):
    @property
    def url_index(self):
        return 'https://www.dbsjeyaraj.com/'

    def get_article_head_list_from_soup(self, soup) -> list:
        div_article_summary_list = soup.find_all('article')
        article_head_list = []
        for div_article_summary in div_article_summary_list:
            a = div_article_summary.find('a')
            url = a['href']
            title = div_article_summary.find('h1').text.strip()
            article_head = ArticleHead(url=url, title=title)
            article_head_list.append(article_head)
        return article_head_list

    def scrape_article_nocache(self, article_head, soup):
        elem_time = soup.find('time')
        time_str = elem_time['datetime']
        ut = TimeFormat('%Y-%m-%dT%H:%M:%S%z').parse(time_str).ut
        content = soup.find('div', {'class': 'entry-content'}).text
        body_paragraphs = Scraper.parse_body_paragraphs(content)

        return Article(
            url=article_head.url,
            title=article_head.title,
            ut=ut,
            body_paragraphs=body_paragraphs,
        )
