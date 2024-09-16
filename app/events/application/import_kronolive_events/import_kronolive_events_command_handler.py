from cqrs.commands.command_handler import CommandHandler
from events.application.import_kronolive_events.import_kronolive_events_command import ImportKronoliveEventsCommand
from events.domain.event.event_creator import EventCreator
from events.domain.event.event_importer import EventImporter
from events.domain.event.event_repository import EventRepository


class ImportKronoliveEventsCommandHandler(CommandHandler):
    def __init__(self, event_creator: EventCreator, event_repository: EventRepository, event_importer:EventImporter()):
        self.__event_creator = event_creator
        self.__event_repository = event_repository
        self.__event_importer = event_importer

    def handle(self, command:ImportKronoliveEventsCommand):
        events = self.__event_importer.import_kronolive_events()
        for event in events:
            filtered_event = self.__event_repository.filter_event(event_external_id=event.external_event_id)
            if filtered_event != 0:
                raise Exception("El evento ya existe")
            else:
                created_event = self.__event_creator.create_event(
                    event_external_id=events.external_event_id,
                    name=events.name,
                    start_date=events.start_date,
                    end_date=events.end_date,
                    category=events.category,
                    description=events.description,
                    picture=events.picture,
                    provider_name=events.provider_name
                )

            self.__event_repository.save_event(created_event)
