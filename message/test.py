import requests

data = {}
data["longitude"] = 12
data["latitude"] = 12
data["user"] = {"user_id":123,"telegram_id":"asdasd","phone":"12312312","full_name":"asd"}

data["before"] = "http://localhost:8000/media/219.png"



r = requests.put("http://127.0.0.1:8000/api/patients",data=data)

print(r.content)

