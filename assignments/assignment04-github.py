#importing necessary libraries
from github import Github 
from config import gitconfig
import requests
#using the acccess token
apikey = gitconfig['gitkey'] 
g = Github(apikey)

repo = g.get_repo("nexlanglxm/thepublicone")
fileInfo = repo.get_contents("assignment.txt")
urlofFile = fileInfo.download_url
#print(urlofFile) #making sure that it is loading/working so far

#using the requests to scrape the contents of the file
response = requests.get(urlofFile, auth=(apikey,''))
contentsofFile = response.text
'''
testing
print(contentsofFile) 
'''
#replacing instances
newContent = contentsofFile.replace('Andrew', 'Neil')

gitHubresponse = repo.update_file(fileInfo.path,"updated by prog",newContent,fileInfo.sha)
#print(gitHubresponse)

