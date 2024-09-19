from events.domain.competitor.competitor import Competitor
from events.domain.competitor.competitor_repository import CompetitorRepository


class DbCompetitorRepository(CompetitorRepository):

    def filter_competitor(self, name: str) -> Competitor:
        competitor = Competitor.objects.filter(name=name).first()
        return competitor

    def save_competitor(self, competitor:Competitor) -> None:
        competitor.save()
