from typing import List, Dict
import requests
from bs4 import BeautifulSoup
from pip._vendor.rich import table

from events.domain.event.event import Event
from events.domain.section.section import Section
from events.domain.section_time.section_time_importer import SectionTimeImporter


class KronoliveSectionTimeImporter(SectionTimeImporter):
    def section_time_importer(self, section: Section) -> List[Dict]:
        url = "https://www.kronolive.es/es/Tiempos/1230/rallysprint-ses-salines2024"
        response = requests.get(url)
        #response = requests.get(event.provider_data["times_url"])
        soup = BeautifulSoup(response.text)
        table = soup.find("table")

        table = soup.find("table")
        if not table:
            return

        headers = [header.text for header in table.find_all("th")]
        results = [
            {headers[i]: cell for i, cell in enumerate(row.find_all("td"))}
            for row in table.find_all("tr")
        ]
        total_list = []
        for result in results:
            total_soup = result.get("Total")

            if not all([total_soup]):
                continue

            total = total_soup.text.strip()

            total_list.append({
                "total": total,

            })
        return total_list
