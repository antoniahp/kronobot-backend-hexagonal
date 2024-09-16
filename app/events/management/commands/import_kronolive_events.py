from django.core.management import BaseCommand

from events.application.import_kronolive_events.import_kronolive_events_command import ImportKronoliveEventsCommand
from events.application.import_kronolive_events.import_kronolive_events_command_handler import ImportKronoliveEventsCommandHandler
from events.domain.event.event_creator import EventCreator
from events.domain.event.event_importer import EventImporter
from events.infraestructure.db_event_repository import DbEventRepository


class Command(BaseCommand):
    help = 'Import events form Kronolive'

    def __init__(self):
        super().__init__()
        self.__event_creator = EventCreator()
        self.__db_event_repository = DbEventRepository()
        self.__event_importer = EventImporter()
        self.__import_kronolive_events_command_handler = ImportKronoliveEventsCommandHandler(event_creator=self.__event_creator, event_repository=self.__db_event_repository, event_importer=self.__event_importer)

    def handle(self, *args, **options):
        command = ImportKronoliveEventsCommand(days_to_import_events=30)
        self.__import_kronolive_events_command_handler.handle(command)