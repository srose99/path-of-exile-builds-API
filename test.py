import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "builds/1", {"Name": "SST Champion", "Budget": "HighEnd", "Pastebin": "pastebin.URL", "Description": "Fast and tanky"})
print(response.json())
input()
response = requests.get(BASE + "builds/1")
print(response.json())