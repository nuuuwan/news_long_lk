import os

import requests
from bs4 import BeautifulSoup
from utils import Log, Time, TimeFormat

from news.core import Article, ArticleHead

log = Log('Scraper')


class Scraper:
    DIR_ARTICLES = os.path.join('data', 'articles')

    def get_url_for_page(self, page_num: int):
        x = (page_num - 1) * 30
        return f'https://www.dailymirror.lk/opinion/231/{x}'

    @staticmethod
    def parse_date_id(date_str):
        if date_str.lower().strip().endswith('hours ago'):
            h = int(date_str.split(' ')[0])
            ut = Time.now().ut - h * 3600
            date_id = TimeFormat.DATE_ID.format(Time(ut))
            return date_id

        date_id = TimeFormat.DATE_ID.format(
            TimeFormat('%d %b %Y').parse(date_str)
        )
        return date_id

    def get_article_head_list(self, limit: int) -> list:
        page_num = 1
        article_head_list = []
        while True:
            url = self.get_url_for_page(page_num)
            log.debug(f'[get_urls] {url=}')
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            div_article_summary_list = soup.find_all(
                'div', {'class': 'col-md-8'}
            )
            for div_article_summary in div_article_summary_list:
                a = div_article_summary.find('a')
                url = a['href']
                title = div_article_summary.find('h3').text.strip()
                date_str = div_article_summary.find(
                    'span', {'class': 'gtime'}
                ).text.strip()
                date_id = Scraper.parse_date_id(date_str)

                article_head = ArticleHead(
                    url=url, date_id=date_id, title=title
                )
                article_head_list.append(article_head)
                if len(article_head_list) == limit:
                    return article_head_list
            page_num += 1

    def scrape_article(self, article_head: ArticleHead):
        article_file = article_head.article_file
        if article_file.exists:
            log.debug(f'{article_head.article_file.path} exists')
            return Article.from_file(article_file)

        log.debug(f'[scrape_article] {article_head=}')
        page = requests.get(article_head.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        meta_data_published = soup.find(
            'meta', attrs={'itemprop': 'datePublished'}
        )
        time_str = meta_data_published['content']
        ut = TimeFormat('%Y-%m-%dT%H:%M:%S%z').parse(time_str).ut
        content = soup.find('header', {'class': 'inner-content'}).text
        body_paragraphs = [
            paragraph
            for paragraph in content.split('\n')
            if paragraph.strip() != ''
        ]

        return Article(
            url=article_head.url,
            date_id=article_head.date_id,
            title=article_head.title,
            time_str=time_str,
            ut=ut,
            body_paragraphs=body_paragraphs,
        )

    def scrape(self, limit: int):
        for article_head in self.get_article_head_list(limit):
            article = self.scrape_article(article_head)
            article.save_all()
