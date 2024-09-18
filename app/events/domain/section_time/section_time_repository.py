from abc import abstractmethod, ABC
from events.domain.section_time.section_time import SectionTime


class SectionTimeRepository(ABC):
    @abstractmethod
    def save_section_time(self, section_time: SectionTime) -> None:
        pass
