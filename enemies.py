from random import choices, randint
from player import cls_stats

rarity = {"common": 10, "uncommon": 7, "rare": 4, "very rare": 1, "epic": 0.2, "legendary": 0.05}

pos_loot = {
    "Goblin": {"fish head (gross)": "common", "raw meat": "common", "bag of glass": "uncommon", "silver ring": "rare", "gold ring": "very rare"}

}

class Enemy:

    def __init__(self, hp, atk, speed):
        self.hp = hp
        self.atk = atk
        self.speed = speed
    
    def attack(self):
        print(f"I attacked for {self.atk} dmg")

        

class Goblin(Enemy):

    desc = "Goblin\nSome filty and greedy creature"
    def __init__(self, hp=3, atk=4, speed=1):
        super().__init__(hp, atk, speed)
    
    @cls_stats
    def appear(self, level):
        print(f"A level {level} goblin just appeared! Prepare yourself!")
        self.hp += (level-1)*3
        self.atk += (level-1)

    @cls_stats
    def die(self):
        dec = input("Press [l] to loot or [s] to skip ")
        if dec.lower() == "s":
            pass
        if dec.lower() == "l":
            loot = set(choices((list(pos_loot["Goblin"].keys())), weights = [rarity[i] for i in pos_loot["Goblin"].values()], k = randint(1,3)))
            loot2 = {"gold": randint(5, 20)}
            loot2.update({i: pos_loot["Goblin"][i] for i in loot})
            print(loot2)
            

g1 = Goblin()
g1.die()




