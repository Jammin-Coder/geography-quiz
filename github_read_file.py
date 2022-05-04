import requests
import base64

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

print(github_read_file('Jammin-Coder', 'geography-quiz', 'static/json/iso_countries.json'))