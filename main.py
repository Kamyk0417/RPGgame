import player, enemies
import events

print("Welcome to the game\n")
name = input("Name your hero: ")
p1 = player.Player("name")
p1.show_stats()

while not p1.game_over:
g1 = enemies.Goblin()
events.duel(p1,g1,1)




