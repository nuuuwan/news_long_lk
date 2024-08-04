import os

from utils import JSONFile, Log

log = Log("ArticleReadMe")


class ArticleMetadata:
    METADATA_PATH = os.path.join("data", "articles_metadata.json")

    @classmethod
    def build_metadata(cls):
        articles = cls.list_all()
        d_list = []
        for article in articles:
            d = dict(
                title=article.title,
                url=article.url,
                ut=article.ut,
                dir_path_unix=article.dir_path_unix,
                time_str_formatted=article.time_str_formatted,
            )
            d_list.append(d)

        d_list.sort(key=lambda d: d["ut"], reverse=True)

        JSONFile(cls.METADATA_PATH).write(d_list)
        log.debug(f"Wrote {cls.METADATA_PATH}")
