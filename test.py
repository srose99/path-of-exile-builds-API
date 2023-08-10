import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "SST Champion", "budget": "HighEnd", "pastebin": "pastebin.URL", "description": "Fast and Tanky"},
        {"name": "RF Inquisitor", "budget": "League-Starter", "pastebin": "pastebin.URl", "description": "Tanky"}]

for i in range(len(data)):
    response = requests.put(BASE + "builds/" + str(i), json=data[i])
    if response.status_code == 200:
        print("Build", i, "created successfully")
    else:
        print("Error creating Build", i)
        print(response.status_code)

input()
response = requests.get(BASE + "builds/1")
if response.status_code == 200:
    print(response.json())
else:
    print("Error retrieving Build 1")