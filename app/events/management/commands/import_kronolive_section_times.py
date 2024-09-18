from django.core.management import BaseCommand

from events.application.import_kronolive_sections.import_kronolive_section_time_command import ImportKronoliveSectionTimeCommand
from events.application.import_kronolive_sections.import_kronolive_section_time_command_handler import ImportKronoliveSectionTimeCommandHandler
from events.domain.section.section_creator import SectionCreator
from events.domain.section_time.section_time_creator import SectionTimeCreator
from events.infraestructure.db_event_repository import DbEventRepository
from events.infraestructure.db_section_repository import DbSectionRepository
from events.infraestructure.db_section_time_repository import DbSectionTimeRepository
from events.infraestructure.kronolive_section_time_importer import KronoliveSectionTimeImporter


class KronoliveSectionTimeCommandHandler:
    pass


class KronoliveSectionTimeCommand:
    pass


class Command(BaseCommand):
    help = 'Import kronolive section'

    def __init__(self):
        super().__init__()
        self.__section_creator = SectionCreator()
        self.__db_section_repository = DbSectionRepository()
        self.__section_time_creator = SectionTimeCreator()
        self.__db_section_time_repository = DbSectionTimeRepository()
        self.__section_time_importer = KronoliveSectionTimeImporter()
        self.__db_event_repository = DbEventRepository()
        self.__import_kronolive_section_time_command_handler = ImportKronoliveSectionTimeCommandHandler(
            section_creator=self.__section_creator,
            section_repository=self.__db_section_repository,
            section_time_creator=self.__section_time_creator,
            section_time_repository=self.__db_section_time_repository,
            section_time_importer=self.__section_time_importer,
            event_repository=self.__db_event_repository
        )

    def handle(self, *args, **options):
        command = ImportKronoliveSectionTimeCommand()
        self.__import_kronolive_section_time_command_handler.handle(command)