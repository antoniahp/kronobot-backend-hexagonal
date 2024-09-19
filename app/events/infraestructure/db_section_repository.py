from abc import abstractmethod, ABC
from typing import List, Optional

from django.db.models import Q

from events.domain.section.section import Section
from events.domain.section.section_repository import SectionRepository


class DbSectionRepository(SectionRepository):
    def filter_section(self, name:Optional[str] = None, code:Optional[str] = None) -> List[Section]:
        filters = Q()
        if name is not None:
            filters = filters & Q(name=name)
        if code is not None:
            filters = filters & Q(code=code)

        sections = Section.objects.filter(filters)
        return sections
    def save_section(self, section: Section) -> None:
        section.save()