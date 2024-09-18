from abc import abstractmethod, ABC

from events.domain.section.section import Section


class SectionRepository(ABC):
    @abstractmethod
    def save_section(self, section: Section) -> None:
        pass