from abc import abstractmethod, ABC
from typing import List, Optional

from events.domain.section.section import Section


class SectionRepository(ABC):
    @abstractmethod
    def filter_section(self, name:Optional[str] = None, code:Optional[str] = None, event_id:Optional[str] = None  ) -> List[Section]:
        pass

    @abstractmethod
    def save_section(self, section: Section) -> None:
        pass