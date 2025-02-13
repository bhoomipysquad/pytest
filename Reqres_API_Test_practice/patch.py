import json
import requests

url="https://reqres.in/api/users/2"

response=requests.get(url)
assert response.status_code==200,f"not respond {response.status_code}"
data=response.json()
print(json.dumps(data,indent=4))

new_updated_data= {"updatedAt": "2025-01-28T09:45:17.967Z"}
response=requests.patch(url, json=new_updated_data)
assert response.status_code==200,f"not respond {response.status_code}"
new_updated_data2=response.json()
print(json.dumps(new_updated_data2,indent=4))

response=requests.get(url)
assert response.status_code==200,f"not respond {response.status_code}"
data1=response.json()
print(json.dumps(data1,indent=4))