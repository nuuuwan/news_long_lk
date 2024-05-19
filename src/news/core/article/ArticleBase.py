from dataclasses import dataclass

from utils import Log, Time, TimeFormat
from news.core.ArticleHead import ArticleHead

log = Log('Article')


@dataclass
class ArticleBase(ArticleHead):
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

    @property
    def date_str(self):
        return TimeFormat.DATE.format(Time(self.ut))

    @property
    def dir_path_unix(self):
        return self.dir_path.replace('\\', '/')

    @classmethod
    def from_dict(cls, d):
        return cls(
            url=d['url'],
            date_id=d['date_id'],
            title=d['title'],
            #
            time_str=d['time_str'],
            ut=d['ut'],
            body_paragraphs=d['body_paragraphs'],
        )


    @property 
    def source(self):
        domain = self.url.split('/')[2]
        source = domain.replace('www.', '')
        return source
    
    @property
    def time_str_formatted(self):
        return TimeFormat('%I:%M %p, %A, %B %d, %Y').format(Time(self.ut))