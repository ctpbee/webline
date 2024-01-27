import requests

from ctpbee_webline.util import encrypt

payload = {"username": "admin", "password": str(encrypt("123456"))}
response = requests.post("http://127.0.0.1:7960/web/login", data=payload).json()
print(response)
token = f'Bearer {response["data"]["token"]}'
print("登录返回:", response)

payload["password"] = encrypt("123456")
response = requests.post("http://127.0.0.1:7960/web/change_password", data=payload,
                         headers={"Authorization": token}).json()
token = f'Bearer {response["data"]["token"]}'
print("修改密码返还:", response)


payload["password"] = encrypt("123456")
response = requests.post("http://127.0.0.1:7960/web/change_password", data=payload,
                         headers={"Authorization": token}).json()
print("重置密码返还:", response)
