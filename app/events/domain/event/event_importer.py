from abc import abstractmethod, ABC

from events.domain.event.event import Event


class EventImporter(ABC):
    @abstractmethod
    def import_event(self) -> Event:
        pass