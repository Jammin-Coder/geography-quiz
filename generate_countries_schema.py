from webbrowser import get
from iso_utils import *
import os
from utils import get_continents

regions = ['africa', 'asia', 'europe', 'north america', 'south america', 'oceania']

countries_schema = dict()


for region in regions:
    country_iso_list = list()
    region_country_isos = get_continents()
    for iso in region_country_isos:
        if os.path.isdir(iso) and iso.name in ISO_COUNTRIES_DICT.values():
            country_iso_list.append(iso.name)

    countries_schema[region] = sorted(country_iso_list)

with open('static/json/countries_schema.json', 'w') as f:
    json.dump(countries_schema, f)



