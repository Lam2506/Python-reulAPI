import json
data = {
    "name" : "lam",
    "age" : 20,
    "hobby" : "hoc lap trinh",
    "diem" : 8.5,
}
with open("data.json", "w", encoding='utf-8') as file:
    json.dump(data, file)