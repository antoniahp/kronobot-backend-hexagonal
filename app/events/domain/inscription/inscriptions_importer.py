from abc import ABC, abstractmethod
from typing import List, Dict

from events.domain.event.event import Event


class InscriptionsImporter(ABC):
    @abstractmethod
    def import_inscriptions(self, event:Event) -> List[Dict]:
        pass
