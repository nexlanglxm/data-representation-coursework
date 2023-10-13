import requests
import json

url = "https://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(url)
    #got this idea from "https://stackoverflow.com/questions/54087303/python-requests-how-to-check-for-200-ok"
    if response.status_code == 200:
        print("Status code '200', all is good.")
    else:
        print("Something is not functioning as intended")
    return response.json()

def readbook(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
# we could do checking for correct response code here
    if response.status_code == 200:
        print("Status code '200', all is good.")
    return response.json()

def createbook(book):
    response = requests.post(url, json=book)
    if response.status_code == 200:
        print("Status code '200', all is good.")
    return response.json()

def updatebook(id, book):
    puturl = url + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

def deletebook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__ == "__main__":
    '''
    book= {
        'Author: teasing',
        'Title: el titulo',
        "Price": 15
    }
    bookdiff= {
        "Price":16        
    }
    '''
    #print(readbook(4))
    #print(readbooks())
    #print(createbook(book))
    #print(updatebook(5, bookdiff))
    print(deletebook())