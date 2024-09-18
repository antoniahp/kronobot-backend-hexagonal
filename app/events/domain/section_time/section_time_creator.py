from datetime import datetime
from uuid import UUID

from events.domain.section_time.section_time import SectionTime


class SectionTimeCreator:
    def section_time_creator(self, section_id:UUID, inscription: UUID, section_time: datetime) -> SectionTime:
        return SectionTime(
            section_id=section_id,
            inscription=inscription,
            section_time=section_time
        )