from typing import List, Dict

from bs4 import BeautifulSoup
import requests

from events.domain.event.event import Event
from events.domain.inscription.inscriptions_importer import InscriptionsImporter


class KronoliveInscriptionsImporter(InscriptionsImporter):
    def import_inscriptions(self, event:Event) -> List[Dict]:
        event_external_id = event.event_external_id
        url = "https://www.kronolive.es/es/ListaDeInscritos/1231/a"
        response = requests.get(url)
        #response = requests.get(event.provider_data["inscribed_url"])
        inscriptions_list = []
        soup = BeautifulSoup(response.text)
        a = soup.find("a", id="ctl00_cphContenido_TopPrueba_hypClasificacion")
        if a and 'href' in a.attrs:
            href = a['href']
            url_sections = href.split("/")
            event_external_id = url_sections[3]

        table = soup.find("table")
        if not table:
            return

        headers = [header.text for header in table.find_all("th")]
        results = [
            {headers[i]: cell for i, cell in enumerate(row.find_all("td"))}
            for row in table.find_all("tr")
        ]

        for result in results:
            dorsal_soup = result.get("#")
            pilot_soup = result.get("Piloto")
            copilot_soup = result.get("Copiloto")
            car_soup = result.get("Vehículo")
            category_soup = result.get("Gr.")

            if not all([dorsal_soup, pilot_soup, copilot_soup, car_soup, category_soup]):
                continue

            dorsal = dorsal_soup.text.strip()
            pilots_separator = "!"
            pilots_text = pilot_soup.get_text(separator=pilots_separator, strip=True)
            if pilots_separator in pilots_text:
                pilots_names = pilots_text.split(pilots_separator)
                pilot_name = pilots_names[0]
                copilot_name = pilots_names[1]
            else:
                pilot_name = pilots_text
                copilot_name = None
            #copilot = copilot_soup.text.strip()
            car = car_soup.text.strip()
            category = category_soup.text.strip()

            inscriptions_list.append({
                "event_external_id": event_external_id,
                "dorsal": dorsal,
                "pilot": pilot_name,
                "copilot": copilot_name,
                "category": category,
                "car": car
            })
        return inscriptions_list


