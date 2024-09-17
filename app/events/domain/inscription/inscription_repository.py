from abc import abstractmethod, ABC
from typing import Optional

from events.domain.inscription.inscription import Inscription


class InscriptionRepository(ABC):
    @abstractmethod
    def filter_inscriptions(self, event_id:Optional[str] = None) -> bool:
        pass
    @abstractmethod
    def save_inscription(self, inscription: Inscription) -> None:
        pass
