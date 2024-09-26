from typing import Optional
import requests
from events.domain.notifier import Notifier

class WhatsappSectionTimesNotifier(Notifier):
    def __init__(self, whatsapp_url: str, whatsapp_token: str, origen_whatsapp_number: str):
        self.__whatsapp_url = whatsapp_url
        self.__whatsapp_token = whatsapp_token
        self.__origen_whatsapp_number = origen_whatsapp_number

    def notify(self, pilot_name: str, copilot_name: Optional[str], car: str, section_name: str, section_time: str, image_url: Optional[str]) -> None:

        competitors_string = (
            f"*{pilot_name}* y *{copilot_name}* llegan" if copilot_name else f"*{pilot_name}* llega"
        )
        short_description = f"{competitors_string} a meta con un tiempo de *{section_time}* en *{section_name}*\n"

        pilot_text = f"🧍 *Piloto:*  {pilot_name}"
        copilot_text = f"🧍 *Copiloto:*  {copilot_name}" if copilot_name else ""
        car_text = f"🚗 *Coche:*  {car}"
        section_name_text = f"🚥 *Tramo:*  {section_name}"
        section_time_text = f"🏁 *Tiempo:*  {section_time}"

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

        url = self.__whatsapp_url


        # if image_url:
        #     with open(image_url, "rb") as image_file:
        #         data = base64.b64encode(image_file.read())
        #     payload = {
        #         "to": self.__origen_whatsapp_number,
        #         "body": text,
        #         "media": data.decode("utf-8")
        #     }
        # else:
        payload = {
            "to": self.__origen_whatsapp_number,
            "caption": text,
            "media": "https://cdn.pixabay.com/photo/2018/10/02/18/57/car-3719640_1280.jpg"
        }

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": self.__whatsapp_token
        }

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
