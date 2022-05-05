from webbrowser import get
from utils import *
import os
from utils import get_continents, get_country_name_by_iso

regions = ['africa', 'asia', 'europe', 'north america', 'south america', 'oceania']

countries_schema = dict()


for region in regions:
    country_iso_list = list()
    continents = os.scandir(f'{MAPS_DIR}/{region}')
    for iso_dir in continents:
        if os.path.isdir(iso_dir) and iso_dir.name in get_iso_countries_dict().values():
            country_name = get_country_name_by_iso(iso_dir.name)
            country_iso_list.append({'country': country_name, 'iso': iso_dir.name})

    countries_schema[region] = country_iso_list

with open('static/json/countries_schema.json', 'w') as f:
    json.dump(countries_schema, f, indent=4)



