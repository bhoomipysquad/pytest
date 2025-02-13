import json

import requests

url="https://api.restful-api.dev/objects?id=3&id=5&id=10&id=7"
response=requests.get(url)
if response.status_code==200:
    print("url successfully opened")
data=response.json()
print(json.dumps(data,indent=4))
