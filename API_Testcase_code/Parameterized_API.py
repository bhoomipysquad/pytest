import json
import pytest
import requests

url="https://reqres.in/api/users?page=2"

@pytest.mark.parametrize("id, first_name", [
    (7, "Michael"),
    (8, "Lindsay"),
    (9, "Tobias")
])

def test_get_user_by_id(id, first_name):
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    print(json.dumps(data, indent=4))
