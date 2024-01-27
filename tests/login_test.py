import requests

from ctpbee_webline.util import encrypt

payload = {"username": "admin", "password": encrypt("123456")}

response = requests.post("http://127.0.0.1:7960/web/login", data=payload).json()
print("login response: ", response)
token = f'Bearer {response["data"]["token"]}'
print(response)

response = requests.get("http://127.0.0.1:7960/web/logout", ).json()
print(response)

response = requests.get("http://127.0.0.1:7960/web/logout", headers={"Authorization": token}).json()
print(response)
