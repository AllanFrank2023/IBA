import random 

 
 

class Monster: 

    def __init__(self, Name, Health, Defence, Strenth): 

        self.Name = Name 

        self.Health = Health 

        self.Defence = Defence 

        self.strenth = Strenth 

 
 

    def take_dmg(self, dmg): 

        if dmg < self.Health: 

            self.Health -= dmg 

        else: 

            self.Health = 0 

        return self.Health 

 
 

    def Attack(self): 

        Monster_Skade = self.strenth  

        return Monster_Skade 

 
 

# Hvis vi bruger dette, så skal vi finde ud af hvordan vi bruger det under kampen - her skal det være tilfældigt, om monsteret vælger at bruge defence. 

#    def monster_use_defence(self): 

#       return random.choice([True,False]) 

 
 

Monster1 = Monster("Goblin", 30, 5, 8) 

Monster2 = Monster("Skeleton", 25, 3, 10) 

Monster3 = Monster("Troll", 50, 8, 15) 

Monster4 = Monster("Vampyre", 45, 5, 12) 

Monster5 = Monster("Giant", 80, 10, 20) 

Monster6 = Monster("Dragon",100,30,50) 

 

monstre_liste = [Monster1, Monster2, Monster3, Monster4, Monster5, Monster6] 

