import requests
import json

url = "https://reqres.in/api/users/2"
data={
    "name": "morpheus",
    "job": "leader",
    "id": "389",
    "createdAt": "2025-01-27T10:09:34.686Z"
}
response = requests.post(url,data=data)
assert response.status_code == 201 ,f"not response code {response.status_code}"
data=response.json()
print(json.dumps(data, indent=4))

updated_data ={
    "name" : "Bhumi",
    #  "job": "leader",
    #  "id": "389",
    # "createdAt": "2025-01-27T11:20:56.603Z"
}

response=requests.patch(url, data=updated_data)
assert response.status_code == 200 ,f"not response code {response.status_code}"
updated_data = response.json()
print(json.dumps(updated_data, indent=4))



