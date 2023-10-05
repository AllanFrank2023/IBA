import random

class Loot:
    def __init__(self, name, rarity):
        

# Liste over mulige items og deres sjældenheder
items = [
    {"Name": "Epic Item", "Rarity": "Epic"},
    {"Name": "Rare Item 1", "Rarity": "Rare"},
    {"Name": "Rare Item 2", "Rarity": "Rare"},
    {"Name": "Rare Item 3", "Rarity": "Rare"},
    {"Name": "Common Item 1", "Rarity": "Common"},
    {"Name": "Common Item 2", "Rarity": "Common"},
    {"Name": "Common Item 3", "Rarity": "Common"},
    {"Name": "Normal Item 1", "Rarity": "Normal"},
    {"Name": "Normal Item 2", "Rarity": "Normal"},
    {"Name": "Normal Item 3", "Rarity": "Normal"},
]

# Liste til at holde styr på brugte items
used_items = []

# Funktion til at vælge et tilfældigt item baseret på reglerne
def choose_item():
    while True:
        item = random.choice(items)
        if item["Rarity"] == "Epic" and items.count(item) > used_items.count(item):
            used_items.append(item)
            return item

# Funktion til at simulere dråber fra et monster
def monster_drop():
    drops = []
    for _ in range(2):
        item = choose_item()
        drops.append(item)
    return drops

# Simulering af dråber fra et monster
monster_drops = monster_drop()

# Udskriv de genererede items
for idx, item in enumerate(monster_drops, start=1):
    print(f"Drop {idx}:")
    print(item["Name"])
    print("Rarity:", item["Rarity"])
    print()

# Hvis du vil se, hvilke items der er brugt
print("Brugte items:")
for item in used_items:
    print(item["Name"])
