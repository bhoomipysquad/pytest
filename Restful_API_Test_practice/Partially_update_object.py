import json
import requests


def test_patch_data():
    url = "https://api.restful-api.dev/objects/7"
    data = {
   "name": "Apple MacBook Pro 16 (Updated Name)"
}
    response=requests.patch(url,json=data)
    if response.status_code == 200:
        print("patch data passed")

def test_get_data_after_patch():
    url = "https://api.restful-api.dev/objects/7"
    new_response = requests.get(url)
    if new_response == 200:
        print("yes, get data passed")
    new_data=new_response.json()
    print(json.dumps(new_data,indent=4))

