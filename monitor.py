import json

file = open("rabbit.json")

dados = json.load(file)

for queue in dados:
    if queue["messages_ready"] != None:
        print(queue["name"], queue["messages_ready"])