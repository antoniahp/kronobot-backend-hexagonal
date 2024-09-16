from events.domain.event.event import Event
from events.domain.event.event_importer import EventImporter


class KronoliveEventImporter(EventImporter):

    def import_event(self) -> Event:
        pass