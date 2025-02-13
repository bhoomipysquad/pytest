import json
import requests

def test_create_user():
   url="https://api.restful-api.dev/objects"
   data={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}
   response=requests.post(url,json=data)
   assert response.status_code==200,f"its not working{response.status_code}"

def test_get_detail():
   url="https://api.restful-api.dev/objects"
   get_response=requests.get(url)
   if get_response.status_code==200:
     print("yes it's working")
   get_data=get_response.json()
   print(json.dumps(get_data,indent=4))


