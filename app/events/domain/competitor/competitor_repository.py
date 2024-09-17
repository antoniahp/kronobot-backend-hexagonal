from abc import ABC, abstractmethod

from events.domain.competitor.competitor import Competitor


class CompetitorRepository(ABC):
    @abstractmethod
    def filter_competitor(self, name: str) -> Competitor:
        pass
    @abstractmethod
    def save_competitor(self, competitor:Competitor) -> None:
        pass