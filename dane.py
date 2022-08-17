def lvlstats():
    lvls = [(x+1)*x*5 for x in range(1,30)]
    mana_hp = [50+20*y for y in range(1,30)]
    return lvls, mana_hp

print(lvlstats())