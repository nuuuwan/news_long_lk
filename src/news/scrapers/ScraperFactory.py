from news.scrapers.custom import FTLK, DailyMirrorLK, MITTechReview


class ScraperFactory:
    @staticmethod
    def list():
        return [
            FTLK,
            DailyMirrorLK,
            MITTechReview,
        ][-1:]
