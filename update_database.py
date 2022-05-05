from dis import code_info
import requests
import base64
import json

from utils import read_json
from settings import (
    CONTINENTS, GITHUB_REPO, GITHUB_USERNAME, COUNTRIES_SCHEMA_URL
)

import mysql.connector
from database import db_connect


def verify_countries_schema(countries_schema):
    
    def example():
        example_json = """
        {
            "country": "<country_name>",
            "iso": "<iso_name>"
        }
        """
        print(f'Expected format: {example_json}')
    
    for continent in countries_schema:
        if continent not in CONTINENTS:
            print(f'{continent} is not in {CONTINENTS}!')
            exit()
        
        for country in countries_schema[continent]:
            # Missing 'country' key
            if not 'country' in country.keys():
                print(f'Key "country" was excpected to be in {continent} sub-object (country):\n{country}')
                example()
                exit()
            
            if len(country['country']) > 255:
                print(f'Country name "{country["country"]}" too long. Must be less than 255 characters long.')
                exit()
            
            if len(country['iso']) > 10:
                print(f'ISO name "{country["iso"]}" too long:')
                exit()

            # Missing 'iso' key
            if not 'iso' in country.keys():
                print(f'Key "iso" was excpected to be in {continent} sub-object (country):\n{country}')
                example()
                exit()
            
            # Makes sure there are no excess keys
            if len(country.keys()) > 2:
                print(f'Too many key/value pairs in {continent} sub-object (country): {country}.')
                example()
                exit()
    
    # If this line is reached, then the JSON is valid :)
    print('Countries schema is valid!')


# Thanks to this stackoverflow answer for providing this awesome function:
# https://stackoverflow.com/a/70136393/17273033
def github_read_file(username, repository_name, file_path, github_token=None):
    headers = {}
    if github_token:
        headers['Authorization'] = f"token {github_token}"
        
    url = f'https://api.github.com/repos/{username}/{repository_name}/contents/{file_path}'
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    data = r.json()
    file_content = data['content']
    file_content_encoding = data.get('encoding')
    if file_content_encoding == 'base64':
        file_content = base64.b64decode(file_content).decode()

    return file_content


def update_table(table):
    # remote_schema = github_read_file(GITHUB_USERNAME, GITHUB_REPO, COUNTRIES_SCHEMA_URL)
    country_schema = read_json(COUNTRIES_SCHEMA_URL)
    verify_countries_schema(country_schema)
    db = db_connect()
    cursor = db.cursor()
    
    try:
        cursor.execute(f'DELETE FROM {table}')
        for continent in country_schema:
            for country in country_schema[continent]:
                country_name = country['country']
                iso = country['iso']
                cursor.execute(
                    f'INSERT INTO {table}' + """ (continent, country, iso)
                    VALUES(%(continent)s, %(country)s, %(iso)s) ON DUPLICATE KEY UPDATE country=%(country)s;
                """,
                    {
                        'continent': continent,
                        'country': country_name,
                        'iso': iso
                    }
                )
                db.commit()
    finally:
        db.close()

def update_db():
    print('Updating database...')
    try:
        # Try updating the test table first BEFORE updating the real countries table.
        update_table('countries_test')
        update_table('countries')
    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')
        exit()

    print('Database updated.')

if __name__ == '__main__':
    update_db()
    