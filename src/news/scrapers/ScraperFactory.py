from news.scrapers.custom import (FTLK, HBR, DailyMirrorLK, EconomistIU,
                                  MITTechReview)


class ScraperFactory:
    @staticmethod
    def list():
        return [
            FTLK,
            DailyMirrorLK,
            MITTechReview,
            HBR,
            EconomistIU,
        ]
