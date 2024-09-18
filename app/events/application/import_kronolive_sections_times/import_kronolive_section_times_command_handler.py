from datetime import datetime
from uuid import UUID

from cqrs.commands.command_handler import CommandHandler
from events.application.import_kronolive_sections.import_kronolive_section_command import  ImportKronoliveSectionCommand
from events.domain.event.event_repository import EventRepository
from events.domain.inscription.inscription_repository import InscriptionRepository

from events.domain.section.section_repository import SectionRepository
from events.domain.section_time.section_time_creator import SectionTimeCreator
from events.domain.section_time.section_time_importer import SectionTimeImporter
from events.domain.section_time.section_time_repository import SectionTimeRepository


class ImportKronoliveSectionTimesCommandHandler(CommandHandler):
    def __init__(self, section_times_creator: SectionTimeCreator,section_time_repository: SectionTimeRepository, section_repository: SectionRepository, section_time_importer: SectionTimeImporter,
                 event_repository: EventRepository, inscription_repository:InscriptionRepository):
        self.__section_times_creator = section_times_creator
        self.__section_repository = section_repository
        self.__section_times_repository = section_time_repository
        self.__section_times_importer = section_time_importer
        self.__event_repository = event_repository
        self.__inscription_repository = inscription_repository

    def handle(self, command: ImportKronoliveSectionCommand):
        sections = self.__section_repository.filter_section()
        for section in sections:
            section_time = self.__section_times_importer.section_time_importer(section=section)
            for section in section_time:
                #inscriptions = self.__inscription_repository.filter_inscriptions(inscription=inscription)
                #for inscription in inscriptions:
                for total in section.items():
                    #time_str = total[1].split(' ')[0]
                    #section_time = datetime.strptime(time_str, "%M:%S.%f")

                    created_sections_times = self.__section_times_creator.section_time_creator(
                        section_id=section.id,
                        inscription=UUID("ffab5d62-506d-4f94-a9ad-f4139b3461ee"),
                        section_time= section_time
                    )
                    self.__section_repository.save_section(created_sections_times)
