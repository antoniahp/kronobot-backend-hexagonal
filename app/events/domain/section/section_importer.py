from abc import ABC, abstractmethod
from typing import List, Dict

from events.domain.event.event import Event


class SectionImporter(ABC):
    @abstractmethod
    def section_importer(self, event:Event) -> List[Dict]:
        pass
