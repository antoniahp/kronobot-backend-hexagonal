from abc import abstractmethod, ABC
from typing import List

from events.domain.section.section import Section
from events.domain.section.section_repository import SectionRepository


class DbSectionRepository(SectionRepository):
    def filter_section(self) -> List[Section]:
        sections = Section.objects.filter()
        return sections
    def save_section(self, section: Section) -> None:
        section.save()