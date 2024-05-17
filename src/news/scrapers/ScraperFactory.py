from news.scrapers.custom import FTLK, DailyMirrorLK


class ScraperFactory:
    @staticmethod
    def list():
        return [
            FTLK,
            DailyMirrorLK,
        ]
