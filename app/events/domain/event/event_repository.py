from abc import abstractmethod, ABC
from datetime import datetime
from typing import Optional, List

from events.domain.event.event import Event


class EventRepository(ABC):
    @abstractmethod
    def filter_event(self, event_external_id: Optional[str] = None, name: Optional[str]= None, category: Optional[str]= None, start_date__gte:Optional[datetime]= None, end_date__lte:Optional[datetime]= None ) -> List[Event]:
        pass

    @abstractmethod
    def save_event(self, event: Event) -> None:
        pass