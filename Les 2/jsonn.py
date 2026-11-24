import json

data = {"naam": "Luc", "Leeftijd": 16, "fav_kleur": "oranje"}

data = json.dumps(data)
print(data)
data = json.loads(data)