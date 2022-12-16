# -*- coding: utf-8 -*-
"""
* Assignment: About EntryTest Endswith
* Complexity: medium
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Define `result: list[str]`
    2. Collect in `result` all email addresses from `DATA` -> `crew`
       with domain names mentioned in `DOMAINS`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[str]`
    2. Zbierz w `result` wszystkie adresy email z `DATA` -> `crew`
       z nazwami domenowymi wymienionymi w `DOMAINS`
    3. Uruchom doctesty - wszystkie muszą się powieść


    ['mlewis@nasa.gov', 'rmartinez@nasa.gov', 'cbeck@nasa.gov',
     'bjohanssen@nasa.gov', 'mwatney@nasa.gov', 'ptwardowski@polsa.gov.pl']
"""

DATA = {
    'mission': 'Ares 3',
    'launch': '2035-06-29',
    'landing': '2035-11-07',
    'destination': 'Mars',
    'location': 'Acidalia Planitia',
    'crew': [{'name': 'Melissa Lewis', 'email': 'mlewis@nasa.gov'},
             {'name': 'Rick Martinez', 'email': 'rmartinez@nasa.gov'},
             {'name': 'Alex Vogel', 'email': 'avogel@esa.int'},
             {'name': 'Chris Beck', 'email': 'cbeck@nasa.gov'},
             {'name': 'Beth Johanssen', 'email': 'bjohanssen@nasa.gov'},
             {'name': 'Mark Watney', 'email': 'mwatney@nasa.gov'},
             {'name': 'Pan Twardowski', 'email': 'ptwardowski@polsa.gov.pl'},
             {'name': 'Ivan Ivanovich', 'email': 'iivanovich@roscosmos.ru'}]}

# DATA = [{'email': 'mlewis@nasa.gov'},
#         {'email': 'rmartinez@nasa.gov'},
#         {'email': 'avogel@esa.int'},
#         {'email': 'cbeck@nasa.gov'},
#         {'email': 'bjohanssen@nasa.gov'},
#         {'email': 'mwatney@nasa.gov'},
#         {'email': 'ptwardowski@polsa.gov.pl'},
#         {'email': 'iivanovich@roscosmos.ru'}]


DOMAINS = ('.gov', '.gov.pl')
# [row['email'] for row in DATA['crew'] if row['email'].endswith(DOMAINS)]
results = []
for row in DATA['crew']:
    if row['email'].endswith(DOMAINS):
        results.append(row['email'])

results = [row['email'] for row in DATA['crew'] if row['email'].endswith(DOMAINS)]


print()
# str.endswith(DOMAINS)


# Email addresses with top-level domain in DOMAINS
# type: list[str]