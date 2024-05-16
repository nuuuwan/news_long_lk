import os
import re

import requests
from bs4 import BeautifulSoup
from utils import Hash, JSONFile, Log, TimeFormat

log = Log('Scraper')


class Scraper:
    DIR_ARTICLES = os.path.join('data', 'articles')

    def get_url_for_page(self, page_num: int):
        x = (page_num - 1) * 30
        return f'https://www.dailymirror.lk/opinion/231/{x}'

    def get_article_info_list(self, limit: int) -> list[dict]:
        page_num = 1
        d_list = []
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
                date_id = TimeFormat.DATE_ID.format(
                    TimeFormat('%d %b %Y').parse(date_str)
                )

                d = dict(url=url, date_id=date_id, title=title)
                d_list.append(d)
                if len(d_list) == limit:
                    return d_list
            page_num += 1

    @staticmethod
    def get_file_name(url: str, date_id: str, title: str):
        h = Hash.md5(url)[:8]
        title_part = re.sub(r'\W+', ' ', title.lower())
        title_part = re.sub(r'\s+', ' ', title_part)[:32]
        title_part = title_part.replace(' ', '-')
        return f'{date_id}.{title_part}.{h}.json'

    def scrape_article(self, article_info: dict):
        url = article_info['url']
        date_id = article_info['date_id']
        title = article_info['title']
        file_name = Scraper.get_file_name(url, date_id, title)
        file_path = os.path.join(Scraper.DIR_ARTICLES, file_name)
        article_file = JSONFile(file_path)
        if article_file.exists:
            log.debug(f'{file_path} exists')
            return

        log.debug(f'[scrape_url] {url=}')
        page = requests.get(url)
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

        d = dict(
            url=url,
            date_id=date_id,
            ut=ut,
            time_str=time_str,
            title=title,
            body_paragraphs=body_paragraphs,
        )
        article_file.write(d)
        log.info(f'Wrote {file_path}')

    def scrape(self, limit: int):
        d_list = self.get_article_info_list(limit)
        for d in d_list:
            self.scrape_article(d)
