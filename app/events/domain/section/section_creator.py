from uuid import UUID

from events.domain.section.section import Section


class SectionCreator:
    def create_section(self, name: str, code: str, event_id: UUID):
        return Section(
            name=name,
            code=code,
            event_id=event_id
        )