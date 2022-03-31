import requests, json
import updateDatabase

token = 'secret_IMtht0eKf5iMqK7AHKB789jJBrOosub13OGzCHy8ORn'

databaseId = '3b50ffc44cbe40bdb6c44ef83c39cf10'

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

pageId = '9cfc54d0ebb14a93821a6b49151902db'

updateDatabase.getDatabase()
updateDatabase.getDataBases()
updateDatabase.updateDatabase()

def updatePage(padeId, headers):

    print(pageId)

    updateUrl = f"https://api.notion.com/v1/pages/{pageId}"

    updateData = {
        "properties": {
            "Value": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Pretty Good"
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(updateData)

    response = requests.request("PATCH", updateUrl, headers=headers, data=data)

    print(response.status_code)
    print(response.text)

