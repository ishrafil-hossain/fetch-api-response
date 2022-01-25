import requests
from requests.structures import CaseInsensitiveDict

url = "https://gorest.co.in/public/v1/users"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer d7c01847de4c083cb154e9a533294301e9f05f93dbae7d589e42ece63226c0a3"


resp = requests.get(url, headers=headers)

print(resp.text)