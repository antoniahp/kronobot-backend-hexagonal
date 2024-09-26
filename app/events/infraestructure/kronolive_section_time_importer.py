from typing import List, Dict
import re
import requests
from bs4 import BeautifulSoup

from events.domain.event.event import Event
from events.domain.section_time.section_time_importer import SectionTimeImporter


class KronoliveSectionTimeImporter(SectionTimeImporter):
    def section_time_importer(self, event: Event) -> List[Dict]:
        #url = "https://www.kronolive.es/es/Tiempos/1226/rallysprint-sant-salvador2024"
        #response = requests.get(url)
        response = requests.get(event.provider_data["times_url"])
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find("table")
        if not table:
            return []

        headers = [header.text.strip() for header in table.find_all('th')]
        time_headers = [header for header in headers if re.match(r'^(TC\d+|carrera\d+|Entrenos\d+|WarmUp\d+|Cronos|Carrera \d+|Carrera\d+)$', header, re.IGNORECASE)]

        rows = table.find_all('tr')

        results = []
        for row in rows:
            cells = row.find_all('td')
            if cells:
                result = {headers[i]: cell.text.strip() for i, cell in enumerate(cells)}
                results.append(result)

        # Procesar los tiempos
        total_list = []
        valid_time_pattern = r"^\d{2}:\d{2}\.\d{1,3}$"  # Ajustado para tiempos con milisegundos

        for result in results:
            dorsal = result.get("#")
            if not dorsal:
                continue

            time_data = {}
            for header in time_headers:
                time_value = result.get(header)
                if time_value:
                    time_value = re.sub(r"\s*\(.*?\)", "", time_value.strip())
                    if re.match(valid_time_pattern, time_value):
                        time_data[header] = time_value

            if time_data:
                total_list.append({
                    "dorsal": dorsal.strip(),
                    "code": time_data
                })

        return total_list
