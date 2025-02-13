import requests
import json

url = "https://reqres.in/api/users/2"
response = requests.delete(url)
if response.status_code==204:
    print("data successfully deleted")
else:
    print("spmething went wrong")

