from django.core.management import BaseCommand

from events.application.import_kronolive_sections.import_kronolive_section_command import  ImportKronoliveSectionCommand
from events.application.import_kronolive_sections.import_kronolive_section_command_handler import  ImportKronoliveSectionCommandHandler
from events.domain.section.section_creator import SectionCreator
from events.infraestructure.db_event_repository import DbEventRepository
from events.infraestructure.db_section_repository import DbSectionRepository
from events.infraestructure.kronolive_section_importer import KronoliveSectionImporter



class Command(BaseCommand):
    help = 'Import kronolive section'

    def __init__(self):
        super().__init__()
        self.__section_creator = SectionCreator()
        self.__db_section_repository = DbSectionRepository()
        self.__section_creator = SectionCreator()
        self.__section_importer = KronoliveSectionImporter()
        self.__db_event_repository = DbEventRepository()
        self.__import_kronolive_section_command_handler = ImportKronoliveSectionCommandHandler(
            section_creator=self.__section_creator,
            section_repository=self.__db_section_repository,
            section_importer=self.__section_importer,
            event_repository=self.__db_event_repository
        )

    def handle(self, *args, **options):
        command = ImportKronoliveSectionCommand()
        self.__import_kronolive_section_command_handler.handle(command)
