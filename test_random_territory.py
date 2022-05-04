from utils import get_random_territory_from_region, get_iso_name
from settings import CONTINENTS
import random

if __name__ == '__main__':
    print('Getting a random territory\n')
    region_name = CONTINENTS[random.randrange(0, len(CONTINENTS))]
    territory_name = get_random_territory_from_region(region_name)
    territory_iso = get_iso_name(territory_name)
    image_file = '256.png'
    territory_image_url = f'static/maps/{region_name}/{territory_iso}/{image_file}'.replace(' ', '%20')
    print(f'Region name: {region_name}')
    print(f'Territory: {territory_name},')
    print(f'ISO: {territory_iso},')
    print(f'Image URL: {territory_image_url}\n')