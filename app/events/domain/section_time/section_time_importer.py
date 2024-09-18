from abc import ABC, abstractmethod
from typing import List, Dict

from events.domain.event.event import Event


class SectionTimeImporter(ABC):
    @abstractmethod
    def section_time_importer(self, event:Event) -> List[Dict]:
        pass
