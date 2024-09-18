from cqrs.commands.command_handler import CommandHandler
from events.application.import_kronolive_sections.import_kronolive_section_time_command import ImportKronoliveSectionTimeCommand
from events.domain.event.event_repository import EventRepository
from events.domain.section.section_creator import SectionCreator
from events.domain.section_time.section_time_importer import  SectionTimeImporter
from events.domain.section.section_repository import SectionRepository
from events.domain.section_time.section_time_creator import SectionTimeCreator
from events.domain.section_time.section_time_repository import SectionTimeRepository


class ImportKronoliveSectionTimeCommandHandler(CommandHandler):
    def __init__(self, section_creator: SectionCreator, section_repository: SectionRepository, section_time_importer: SectionTimeImporter,
                 event_repository: EventRepository,section_time_creator: SectionTimeCreator,section_time_repository:SectionTimeRepository):
        self.__section_creator = section_creator
        self.__section_repository = section_repository
        self.__section_time_creator = section_time_creator
        self.__section_time_repository = section_time_repository
        self.__section_time_importer = section_time_importer
        self.__event_repository = event_repository

    def handle(self, command: ImportKronoliveSectionTimeCommand):
        events = self.__event_repository.filter_event()
        for event in events:
            sections = self.__section_time_importer.section_time_importer(event=event)
            for section in sections:
                for code, name in section.items():
                    created_sections = self.__section_creator.create_section(
                        name = name,
                        code = code,
                        event_id=event.id
                    )
                    self.__section_repository.save_section(created_sections)
