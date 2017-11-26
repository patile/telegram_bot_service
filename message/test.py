import requests

data = {}
data["longitude"] = 12
data["latitude"] = 12
data["user"] = {}
data["user"]["id"] = 1
data["user"]["telegram_id"]="asdasd"
data["user"]["phone"]= "12312312"
data["user"]["full_name"]="asd"

data["before"] = "/219.png"

print(data)


r = requests.post("http://127.0.0.1:8000/api/patients",json=data)

print(r.content)

