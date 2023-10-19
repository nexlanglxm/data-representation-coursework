import requests
import urllib.parse
from config import config

targetUrl = "https://en.wikipedia.org"

apiKey = config["htmltopdfkey"]

apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetUrl, 'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl + "?" + parsedparams

response = requests.get(requestUrl)
print (response.status_code)

result = response.content
with open("document.pdf", "wb") as handler:
    handler.write(result)