import random
class Player:
    def __init__(self, name, hp, inventory):
        self.name = name
        self.hp = hp
        self.inventory = inventory

class Enemy:
    def __init__(self, name, min_damage, max_damage, hp):
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.hp = hp

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")

    while player.hp > 0 and enemy.hp > 0:
        action = input("Do you want to (A) attack or (R) run? ").lower()

        if action == 'a':
            player_damage = random.randint(1, 10)
            enemy_damage = random.randint(enemy.min_damage, enemy.max_damage)

            print(f"You did {player_damage} damage to the {enemy.name}")
            enemy.hp -= player_damage

            if enemy.hp > 0:
                print(f"The {enemy.name} attacks back and does {enemy_damage} damage to you")
                player.hp -= enemy_damage
        elif action == 'r':
            escape_chance = random.random()
            if escape_chance > 0.5:
                print("You successfully escaped")
                return
            else:
                print("You failed to escape, your legs will not move further dumbo")
                enemy_damage = random.randint(enemy.min_damage, enemy.max_damage)
                print(f"The {enemy.name} attacks and does {enemy_damage} damage to you")
                player.hp -= enemy_damage
        else:
            print("Invalid input. Choose (A) attack or (R) run.")

    if player.hp <= 0:
        print(f"You have been defeated by the {enemy.name}. Game over(you have become a goofy goober for the rest of time :())")
    else:
        print(f"You defeated the {enemy.name}. You gained some HP and a special item.")
        player.hp += 10
        player.inventory.append(f"{enemy.name} goofy essence")

def main():
    print("Welcome to the goofy goober RPG :/")

    player_name = input("Enter your adventurer's name: ")
    player = Player(name=player_name, hp=50, inventory=[])

    while True:
        walk_command = input("type 'w' to walk: ").lower()

        if walk_command == 'w':
            enemy_appeared = random.random() < 0.25

            if enemy_appeared:
                enemies = [
                    Enemy(name="goofy goober", min_damage=5, max_damage=10, hp=20),
                    Enemy(name="silly goober", min_damage=8, max_damage=15, hp=25),
                    Enemy(name="supreme wacky guy", min_damage=15, max_damage=25, hp=30)
                ]
                random_enemy = random.choice(enemies)
                battle(player, random_enemy)
            else:
                print("You walk forward")

        elif walk_command.lower() == 'p' or walk_command.lower() == 'print':
            print(f"Name: {player.name}")
            print(f"HP: {player.hp}")
            print("Inventory:")
            for item in player.inventory:
                print(f" - {item}")
        else:
            print("Invalid command. Press 'w' to walk or 'p' to open inventory.")

if __name__ == "__main__":
    main()


