import random


class Loot:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.used = False

# Definer mulige loot-genstande
possible_loots = [
    Loot("Epic Sword", "Epic"),
    Loot("Rare Shield", "Rare"),
    Loot("Rare Potion", "Rare"),
    Loot("Rare Ring", "Rare"),
    Loot("Common Dagger", "Common"),
    Loot("Common Health Potion", "Common"),
    Loot("Common Scroll", "Common"),
    Loot("Normal Boots", "Normal"),
    Loot("Normal Helmet", "Normal"),
    Loot("Normal Bow", "Normal")
]

# Opret separate lister for hver sjældenhed
epic_loots = [loot for loot in possible_loots if loot.rarity == "Epic"]
rare_loots = [loot for loot in possible_loots if loot.rarity == "Rare"]
common_loots = [loot for loot in possible_loots if loot.rarity == "Common"]
normal_loots = [loot for loot in possible_loots if loot.rarity == "Normal"]

# Funktion til at droppe loot
def drop_loot():
    if epic_loots:
        selected_loot = random.choice(epic_loots)
        epic_loots.remove(selected_loot)
        selected_loot.used = True
        return selected_loot
    elif rare_loots:
        selected_loot = random.choice(rare_loots)
        rare_loots.remove(selected_loot)
        selected_loot.used = True
        return selected_loot
    elif common_loots:
        selected_loot = random.choice(common_loots)
        common_loots.remove(selected_loot)
        selected_loot.used = True
        return selected_loot
    elif normal_loots:
        selected_loot = random.choice(normal_loots)
        normal_loots.remove(selected_loot)
        selected_loot.used = True
        return selected_loot
    else:
        return None

# Drop to loot-genstande
for _ in range(2):
    loot = drop_loot()
    if loot:
        print("Dropped:", loot.name, loot.rarity)
    else:
        print("Ingen loot tilbage at droppe.")