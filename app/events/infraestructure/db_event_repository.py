from events.domain.event.event_repository import Event
from events.domain.event.event_repository import EventRepository
from django.db.models import Q
from datetime import datetime
from typing import List, Optional

class DbEventRepository(EventRepository):

    def filter_event(self, event_external_id: Optional[str] = None, name: Optional[str]= None, category: Optional[str]= None, start_date__gte:Optional[datetime]= None, end_date__lte:Optional[datetime]= None ) -> List[Event]:
        filters = Q()
        if event_external_id is not None:
            filters = filters & Q(event_external_id=event_external_id)
        if name is not None:
            filters = filters & Q(name=name)
        if category is not None:
            filters = filters & Q(category=category)
        if start_date__gte is not None:
            filters = filters & Q(start_date__gte=start_date__gte)
        if end_date__lte is not None:
            filters = filters & Q(end_date__lte=end_date__lte)

        events = Event.objects.filter(filters)
        return events


    def save_event(self, event: Event) -> None:
        event.save()
