import requests
import base64
import json

import mysql.connector
from utils import read_json
from settings import (
    GITHUB_REPO, GITHUB_USERNAME,
    COUNTRIES_SCHEMA_URL,
    DB_HOST, DB_NAME, DB_PASSWORD, DB_USERNAME
)

db = mysql.connector.connect(
    user=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME
)

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


def update_country_schema():
    # remote_schema = github_read_file(GITHUB_USERNAME, GITHUB_REPO, COUNTRIES_SCHEMA_URL)
    country_schema = read_json(COUNTRIES_SCHEMA_URL)
    cursor = db.cursor()
    try:
        for continent in country_schema:
            for country in country_schema[continent]:
                country_name = country['country']
                iso = country['iso']
                cursor.execute("""
                    INSERT INTO countries (continent, country, iso)
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



if __name__ == '__main__':
    print('Updating database...')
    update_country_schema()
    print('Database updated.')