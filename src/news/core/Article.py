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
        log.info(f'Wrote {self.article_file.path}')


    def save_readme(self):
        readme_file = JSONFile(os.path.join(self.dir_path, 'README.md'))
        lines = [
            f'# {self.title}',
            '',
            f'*[{self.time_str}]({self.url})*',
            '',
        ] + [paragraph +'\n' for paragraph in self.body_paragraphs] + ['']
        readme_file.write_lines(lines)
        log.info(f'Wrote {readme_file.path}')