import time
from typing import Optional

from telegram.error import RetryAfter

from events.domain.notifier import Notifier
import telegram as _telegram

class TelegramSectionTimesNotifier(Notifier):
    def __init__(self, bot_token: str, chat_id: str):
        self.__bot = _telegram.Bot(token=bot_token)
        self.__chat_id = chat_id

    def notify(self, pilot_name: str, copilot_name: Optional[str], car: str, section_name: str, section_time: str, image_url: Optional[str]) -> None:

        competitors_string = (
            f"*{pilot_name}* y *{copilot_name}* llegan" if copilot_name else f"*{pilot_name}* llega"
        )
        short_description = f"{competitors_string} a meta con un tiempo de *{section_time}* a meta en *{section_name}*\n"

        pilot_text = f"🧍 *Piloto:*  {pilot_name}"
        copilot_text = f"🧍 *Copiloto:*  {copilot_name}"
        car_text = f"🚗 *Coche:*  {car}"
        section_name_text = f"🚥 *Tramo:*  {section_name}"
        section_time_text = f"🏁 *Tiempo:*  {section_time}"

        try:
            if copilot_name:
                text = "\n".join(
                    [
                        short_description,
                        pilot_text,
                        copilot_text,
                        car_text,
                        section_name_text,
                        section_time_text,
                    ]
                )
            else:
                text = "\n".join(
                    [
                        short_description,
                        pilot_text,
                        car_text,
                        section_name_text,
                        section_time_text,
                    ]
                )

            if image_url:
                self.__bot.send_photo(
                    chat_id=self.__chat_id,
                    photo=open(image_url, "rb"),
                    caption=text,
                    parse_mode="markdown",
                )
            else:
                self.__bot.send_message(chat_id=self.__chat_id, text=text, parse_mode="markdown")


            time.sleep(2)

        except RetryAfter as e:
            time.sleep(e.retry_after)