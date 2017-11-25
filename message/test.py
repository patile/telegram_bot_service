import requests

data = {}
data["longitude"] = 12
data["latitude"] = 12
data["user"] = {}
data["user"]["user_id"] = 123
data["user"]["telegram_id"] = "asdasdasd"
data["user"]["phone"] = "1231231312"
data["user"]["full_name"] = "asdasdasd"
data["before"] = "http://localhost:8000/media/219.png"
print(data)


r = requests.put("http://127.0.0.1:8000/api/patients",data=data)

print(r.content)