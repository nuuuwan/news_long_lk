import os
from dataclasses import dataclass

from utils import JSONFile, Log, Time, TimeFormat

from news.core.article.ArticleAIImage import ArticleAIImage
from news.core.article.ArticleAIText import ArticleAIText
from news.core.article.ArticleReadMe import ArticleReadMe
from news.core.ArticleHead import ArticleHead

log = Log('Article')


@dataclass
class Article(ArticleHead, ArticleReadMe, ArticleAIImage, ArticleAIText):
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

    @property
    def date_str(self):
        return TimeFormat.DATE.format(Time(self.ut))

    @property
    def dir_path_unix(self):
        return self.dir_path.replace('\\', '/')

    @staticmethod
    def from_dict(d):
        return Article(
            url=d['url'],
            date_id=d['date_id'],
            title=d['title'],
            #
            time_str=d['time_str'],
            ut=d['ut'],
            body_paragraphs=d['body_paragraphs'],
        )

    @staticmethod
    def from_file(article_file):
        d = article_file.read()
        return Article.from_dict(d)

    @staticmethod
    def list_all():
        articles = []
        for child_dir in os.listdir(Article.DIR_DATA):
            article_file = JSONFile(
                os.path.join(Article.DIR_DATA, child_dir, 'article.json')
            )
            if article_file.exists:
                article = Article.from_file(article_file)
                articles.append(article)
        articles.sort(
            key=lambda article: article.ut,
            reverse=True,
        )
        log.debug(f'Found {len(articles)} articles')
        return articles

    def save(self):
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)
        self.article_file.write(self.todict())
        log.info(f'Wrote {self.article_file.path}')

    def save_all(self):
        self.save()
        self.ai_summary
        self.ai_follow_ups
        self.save_readme()
