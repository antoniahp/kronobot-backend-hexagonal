from typing import Optional

from events.domain.competitor.competitor import Competitor


class CompetitorCreator:
    def create_competitor(self, event_id: str, name: str, image:Optional[str] = None) -> Competitor:
        return Competitor(
            event_id=event_id,
            name=name,
            image=image
        )
