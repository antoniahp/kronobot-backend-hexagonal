from django.core.management import BaseCommand

from events.application.import_kronolive_sections.import_kronolive_section_command import  ImportKronoliveSectionCommand
from events.application.import_kronolive_sections.import_kronolive_section_command_handler import  ImportKronoliveSectionCommandHandler
from events.application.import_kronolive_sections_times.import_kronolive_section_times_command_handler import ImportKronoliveSectionTimesCommandHandler
from events.domain.inscription.inscription_repository import InscriptionRepository
from events.domain.section.section_creator import SectionCreator
from events.domain.section_time.section_time_creator import SectionTimeCreator
from events.domain.section_time.section_time_importer import SectionTimeImporter
from events.infraestructure.db_event_repository import DbEventRepository
from events.infraestructure.db_inscription_repository import DbInscriptionRepository
from events.infraestructure.db_section_repository import DbSectionRepository
from events.infraestructure.db_section_time_repository import DbSectionTimeRepository
from events.infraestructure.kronolive_section_importer import KronoliveSectionImporter
from events.infraestructure.kronolive_section_time_importer import KronoliveSectionTimeImporter


class Command(BaseCommand):
    help = 'Import kronolive section'

    def __init__(self):
        super().__init__()
        self.__section_times_creator = SectionTimeCreator()
        self.__db_section_repository = DbSectionRepository()
        self.__db_section_time_repository = DbSectionTimeRepository()
        self.__kronolive_section_time_importer = KronoliveSectionTimeImporter()
        self.__db_event_repository = DbEventRepository()
        self.__db_inscription_repository = DbInscriptionRepository()
        self.__kronolive_section_importer = KronoliveSectionImporter()
        self.__import_kronolive_section_time_command_handler = ImportKronoliveSectionTimesCommandHandler(
            section_times_creator=self.__section_times_creator,
            section_repository=self.__db_section_repository,
            section_time_repository=self.__db_section_time_repository,
            section_time_importer=self.__kronolive_section_time_importer,
            event_repository=self.__db_event_repository,
            inscription_repository=self.__db_inscription_repository,
            section_importer=self.__kronolive_section_importer,
        )

    def handle(self, *args, **options):
        command = ImportKronoliveSectionCommand()
        self.__import_kronolive_section_time_command_handler.handle(command)