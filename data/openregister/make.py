import os

import requests
import requests_cache

requests_cache.install_cache('demo_cache')

page = 1
base_url = "https://api.github.com/{}/openregister/"
json_data = True
while json_data:
    url = '{}repos?page={}'.format(base_url.format('orgs'), page)
    req = requests.get(url)
    json_data = req.json()
    for repo in json_data:
        name = repo['name']
        if not name.endswith('-data'):
            continue
        # print(name)
        base_path = os.path.join(os.path.dirname(__file__), name)
        maps_url = "{}{}/contents/maps".format(base_url.format('repos'), name)
        # print(maps_url)
        for file_data in requests.get(maps_url).json():
            if file_data in ["documentation_url", "message"]:
                continue
            print(file_data)
            os.makedirs(base_path, exist_ok=True)
            file_path = os.path.join(
                base_path, file_data['path'].split('/')[-1])
            if file_path == "locality.tsv":
                continue
            if 'download_url' in file_data and file_data['download_url']:
                with open(file_path, 'w') as f:
                    f.write(requests.get(file_data['download_url']).text)

    page = page + 1
