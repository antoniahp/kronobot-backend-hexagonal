from abc import abstractmethod, ABC
from typing import List

from events.domain.section.section import Section


class SectionRepository(ABC):
    @abstractmethod
    def filter_section(self) -> List[Section]:
        pass

    @abstractmethod
    def save_section(self, section: Section) -> None:
        pass