#importing necessary libraries
from github import Github 
from config import gitconfig
import requests

apikey = gitconfig['gitkey'] 
g = Github(apikey)

repo = g.get_repo("nexlanglxm/thepublicone")