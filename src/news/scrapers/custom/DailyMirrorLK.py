from utils import Log, TimeFormat

from news.core import Article, ArticleHead
from news.scrapers.Scraper import Scraper

log = Log("DailyMirrorLK")


class DailyMirrorLK(Scraper):
    @property
    def url_index(self):
        return "https://www.dailymirror.lk/opinion/231"

    def get_article_head_list_from_soup(self, soup) -> list:
        div_article_summary_list = soup.find_all("div", {"class": "col-md-8"})
        article_head_list = []
        for div_article_summary in div_article_summary_list:
            a_list = div_article_summary.find_all("a")
            a = None
            for a in a_list:
                if "http" not in a["href"]:
                    continue
            url = a["href"]
            elem_h3 = div_article_summary.find("h3")
            if not elem_h3:
                continue
            title = elem_h3.text.strip()
            article_head = ArticleHead(url=url, title=title)
            article_head_list.append(article_head)
        return article_head_list

    def scrape_article_nocache(self, article_head, soup):
        meta_data_published = soup.find("meta", attrs={"itemprop": "datePublished"})
        time_str = meta_data_published["content"]
        ut = TimeFormat("%Y-%m-%d %H:%M:%S").parse(time_str).ut
        content = soup.find("div", {"class": "a-content"}).text
        body_paragraphs = Scraper.parse_body_paragraphs(content)

        return Article(
            url=article_head.url,
            title=article_head.title,
            ut=ut,
            body_paragraphs=body_paragraphs,
        )
