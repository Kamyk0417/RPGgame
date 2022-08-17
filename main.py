from dane import lvlstats

class Player:
    def __init__(self, name, level=1, exp=0, hp=50, mana=50, gold=0, eq={}):
        self.name = name
        self.level = level
        self.exp = exp
        self.hp = hp
        self.mana = mana
        self.gold = gold
        self.eq = eq
    def xp_gain(self, gain):
        lvle = lvlstats()
        while self.exp + gain >= lvle[0][self.level-1]:
            gain -= (lvle[0][self.level-1]-self.exp)
            self.exp = 0
            self.level += 1
            print("You leveled up!\n"
            "HP and mana fully regened, you got +20 max HP and mana for every level up\n"
            f"Your max HP and mana now: {lvle[1][self.level-1]}")
        self.exp = gain
        print(f"Now you have level: {self.level} and exp: {self.exp}/{lvle[0][self.level-1]}")

p1 = Player("a")
p1.xp_gain(9)
p1.xp_gain(80)

