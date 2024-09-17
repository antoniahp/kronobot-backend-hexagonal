from typing import Optional

from events.domain.inscription.inscription import Inscription


class InscriptionCreator:
    def create_inscription(self, event_id: str, car: str, category: str, dorsal: str, pilot_id: str, copilot_id: Optional[str] = None) -> Inscription:
        return Inscription(
            event_id=event_id,
            car=car,
            category=category,
            dorsal=dorsal,
            pilot_id=pilot_id,
            copilot_id=copilot_id
        )