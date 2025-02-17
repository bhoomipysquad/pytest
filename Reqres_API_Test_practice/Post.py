import json

import requests

url = "https://reqres.in/api/users"
header = { 'Content-Type': 'application/json',
          }
# pay_load = {
#     "name": "morpheus",
#     "job": "leader"
# }


 # import from another file
json_file = open ('./users.json')
json_payload = json.load(json_file)

response = requests.post(url , headers=header , json= json_payload)
print(response.json())
assert response.status_code == 201