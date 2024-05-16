import os
from dataclasses import dataclass

from utils import JSONFile, Log

from news.core.ArticleHead import ArticleHead

log = Log('Article')


@dataclass
class Article(ArticleHead):
    DIR_DATA = os.path.join('data', 'articles')

    time_str: str
    ut: int
    body_paragraphs: list[str]

    def todict(self):
        return dict(
            url=self.url,
            date_id=self.date_id,
            title=self.title,
            #
            time_str=self.time_str,
            ut=self.ut,
            body_paragraphs=self.body_paragraphs,
        )

    def save(self):
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)
        self.article_file.write(self.todict())
        log.debug(f'Wrote {self.article_file.path}')
