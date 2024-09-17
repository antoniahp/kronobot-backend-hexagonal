from datetime import datetime
from typing import Optional

from events.domain.event.event import Event


class EventCreator:
    def create_event(self,
                     event_external_id: str,
                     name: str,
                     start_date: datetime,
                     category: str,
                     provider_name: str,
                     end_date: Optional[datetime] = None,
                     picture: Optional[str] = None,
                     description: Optional[str] = None,
                     ) -> Event:

        return Event(
            event_external_id=event_external_id,
            name=name,
            start_date=start_date,
            category=category,
            provider_name=provider_name,
            end_date=end_date,
            picture=picture,
            description=description
        )
