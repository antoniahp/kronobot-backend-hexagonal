from cqrs.commands.command_handler import CommandHandler
from events.application.import_kronolive_sections.import_kronolive_section_command import  ImportKronoliveSectionCommand
from events.domain.event.event_repository import EventRepository
from events.domain.inscription.inscription_repository import InscriptionRepository
from events.domain.notifier import Notifier
from events.domain.section.section_importer import SectionImporter

from events.domain.section.section_repository import SectionRepository
from events.domain.section_time.section_time_creator import SectionTimeCreator
from events.domain.section_time.section_time_importer import SectionTimeImporter
from events.domain.section_time.section_time_repository import SectionTimeRepository
from events.domain.competitor import competitor


class ImportKronoliveSectionTimesCommandHandler(CommandHandler):
    def __init__(self, section_times_creator: SectionTimeCreator,section_time_repository: SectionTimeRepository, section_repository: SectionRepository, section_time_importer: SectionTimeImporter,
                 event_repository: EventRepository, inscription_repository:InscriptionRepository, section_importer: SectionImporter, notifier:Notifier):
        self.__section_times_creator = section_times_creator
        self.__section_repository = section_repository
        self.__section_time_repository = section_time_repository
        self.__section_times_importer = section_time_importer
        self.__event_repository = event_repository
        self.__inscription_repository = inscription_repository
        self.__section_importer = section_importer
        self.__notifier = notifier

    def handle(self, command: ImportKronoliveSectionCommand):
        events = self.__event_repository.filter_event()
        for event in events:
            sections = self.__section_repository.filter_section()
            inscriptions = self.__inscription_repository.filter_inscriptions(event_id=event.id)
            if len(inscriptions) == 0:
                continue

            dorsal_inscription_mapper = {}
            for inscription in inscriptions:
                dorsal_inscription_mapper[inscription.dorsal] = inscription


            section_code_section_mapper = {}
            for section in sections:
                section_code_section_mapper[section.code] = section

            section_times = self.__section_times_importer.section_time_importer(event=event)
            for section_time in section_times:
                dorsal = section_time["dorsal"]
                inscription = dorsal_inscription_mapper[dorsal]
                for section_code, time in section_time["code"].items():
                    section = section_code_section_mapper[section_code]
                    created_sections_times = self.__section_times_creator.section_time_creator(
                        section_id=section.id,
                        inscription=inscription.id,
                        section_time=time
                    )
                    self.__section_time_repository.save_section_time(created_sections_times)
                    self.__notifier.notify(section_name=section.name,
                                           section_time=time,
                                           pilot_name=inscription.pilot.name,
                                           copilot_name=inscription.copilot.name if inscription.copilot else None,
                                           car=inscription.car,
                                           image_url=inscription.pilot.image.url if inscription.pilot.image else None)