import os
import pandas as pd

#clearing console decorator
clear = lambda: os.system("cls")

def cls_stats(func):
    def wrapper(*args, **kwargs):
        clear()
        val = func(*args, **kwargs)
        return val
    return wrapper

#exp mana and hp increase with lvl
def lvlstats():
    lvls = [(x+1)*x*5 for x in range(1,30)]
    mana_hp = [20+10*y for y in range(1,30)]
    return lvls, mana_hp


class Player:
    game_over = False
    def __init__(self, name, level=1, exp=0, hp=50, mana=50, gold=0, stats={"strength":5, "agility":3, "intellect":0, "charisma":0, "luck":0}, eq={}):
        self.name = name
        self.level = level
        self.exp = exp
        self.hp = hp
        self.mana = mana
        self.gold = gold
        self.eq = eq
        self.stats = stats

    @cls_stats
    def show_stats(self):
        stats_ds = [["name", "level", "exp", "hp", "mana", "gold"], [self.name, self.level, self.exp, self.hp, self.mana, self.gold]]
        stats_pd = pd.DataFrame(stats_ds)
        print("\n", stats_pd)

    def xp_gain(self, gain):
        lvls = lvlstats()
        while self.exp + gain >= lvls[0][self.level-1]:
            gain -= (lvls[0][self.level-1]-self.exp)
            self.exp = 0
            self.level += 1
            print("You leveled up!\n"
            "HP and mana fully regened, you got +20 max HP and mana for every level up\n"
            f"Your max HP and mana now: {lvls[1][self.level-1]}")
        self.exp = gain
        print(f"Now you have level: {self.level} and exp: {self.exp}/{lvls[0][self.level-1]}")

    def take_dmg(self, dmg):
        if dmg < self.hp:
            self.hp -= dmg
            print(f"You got damaged for {dmg} hp - now you have {self.hp} hp")
        else:
            print("YOU DIED, GAME OVER")
            self.game_over = True
