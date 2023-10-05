import random

class Loot:
    def __init__(self, rarity):
        self.attack_modifier = 0
        self.defence_modifier = 0
        self.name = ""
        self.value = 0
        self.rarity = rarity

    def generate(self):
        if self.rarity == "Epic":
            self.attack_modifier = random.randint(20, 50)
            self.defence_modifier = random.randint(3, 10)
            self.name = "Epic Item"
            self.value = random.randint(1000, 5000)
        elif self.rarity == "Rare":
            self.attack_modifier = random.randint(5, 15)
            self.defence_modifier = random.randint(1, 5)
            self.name = "Rare Item"
            self.value = random.randint(200, 999)
        elif self.rarity == "Common":
            self.attack_modifier = random.randint(1, 5)
            self.defence_modifier = random.randint(1, 5)
            self.name = "Common Item"
            self.value = random.randint(50, 199)
        elif self.rarity == "Normal":
            self.attack_modifier = random.randint(0, 2)
            self.defence_modifier = random.randint(0, 2)
            self.name = "Normal Item"
            self.value = random.randint(10, 49)

    def __str__(self):
        return "Name:", self.name, "\n,Rarity:", self.rarity,"\nAttack Modifier:", self.attack_modifier, "\nDefence Modifier:", self.defence_modifier, "\nValue:", self.value

# Generer ti loot-objekter med de specificerede regler
loots = []
rarities = ["Epic", "Rare", "Common", "Normal"]

for _ in range(1):
    loots.append(Loot("Epic"))
for _ in range(3):
    loots.append(Loot("Rare"))
for _ in range(3):
    loots.append(Loot("Common"))
for _ in range(3):
    loots.append(Loot("Normal"))

for loot in loots:
    loot.generate()
    print(loot)
    print("="*20)
