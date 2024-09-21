from abc import abstractmethod, ABC
from typing import Optional

from django.core.files.uploadedfile import UploadedFile


class Notifier(ABC):
    @abstractmethod
    def notify(self, pilot_name: str, copilot_name: Optional[str], car: str, section_name: str, section_time: str, image_file: Optional[UploadedFile]) -> None:
        pass
