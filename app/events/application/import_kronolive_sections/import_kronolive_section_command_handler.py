from cqrs.commands.command_handler import CommandHandler
from events.application.import_kronolive_sections.import_kronolive_section_command import  ImportKronoliveSectionCommand
from events.domain.event.event_repository import EventRepository
from events.domain.section.section_creator import SectionCreator
from events.domain.section.section_importer import SectionImporter
from events.domain.section.section_repository import SectionRepository



class ImportKronoliveSectionCommandHandler(CommandHandler):
    def __init__(self, section_creator: SectionCreator, section_repository: SectionRepository, section_importer: SectionImporter,
                 event_repository: EventRepository):
        self.__section_creator = section_creator
        self.__section_repository = section_repository
        self.__section_importer = section_importer
        self.__event_repository = event_repository

    def handle(self, command: ImportKronoliveSectionCommand):
        events = self.__event_repository.filter_event()
        for event in events:
            sections = self.__section_importer.section_importer(event=event)
            for section in sections:
                for code, name in section.items():
                    section = self.__section_repository.filter_section(name=name)
                    if not section:
                        created_sections = self.__section_creator.create_section(
                            name = name,
                            code = code,
                            event_id=event.id
                        )
                        self.__section_repository.save_section(created_sections)
