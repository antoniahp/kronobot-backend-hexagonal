from datetime import datetime
from uuid import UUID

from cqrs.commands.command_handler import CommandHandler
from events.application.import_kronolive_sections.import_kronolive_section_command import  ImportKronoliveSectionCommand
from events.domain.event.event_repository import EventRepository
from events.domain.inscription.inscription_repository import InscriptionRepository
from events.domain.section.section_importer import SectionImporter

from events.domain.section.section_repository import SectionRepository
from events.domain.section_time.section_time_creator import SectionTimeCreator
from events.domain.section_time.section_time_importer import SectionTimeImporter
from events.domain.section_time.section_time_repository import SectionTimeRepository


class ImportKronoliveSectionTimesCommandHandler(CommandHandler):
    def __init__(self, section_times_creator: SectionTimeCreator,section_time_repository: SectionTimeRepository, section_repository: SectionRepository, section_time_importer: SectionTimeImporter,
                 event_repository: EventRepository, inscription_repository:InscriptionRepository, section_importer: SectionImporter):
        self.__section_times_creator = section_times_creator
        self.__section_repository = section_repository
        self.__section_time_repository = section_time_repository
        self.__section_times_importer = section_time_importer
        self.__event_repository = event_repository
        self.__inscription_repository = inscription_repository
        self.__section_importer = section_importer

    def handle(self, command: ImportKronoliveSectionCommand):
        events = self.__event_repository.filter_event()
        for event in events:
            sections = self.__section_repository.filter_section()
            for section in sections:
                inscriptions = self.__inscription_repository.filter_inscriptions(event_id=event.id)
                for inscription in inscriptions:
                    section_times = self.__section_times_importer.section_time_importer(section=section)
                    for time in section_times:
                        created_sections_times = self.__section_times_creator.section_time_creator(
                            section_id=section.id,
                            inscription=inscription.id,
                            section_time=time["total"]
                        )
                        self.__section_time_repository.save_section_time(created_sections_times)
