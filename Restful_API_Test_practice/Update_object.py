import json
import requests

def test_update_object():
    url="https://api.restful-api.dev/objects/7"
    data={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}
    response=requests.put(url,json=data)
    if response.status_code==200:
        print("put data passed")

def test_get_put_user():
    url = "https://api.restful-api.dev/objects/7"
    new_response=requests.get(url)
    if new_response.status_code==200:
        print("get data  passed")
    new_get_data=new_response.json()
    print(json.dumps(new_get_data,indent=4))