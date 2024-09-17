from typing import List, Dict

import requests

from events.domain.event.event_category_choices import EventCategoryChoices
from events.domain.event.event_importer import EventImporter

from bs4 import BeautifulSoup


class KronoliveEventImporter(EventImporter):
    def import_events(self) -> List[Dict]:
        url = "https://www.kronolive.es/es/2024"
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        cards = soup.find_all("div", class_="col-12 col-sm-6 col-md-4 col-lg-3")
        event_list = []
        for card in cards:
            url = card.find('a')['href']
            event_url = f"https://www.kronolive.es{url}"
            name = card.find('br').previous_sibling.strip()
            start_date = card.find('small').text.strip()
            url_sections = url.split("/")
            event_external_id = url_sections[3]

            name = name.lower()
            if "pujada" in name or "subida" in name:
                category =  EventCategoryChoices.HILL_CLIMB.value
            elif "autocross" in name:
                category = EventCategoryChoices.AUTO_CROSS.value
            elif "karting" in name:
                category = EventCategoryChoices.KARTING.value
            else:
                category = EventCategoryChoices.RALLY.value


            event_list.append(
                {
                    "url": event_url,
                    "name": name,
                    "start_date": start_date,
                    "event_external_id": event_external_id,
                    "category": category
                })
        return event_list
