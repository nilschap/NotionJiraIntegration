import requests

urlSingleDataBase = "https://api.notion.com/v1/databases/8441870bfb8a4078880fd6f13e5b643c"
urlAllDataBases = "https://api.notion.com/v1/search"

token = 'secret_IMtht0eKf5iMqK7AHKB789jJBrOosub13OGzCHy8ORn'

payload = {"page_size": 100}

headers = {
"Authorization": "Bearer " + token,
    "Accept": "application/json",
    "Notion-Version": "2022-02-22"
}

def getDatabase():

 response = requests.request("GET", urlSingleDataBase, headers=headers)
 print(response.status_code)
 print(response.text)

def getDataBases():
 response = requests.request("POST", urlAllDataBases, json=payload, headers=headers)
 print(response.text)