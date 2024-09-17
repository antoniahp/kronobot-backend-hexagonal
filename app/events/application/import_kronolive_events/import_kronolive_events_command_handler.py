from datetime import datetime

from cqrs.commands.command_handler import CommandHandler
from events.application.import_kronolive_events.import_kronolive_events_command import ImportKronoliveEventsCommand
from events.domain.event.event_creator import EventCreator
from events.domain.event.event_importer import EventImporter
from events.domain.event.event_provider_choices import EventProviderChoices
from events.domain.event.event_repository import EventRepository


class ImportKronoliveEventsCommandHandler(CommandHandler):
    def __init__(self, event_creator: EventCreator, event_repository: EventRepository, event_importer:EventImporter):
        self.__event_creator = event_creator
        self.__event_repository = event_repository
        self.__event_importer = event_importer

    def handle(self, command:ImportKronoliveEventsCommand):
        events = self.__event_importer.import_events()
        for event in events:
             filtered_event = self.__event_repository.filter_event(event_external_id=event["event_external_id"])
             if not filtered_event:
                created_event = self.__event_creator.create_event(
                    event_external_id=event["event_external_id"],
                    name=event["name"],
                    start_date=datetime.strptime(event["start_date"], '%d/%m/%Y'),
                    end_date=datetime.strptime(event["start_date"], '%d/%m/%Y'),
                    category=event["category"],
                    description=None,
                    picture=None,
                    provider_name=EventProviderChoices.KRONOLIVE.value
                )

                self.__event_repository.save_event(created_event)
