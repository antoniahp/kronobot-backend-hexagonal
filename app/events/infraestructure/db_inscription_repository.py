from typing import Optional, List

from events.domain.inscription.inscription import Inscription
from events.domain.inscription.inscription_repository import InscriptionRepository


class DbInscriptionRepository(InscriptionRepository):

    def filter_inscriptions(self, event_id:Optional[str] = None) -> List[Inscription]:
        inscriptions = Inscription.objects.filter(event_id=event_id)
        return inscriptions


    def save_inscription(self, inscription: Inscription) -> None:
        inscription.save()
