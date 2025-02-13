import json

import pytest
import requests

@pytest.mark.regression
def test_delete_data():
    url="https://api.restful-api.dev/objects/6"
    response=requests.delete(url)
    if response.status_code==200:
        print("data deleted")

def test_after_delete_get_data():
    url="https://api.restful-api.dev/objects/6"
    new_response=requests.get(url)
    if new_response.status_code==200:
        print("id is not existing")
    get_data=new_response.json()
    print(json.dumps(get_data,indent=4))




