from typing import List, Dict
import requests
from bs4 import BeautifulSoup

from events.domain.event.event import Event
from events.domain.section.section_importer import SectionImporter


class KronoliveSectionImporter(SectionImporter):
    def section_importer(self, event: Event) -> List[Dict]:
        #url = "https://www.kronolive.es/es/Tiempos/1231/rallysprint-aficio-de-calvia2024"
        #response = requests.get(url)
        response = requests.get(event.provider_data["times_url"])
        soup = BeautifulSoup(response.text)
        table = soup.find("table")

        verbose_section_names = {
            header.text: header.find("a").get("title") if header.find("a") else None
            for header in table.find_all("th")
        }

        sections = [{}]

        for section in verbose_section_names:
            if verbose_section_names[section] is not None:
                sections.append({section: verbose_section_names[section]})


        return sections
