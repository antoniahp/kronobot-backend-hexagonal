from typing import Optional

from events.domain.event.event import Event
from events.domain.inscription.inscription import Inscription
from events.domain.inscription.inscription_repository import InscriptionRepository


class DbInscriptionRepository(InscriptionRepository):

    def filter_inscriptions(self, event_id:Optional[str] = None) -> bool:
        event = Event.objects.filter(event_id=event_id)
        if event is not None:
            return True
        else:
            return False


    def save_inscription(self, inscription: Inscription) -> None:
        inscription.save()
