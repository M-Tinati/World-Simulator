Creatures = [
    {"name": "Wolf", "health": 80},
    {"name": "Cat", "health": 20},
    {"name": "Human", "health": 90},
    {"name": "Monster", "health": 5}
]
new_creatures = Creatures.copy()
for i in new_creatures:
    if i["health"] <=30:
        Creatures.remove(i)
print(Creatures)
print("===================")
print(new_creatures)