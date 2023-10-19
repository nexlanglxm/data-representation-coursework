import requests
import urllib.parse
import json
from config import gitconfig

gitkey = gitconfig["gitkey"]

url = 'https://github.com/nexlanglxm/theprivateone'

response = requests.get(url, auth=('token',gitkey))

repoJSON = response.json()

with open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)