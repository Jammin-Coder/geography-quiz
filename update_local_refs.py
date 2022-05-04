import requests
import base64
import json

from utils import write, write_json
from settings import (
    GITHUB_REPO, GITHUB_USERNAME,
    ISO_COUNTRIES_URL, COUNTRIES_SCHEMA_URL
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


def update_local_refs():
    iso_countries = json.loads(github_read_file(GITHUB_USERNAME, GITHUB_REPO, ISO_COUNTRIES_URL))
    countries_schema = json.loads(github_read_file(GITHUB_USERNAME, GITHUB_REPO, COUNTRIES_SCHEMA_URL))
    write_json(ISO_COUNTRIES_URL, iso_countries)
    write_json(COUNTRIES_SCHEMA_URL, countries_schema)

if __name__ == '__main__':
    print('Updating local JSON reference files...')
    update_local_refs()
    print('Local JSON reference files are updated')