from events.domain.section.section import Section
from events.domain.section_time.section_time_repository import SectionTimeRepository


class DbSectionTimeRepository(SectionTimeRepository):

    def save_section_time(self, section: Section) -> None:
        section.save()
