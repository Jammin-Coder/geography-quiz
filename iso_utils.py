import json
import random

def read(path):
    with open(path, 'r') as f:
        return f.read()

def read_json(path):
    return json.loads(read(path))


ISO_COUNTRIES_DICT = read_json('static/json/iso_countries.json')

def get_iso_name(name):
    return ISO_COUNTRIES_DICT[name]

def get_country_name_by_iso(target_iso):
    for country_name, iso_value in ISO_COUNTRIES_DICT.items():
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


if __name__ == '__main__':
    print('Getting a random territory\n')
    region_name = 'north america'
    random_territory = get_random_territory_from_region(region_name)
    territory_iso = get_iso_name(random_territory)
    image_file = '256.png'
    territory_image_url = f'static/maps/{region_name}/{territory_iso}/{image_file}'.replace(' ', '%20')
    print(f'Territory: {random_territory},')
    print(f'ISO: {territory_iso},')
    print(f'Image URL: {territory_image_url}')


