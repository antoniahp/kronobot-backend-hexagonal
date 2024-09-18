from abc import abstractmethod, ABC

from events.domain.section.section import Section
from events.domain.section.section_repository import SectionRepository


class DbSectionRepository(SectionRepository):

    def save_section(self, section: Section) -> None:
        section.save()