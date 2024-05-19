from news.scrapers.custom import (FTLK, HBR, DailyMirrorLK, EconomistIU,
                                  MITTechReview, DBSJeyaraj)


class ScraperFactory:
    @staticmethod
    def list():
        return [
            FTLK,
            DailyMirrorLK,
            MITTechReview,
            HBR,
            EconomistIU,
            DBSJeyaraj,
        ][-1:]
