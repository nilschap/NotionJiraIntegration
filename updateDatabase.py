import requests

urlSingleDataBase = "https://api.notion.com/v1/databases/3b50ffc4-4cbe-40bd-b6c4-4ef83c39cf10"
urlAllDataBases = "https://api.notion.com/v1/search"

token = 'secret_IMtht0eKf5iMqK7AHKB789jJBrOosub13OGzCHy8ORn'

payload = {"page_size": 100}

payloadUpdateDataBase = {"properties":{"Ticket ID":{"name": "New Ticket ID"},},}

headers = {
"Authorization": "Bearer " + token,
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json"
}

def updateDatabase():
    response = requests.request("PATCH", urlSingleDataBase, json=payloadUpdateDataBase, headers=headers)
    print(response.status_code)
    print(response.text)

def getDatabase():

 response = requests.request("GET", urlSingleDataBase, headers=headers)
 print(response.status_code)
 print(response.text)

def getDataBases():
 response = requests.request("POST", urlAllDataBases, json=payload, headers=headers)
 print(response.status_code)
 print(response.text)