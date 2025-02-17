import json
import requests

url="https://api.restful-api.dev/objects"

response=requests.get(url)
print(response.status_code)
if response.status_code==200:
    print("url successfully opened")

data=response.json()
print(json.dumps(data,indent=4))