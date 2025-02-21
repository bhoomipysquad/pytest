import json

import requests

url="https://api.restful-api.dev/objects/2"
response=requests.get(url)
if response.status_code==200:
    print("yes, url opened successfully")
else:
    print("something went wrong")

data=response.json()
print(json.dumps(data,indent=4))
