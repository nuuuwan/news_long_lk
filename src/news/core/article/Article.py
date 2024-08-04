import os

from utils import JSONFile, Log

from news.core.article.ArticleAIImage import ArticleAIImage
from news.core.article.ArticleAIText import ArticleAIText
from news.core.article.ArticleBase import ArticleBase
from news.core.article.ArticleMetadata import ArticleMetadata
from news.core.article.ArticleReadMe import ArticleReadMe

log = Log("Article")


class Article(
    ArticleBase, ArticleReadMe, ArticleAIImage, ArticleAIText, ArticleMetadata
):
    DIR_DATA = os.path.join("data", "articles")

    @staticmethod
    def from_file(article_file):
        d = article_file.read()
        return Article.from_dict(d)

    @staticmethod
    def list_all():
        articles = []
        for child_dir in os.listdir(Article.DIR_DATA):
            article_file = JSONFile(
                os.path.join(Article.DIR_DATA, child_dir, "article.json")
            )
            if article_file.exists:
                article = Article.from_file(article_file)
                articles.append(article)
        articles.sort(
            key=lambda article: article.ut,
            reverse=True,
        )
        log.debug(f"Found {len(articles)} articles")
        return articles

    def save(self):
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)
        self.article_file.write(self.todict())
        log.debug(f"Wrote {self.article_file.path}")

    def save_all(self):
        self.save()
        self.save_readme()
