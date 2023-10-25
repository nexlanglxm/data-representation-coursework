from github import Github
from config import gitconfig
import requests

apikey = gitconfig['gitkey']
g = Github(apikey)
# print(g)

# for repo in g.get_user().get_repos():
#     print(repo.name)
repo = g.get_repo("nexlanglxm/thepublicone")
# print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlofFile = fileInfo.download_url
# print (urlofFile)

response = requests.get(urlofFile)
contentofFile = response.text
# print (contentofFile)

newContents = contentofFile + "\n more shtuff, \n and more"
# print(newContents)

gitHubresponse = repo.update_file(fileInfo.path,"updated via prog",newContents,fileInfo.sha)
print (gitHubresponse)