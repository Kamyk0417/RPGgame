from random import randint

def duel(p, e, lvl0):
    e.appear(randint(lvl0, p.level))
    print("Roll the dice to increase your speed")
    p_dmg_2 = p.stats["agility"] + randint(1, 6)
    e_dmg_2 = e.speed + randint(1, 6)
    print(f"Your speed - {p_dmg_2}, enemy's - {e_dmg_2}")
    if e_dmg_2 > p_dmg_2:
        print(f"{e.name} attacks first")
        p.take_dmg(e.atk)
    while e.alive and not p.game_over:
        print(f"You attacked for {p.stats['strength']}")
        e.take_dmg(p.stats["strength"])
        if not e.alive:
            break
        p.take_dmg(e.atk)
