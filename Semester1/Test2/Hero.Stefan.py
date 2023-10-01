class hero:
    """
    This is the hero class which define how the hero is defined. 
    This hero can pickup loot item from the monster, take damage and do on off defence, attack or move. 
    The hero needs som attributes to define the attack power, defence power, backpack, equipment and health. 
    """
    
    def __init__(self, name):
        """
        The constructor sets the default value of the hero class, and also add the default items to the backpack. 
        """
        self.equipment = []
        self.pos = [0, 0]
        self.name=name
        self.health = 20
        self.attack = 0
        self.defence = 0
        self.backpack = ["Rope", "fint and steel", "candle"]
        self.stand = "move"

    def heroPickup(self, item):
        """
        This is method for picking up items from the ground. 
        The items, that are collected, is placed in the backpack. 
        There is only room for ten items in the backpack. 

        param: item: string containing the information about the item dropped
        return: amount: the amount of item in the backpack.
        """
        if len(self.backpack) < 11:
            self.backpack.append(item)
        
        return len(self.backpack)

    def heroDamage(self, damage):
        """
        The damage method, is used for the hero to take damage. 
        If the damage is greate or equal to remaining health, the hero is dead. 
        
        param: damage: The amount of damage inflicted on hero. 
        return: health: The remaining health of the hero. 
        """
        if damage - self.defence < 0: 
            return self.health

        if damage < self.health:
            self.health -= (damage -self.defence)
        else:
            self.health = 0
        
        return self.health

    def heroDefence(self):
        """
        Hero take defence stannds and boost defence stats by 1.5 times the hero stat, 
        but the hero also reduced the amount of attack by 0.5 times the hero stat.

        """
        if self.stand != "defence":
            self.attack = 0.5 * self.attack
            self.defence = 1.5 * self.attack
            self.stand = "defence"


    def heroAttack(self):
        """
        Hero perform attack. 

        return: amount: the amount of total attack
        """
        if self.stand == "defence":
            self.attack = 2 * self.attack
            self.defence = self.attack / 1.5
            self.stand = "attack"
        return self.attack

    def heroMove(self, dir, steps):
        """
        Move the hero around the board.
        The board is made of 2d grid pattern described in a list [x,y]. 
        l is the same as minus x
        r is the same as x
        u is the same as y
        d is the same as minus y

        param: pos: The current possint in the 2d grid.
        param: dir: The direction of movement, l, r, u, d
        param: steps: The amount of steps to perform the movement. 
        return: pos: the new position in 2d grid. 
        """
        
        if (dir == "l"):
            self.pos[0] -= steps
        elif dir == "r":
            self.pos[0] += steps
        elif dir == "d":
            self.pos[1] -= steps
        elif dir == "u":
            self.pos[1] += steps

        return self.pos
        
       
if __name__ == "__main__":
    """
        IF the file is executed, the following test is performed: 
        1) Test picking up loot
        2) The hero should take dmg
        3) The hero should go in defence mode
        4) The hero should go in attack mode
        5) The hero should move in a direction 
        """
    # Pre test
    ## The main hero 
    hercules = hero("Hercules")
    item = "Rotten flesh"
    hercules.attack = 2
    hercules.defence = 2

    ## Secondary Hero to perform the required actions
    monster = hero("Dr. Evil")
    monster.attack = 3
    monster.defence = 1

    # Test 1)
    print("\n1) Hero pickups items")
    hercules.heroPickup(item)
    print(hercules.name + " backpack now has the following items: " + str(hercules.backpack))

    # Test 2) 
    print("\n2) The hero should take dmg")
    print(hercules.name + " has " + str(hercules.health) + " health")
    dmg = hercules.health - hercules.heroDamage(monster.heroAttack())
    print(hercules.name + " takes " + str(dmg) + " in damage")
    print(hercules.name + " has " + str(hercules.health) + " health")
    
    # Test 3) 
    print("\n3) The hero should go in defence mode")
    hercules.heroDefence()
    print(hercules.name + " is now in stands: " + hercules.stand)
    print(hercules.name + " has " + str(hercules.health) + " health")
    dmg = hercules.health - hercules.heroDamage(monster.heroAttack())
    print(hercules.name + " takes " + str(dmg) + " in damage")
    print(hercules.name + " has " + str(hercules.health) + " health")

    # Test 4) 
    print("\n4) The hero should go in attack mode")
    print(monster.name + " has " + str(monster.health) + " health")
    dmg = monster.health - monster.heroDamage(hercules.heroAttack())
    print(hercules.name + " takes " + str(dmg) + " in damage")
    print(monster.name + " has " + str(monster.health) + " health")

    # Test 5) 
    print("\n5) The hero should move in a direction ")
    print(hercules.name + " current position is: " + str(hercules.pos))
    print(hercules.name + " new position is: " + str(hercules.heroMove("l", 1)))
    print(hercules.name + " current position is: " + str(hercules.pos))
    print(hercules.name + " new position is: " + str(hercules.heroMove("r", 1)))
    print(hercules.name + " current position is: " + str(hercules.pos))
    print(hercules.name + " new position is: " + str(hercules.heroMove("u", 1)))
    print(hercules.name + " current position is: " + str(hercules.pos))
    print(hercules.name + " new position is: " + str(hercules.heroMove("d", 1)))

 