from cqrs.commands.command_handler import CommandHandler
from events.application.import_kronolive_inscriptions.import_kronolive_inscriptions_command import ImportKronoliveInscriptionsCommand
from events.domain.competitor.competitor_creator import CompetitorCreator
from events.domain.competitor.competitor_repository import CompetitorRepository
from events.domain.event.event_repository import EventRepository
from events.domain.inscription.inscription_creator import InscriptionCreator
from events.domain.inscription.inscription_repository import InscriptionRepository
from events.domain.inscription.inscriptions_importer import InscriptionsImporter


class ImportKronoliveInscriptionsCommandHandler(CommandHandler):
    def __init__(self, inscription_repository:InscriptionRepository, inscription_creator:InscriptionCreator, competitor_repository:CompetitorRepository, competitor_creator:CompetitorCreator, inscriptions_importer:InscriptionsImporter, event_repository:EventRepository):
        self.__inscription_repository = inscription_repository
        self.__inscription_creator = inscription_creator
        self.__competitor_repository = competitor_repository
        self.__competitor_creator = competitor_creator
        self.__inscriptions_importer = inscriptions_importer
        self.__event_repository = event_repository

    def handle(self, command: ImportKronoliveInscriptionsCommand):
        events = self.__event_repository.filter_event()
        for event in events:
            inscriptions = self.__inscriptions_importer.import_inscriptions(event=event)
            if inscriptions != None:
                for competitor in inscriptions:
                    event = self.__event_repository.filter_event(event_external_id=competitor["event_external_id"]).first()
                    self.__competitor_repository.filter_competitor(name=competitor["pilot"])
                    pilot = self.__competitor_repository.filter_competitor(name=competitor["pilot"])
                    if pilot is None:
                        created_pilot = self.__competitor_creator.create_competitor(
                            event_id=event.id,
                            name=competitor["pilot"],
                            image=None
                        )
                        self.__competitor_repository.save_competitor(created_pilot)


                    copilot = self.__competitor_repository.filter_competitor(name=competitor["copilot"])
                    if copilot is None:
                        created_copilot = self.__competitor_creator.create_competitor(
                            event_id=event.id,
                            name=competitor["copilot"],
                            image=None
                        )
                        self.__competitor_repository.save_competitor(created_copilot)

                for inscription in inscriptions:
                    event = self.__event_repository.filter_event(event_external_id=inscription["event_external_id"]).first()
                    pilot = self.__competitor_repository.filter_competitor(name=inscription["pilot"])
                    copilot = self.__competitor_repository.filter_competitor(name=inscription["copilot"])
                    created_inscriptions = self.__inscription_creator.create_inscription(
                        event_id=event.id,
                        car=inscription["car"],
                        category=inscription["category"],
                        dorsal=inscription["dorsal"],
                        pilot_id=pilot.id,
                        copilot_id=copilot.id,
                    )

                    self.__inscription_repository.save_inscription(created_inscriptions)
