from django.core.management import BaseCommand

from config import settings
from events.application.import_kronolive_sections.import_kronolive_section_command import  ImportKronoliveSectionCommand
from events.application.import_kronolive_sections_times.import_kronolive_section_times_command_handler import ImportKronoliveSectionTimesCommandHandler
from events.domain.section_time.section_time_creator import SectionTimeCreator
from events.infraestructure.db_event_repository import DbEventRepository
from events.infraestructure.db_inscription_repository import DbInscriptionRepository
from events.infraestructure.db_section_repository import DbSectionRepository
from events.infraestructure.db_section_time_repository import DbSectionTimeRepository
from events.infraestructure.kronolive_section_importer import KronoliveSectionImporter
from events.infraestructure.kronolive_section_time_importer import KronoliveSectionTimeImporter
from events.infraestructure.telegram_section_times_notifier import TelegramSectionTimesNotifier
from events.infraestructure.whatsapp_section_times_notifier import WhatsappSectionTimesNotifier


class Command(BaseCommand):
    help = 'Import kronolive section'

    def __init__(self):
        super().__init__()
        self.__section_times_creator = SectionTimeCreator()
        self.__db_section_repository = DbSectionRepository()
        self.__db_section_time_repository = DbSectionTimeRepository()
        self.__kronolive_section_time_importer = KronoliveSectionTimeImporter()
        self.__db_event_repository = DbEventRepository()
        self.__db_inscription_repository = DbInscriptionRepository()
        self.__kronolive_section_importer = KronoliveSectionImporter()
        self.__telegram_section_times_notifier = TelegramSectionTimesNotifier(bot_token=settings.TELEGRAM_BOT_TOKEN, chat_id=settings.TELEGRAM_CHAT_ID)
        self.__whatsapp_section_times_notifier = WhatsappSectionTimesNotifier(whatsapp_url=settings.API_WHATSAPP_URL, whatsapp_token=settings.WHATSAPP_BEARER_TOKEN, origen_whatsapp_number=settings.ORIGEN_WHATSAPP_NUMBER)

        self.__import_kronolive_section_time_command_handler = ImportKronoliveSectionTimesCommandHandler(
            section_times_creator=self.__section_times_creator,
            section_repository=self.__db_section_repository,
            section_time_repository=self.__db_section_time_repository,
            section_time_importer=self.__kronolive_section_time_importer,
            event_repository=self.__db_event_repository,
            inscription_repository=self.__db_inscription_repository,
            section_importer=self.__kronolive_section_importer,
            notifiers=[self.__telegram_section_times_notifier, self.__whatsapp_section_times_notifier]
        )

    def handle(self, *args, **options):
        command = ImportKronoliveSectionCommand()
        self.__import_kronolive_section_time_command_handler.handle(command)
