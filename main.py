import player, enemies
from random import randint

print("Welcome to the game\n\n")
name = input("Name your hero: ")
p1 = player.Player(name)

game_over = False

while not game_over:
    g1 = enemies.Goblin()
    while g1.alive:
        g1.appear(randint(1, p1.level))
        print("Roll the dice to increase your speed")
        p_dmg_2 = p1.stats["agility"] + randint(1, 6)
        e_dmg_2 = g1.speed + randint(1, 6)
        print(f"Your speed - {p_dmg_2}, enemy's - {e_dmg_2}")







