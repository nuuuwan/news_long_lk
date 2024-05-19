import os
import re
from dataclasses import dataclass

from utils import Hash, JSONFile


@dataclass
class ArticleHead:
    DIR_DATA = os.path.join('data', 'articles')

    url: str
    date_id: str
    title: str

    @property
    def dir_path(self):
        h = Hash.md5(self.url)[:8]
        title_part = re.sub(r'\W+', ' ', self.title.lower())
        title_part = re.sub(r'\s+', ' ', title_part)[:24].strip()
        title_part = title_part.replace(' ', '-')
        dir_name = f'{title_part}.{h}'
        return os.path.join(ArticleHead.DIR_DATA, dir_name)

    @property
    def article_file(self):
        return JSONFile(os.path.join(self.dir_path, 'article.json'))
