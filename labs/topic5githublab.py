import requests
import urllib.parse
import json
from config import gitconfig

filename = "private-repo.json"
gitkey = gitconfig["gitkey"]

url = 'https://api.github.com/nexlanglxm/theprivateone'

response = requests.get(url, auth=('token',gitkey))

repoJSON = response.json()

with open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)