from typing import List, Dict
import re
import requests
from bs4 import BeautifulSoup

from events.domain.event.event import Event
from events.domain.section_time.section_time_importer import SectionTimeImporter


class KronoliveSectionTimeImporter(SectionTimeImporter):
    def section_time_importer(self, event: Event) -> List[Dict]:
        url = "https://www.kronolive.es/es/Tiempos/1231/a"
        response = requests.get(url)
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

# [{'dorsal': '1', 'code': {'tc1': '05:46.8', 'tc2': '05:37.7', 'tc3': '05:32.4', 'tc4': '05:38.9', 'tc5': '05:31.5', 'tc6': '05:30.3'}},
#  {'dorsal': '2', 'code': {'tc1': '05:45.6', 'tc2': '05:41.3', 'tc3': '05:40.9', 'tc4': '05:43.5', 'tc5': '05:36.1', 'tc6': '05:33.2'}},
#  {'dorsal': '3', 'code': {'tc1': '06:01.7', 'tc2': '05:53.7', 'tc3': '05:45.2', 'tc4': '05:43.8', 'tc5': '05:38.6', 'tc6': '05:30.5'}},
#  {'dorsal': '4', 'code': {'tc1': '06:23.1', 'tc2': '06:14.9', 'tc3': '06:06.0', 'tc4': '06:03.1', 'tc5': '06:01.4', 'tc6': '05:56.9'}},
#  {'dorsal': '5', 'code': {'tc1': '05:56.9', 'tc2': '05:50.3', 'tc3': '05:45.9', 'tc4': '05:50.2', 'tc5': '05:44.1', 'tc6': '05:40.5'}},
#  {'dorsal': '6', 'code': {'tc1': '06:07.6', 'tc2': '05:55.3', 'tc3': '05:52.8', 'tc4': '05:56.7', 'tc5': '06:01.6', 'tc6': '05:55.5'}},
#  {'dorsal': '8', 'code': {'tc1': '06:26.3', 'tc2': '06:11.3', 'tc3': '06:02.0', 'tc4': '06:09.6', 'tc5': '05:59.4', 'tc6': '05:52.5'}},
#  {'dorsal': '9', 'code': {'tc1': '06:38.9', 'tc2': '06:24.0', 'tc3': '06:17.6', 'tc4': '06:20.4', 'tc5': '06:13.3', 'tc6': '06:13.7'}},
#  {'dorsal': '10', 'code': {'tc1': '06:11.0', 'tc2': '06:00.5', 'tc3': '05:58.4', 'tc4': '06:02.1', 'tc5': '06:08.6', 'tc6': '05:59.9'}},
#  {'dorsal': '11', 'code': {'tc1': '06:22.6', 'tc2': '06:08.9', 'tc3': '06:07.2', 'tc4': '06:05.7', 'tc5': '06:01.3', 'tc6': '05:55.9'}},
#  {'dorsal': '14', 'code': {'tc1': '06:57.6', 'tc2': '06:53.7', 'tc3': '06:49.7', 'tc4': '06:44.5', 'tc5': '06:44.9', 'tc6': '06:45.4'}},
#  {'dorsal': '16', 'code': {'tc1': '06:19.2', 'tc2': '06:11.0', 'tc3': '06:07.2', 'tc4': '06:16.7', 'tc5': '06:11.4', 'tc6': '06:13.1'}},
#  {'dorsal': '18', 'code': {'tc1': '06:31.4', 'tc2': '06:19.2', 'tc3': '06:15.2', 'tc4': '06:24.8', 'tc5': '06:17.7', 'tc6': '06:15.6'}},
#  {'dorsal': '20', 'code': {'tc1': '06:18.8', 'tc2': '06:08.2', 'tc3': '06:06.2', 'tc4': '06:07.3', 'tc5': '06:01.9', 'tc6': '06:00.4'}},
#  {'dorsal': '21', 'code': {'tc1': '06:25.6', 'tc2': '06:24.0', 'tc3': '06:21.6', 'tc4': '06:20.9', 'tc5': '06:11.8', 'tc6': '06:12.7'}},
#  {'dorsal': '22', 'code': {'tc1': '06:17.6', 'tc2': '06:21.3', 'tc3': '06:16.9', 'tc4': '06:17.5', 'tc5': '06:13.7', 'tc6': '06:09.5'}},
#  {'dorsal': '23', 'code': {'tc1': '06:51.1', 'tc2': '06:33.0', 'tc3': '06:33.8', 'tc4': '06:41.8', 'tc5': '06:27.1', 'tc6': '06:23.3'}},
#  {'dorsal': '24', 'code': {'tc1': '06:52.2', 'tc2': '06:29.6', 'tc3': '06:25.4', 'tc4': '06:37.9', 'tc5': '06:22.8', 'tc6': '06:19.8'}},
#  {'dorsal': '26', 'code': {'tc1': '06:28.7', 'tc2': '06:18.4', 'tc3': '06:08.4', 'tc4': '06:16.0', 'tc5': '06:10.2', 'tc6': '07:34.9'}}]

































# class KronoliveSectionTimeImporter(SectionTimeImporter):
#     def section_time_importer(self, event: Event) -> List[Dict]:
#         url = f"https://www.kronolive.es/es/Tiempos/1230/a"
#         response = requests.get(url)
#         #response = requests.get(event.provider_data["times_url"])
#         soup = BeautifulSoup(response.text)
#
#         table = soup.find("table")
#         if not table:
#             return
#
#         headers = [header.text for header in table.find_all("th")]
#         results = [
#             {headers[i]: cell for i, cell in enumerate(row.find_all("td"))}
#             for row in table.find_all("tr")
#         ]
#         total_list = []
#         for result in results:
#             total_soup = result.get("Total")
#
#             if not all([total_soup]):
#                 continue
#
#             total = total_soup.text.strip()
#             # Usa una expresión regular para extraer la parte que necesitas
#             match = re.match(r"^(\d{2}:\d{2}\.\d{1,2})", total)
#             if match:
#                 total = match.group(1)
#                 total_list.append({
#                         "total": total,
#
#                     })
#         return total_list
