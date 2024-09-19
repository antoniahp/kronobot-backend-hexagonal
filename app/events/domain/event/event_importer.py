from abc import abstractmethod, ABC
from typing import List, Dict


class EventImporter(ABC):
    @abstractmethod
    def import_events(self) -> List[Dict]:
        pass