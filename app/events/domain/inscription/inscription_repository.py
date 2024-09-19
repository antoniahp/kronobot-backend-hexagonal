from abc import abstractmethod, ABC
from typing import Optional, List

from events.domain.inscription.inscription import Inscription


class InscriptionRepository(ABC):
    @abstractmethod
    def filter_inscriptions(self, event_id:Optional[str] = None) -> List[Inscription]:
        pass
    @abstractmethod
    def save_inscription(self, inscription: Inscription) -> None:
        pass
