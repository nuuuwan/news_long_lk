from news.scrapers.custom import FTLK, HBR, DailyMirrorLK, MITTechReview


class ScraperFactory:
    @staticmethod
    def list():
        return [
            FTLK,
            DailyMirrorLK,
            MITTechReview,
            HBR,
        ]
