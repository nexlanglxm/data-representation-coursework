import requests
import json

url = "https://andrewbeatty1.pythonanywhere.com/books"

def readBooks():
    response = requests.get(url)
    #got this idea from "https://stackoverflow.com/questions/54087303/python-requests-how-to-check-for-200-ok"
    if response.status_code == 200:
        print("Status code '200', all is good.")
    else:
        print("Something is not functioning as intended")
    return response.json()

if __name__ == "__main__":
    print(readBooks())

