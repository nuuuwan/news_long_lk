from news.scrapers.custom import FTLK, DailyMirrorLK, MITTechReview, HBR


class ScraperFactory:
    @staticmethod
    def list():
        return [
            FTLK,
            DailyMirrorLK,
            MITTechReview,
            HBR,
        ][-1:]
