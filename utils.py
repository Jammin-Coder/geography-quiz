import json
import random
import os

def get_continents(path='static/maps'):
    continents = []
    dir_contents = os.scandir(path)
    for item in dir_contents:
        if os.path.isdir(item):
            continents.append(item.name)
    return continents


def read(path):
    with open(path, 'r') as f:
        return f.read()

def read_json(path):
    return json.loads(read(path))


def get_iso_countries_dict():
    return read_json('static/json/iso_countries.json')

def get_iso_name(name):
    return get_iso_countries_dict()[name]

def get_country_name_by_iso(target_iso):
    for country_name, iso_value in get_iso_countries_dict().items():
        if iso_value == target_iso:
            return country_name

def check_for_none():
    regions = ['africa', 'asia', 'europe', 'namerica', 'samerica', 'oceania']
    for region in regions:
        territory_isos = read_json('countries_schema.json')[region]
        for iso in territory_isos:
            country = get_country_name_by_iso(iso)
            if country == None:
                print(f'Region: {region}, Country: {country}, ISO: {iso}')

def get_random_territory_from_region(region):
    territories = read_json('static/json/countries_schema.json')[region]
    territory_iso = territories[random.randrange(0, len(territories))]

    territory = get_country_name_by_iso(territory_iso)
    return territory



