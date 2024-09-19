from django.core.management import BaseCommand

from events.application.import_kronolive_inscriptions.import_kronolive_inscriptions_command import ImportKronoliveInscriptionsCommand
from events.application.import_kronolive_inscriptions.import_kronolive_inscriptions_command_handler import ImportKronoliveInscriptionsCommandHandler
from events.domain.competitor.competitor_creator import CompetitorCreator
from events.domain.inscription.inscription_creator import InscriptionCreator
from events.infraestructure.db_competitor_repository import DbCompetitorRepository
from events.infraestructure.db_event_repository import DbEventRepository
from events.infraestructure.db_inscription_repository import DbInscriptionRepository
from events.infraestructure.kronolive_inscriptions_importer import KronoliveInscriptionsImporter


class Command(BaseCommand):
    help = 'Import inscriptions from Kronolive'

    def __init__(self):
        super().__init__()
        self.__kronolive_inscriptions_importer = KronoliveInscriptionsImporter()
        self.__inscription_creator = InscriptionCreator()
        self.__db_inscription_repository = DbInscriptionRepository()
        self.__db_competitor_repository = DbCompetitorRepository()
        self.__competitor_creator = CompetitorCreator()
        self.__db_event_repository = DbEventRepository()
        self.__import_kronolive_inscriptions_command_handler = ImportKronoliveInscriptionsCommandHandler(
            inscriptions_importer=self.__kronolive_inscriptions_importer,
            inscription_creator=self.__inscription_creator,
            inscription_repository=self.__db_inscription_repository,
            competitor_repository=self.__db_competitor_repository,
            competitor_creator=self.__competitor_creator,
            event_repository=self.__db_event_repository
            )

    def handle(self, *args, **options):
        command = ImportKronoliveInscriptionsCommand()
        self.__import_kronolive_inscriptions_command_handler.handle(command)
