from abc import abstractmethod, ABC
from typing import List, Dict

from events.domain.event.event import Event


class EventImporter(ABC):
    @abstractmethod
    def import_events(self) -> List[Dict]:
        pass