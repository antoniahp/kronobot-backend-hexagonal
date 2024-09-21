import time
from typing import Optional

import telegram.error

from events.domain.notifier import Notifier
import telegram as _telegram

class TelegramSectionTimesNotifier(Notifier):
    def __init__(self, bot_token: str, chat_id: str):
        self.__bot = _telegram.Bot(token=bot_token)
        self.__chat_id = chat_id

    def notify(self, pilot_name: str, copilot_name: Optional[str], car: str, section_name: str, section_time: str, image_url: Optional[str]) -> None:

        # Formateo de texto
        caption = (f"*{pilot_name}* y *{copilot_name}* llegan {car}{section_name}{section_time}"
                   if copilot_name else f"*{pilot_name}* llega {car}")

        pilot_text = f"🧍 *Piloto:*  {pilot_name}"
        copilot_text = f"🧍 *Copiloto:*  {copilot_name}" if copilot_name else ""
        car_text = f"🚗 *Coche:*  {car}"
        section_name_text = f"🚥 *Tramo:*  {section_name}"
        section_time_text = f"🏁 *Tiempo:*  {section_time}"

        message_text = f"{pilot_text}\n{copilot_text}\n{car_text}\n{section_name_text}\n{section_time_text}"
        try:
            self.__bot.send_message(
                chat_id=self.__chat_id,
                text=message_text,
                parse_mode="markdown",
            )
        except telegram.error.TimedOut:
            time.sleep(1)