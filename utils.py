import json
import random
import os
from settings import MAPS_DIR, COUNTRIES_SCHEMA_URL

def get_continents(path=MAPS_DIR):
    continents = []
    dir_contents = os.scandir(path)
    for item in dir_contents:
        if os.path.isdir(item):
            continents.append(item.name)
    return continents


def read(path):
    with open(path, 'r') as f:
        return f.read()


def write(path, contents):
    with open(path, 'w') as f:
        f.write(contents)


def write_json(path, contents):
    with open(path, 'w') as f:
        json.dump(contents, f, indent=4)


def read_json(path):
    return json.loads(read(path))


def get_iso_countries_dict():
    pass


def get_iso_name(name):
    pass


def get_country_name_by_iso(target_iso):
    pass


def get_random_territory_from_region(region):
    pass



