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
    print(f"A wild {enemy.name} is confronting you about your cars extended warranty!")

    while player.hp > 0 and enemy.hp > 0:
        action = input("Do you want to (A) attack or (R) run? ").lower()

        if action == 'a':
            player_damage = random.randint(1, 10)
            enemy_damage = random.randint(enemy.min_damage, enemy.max_damage)

            print(f"You did {player_damage} damage to the {enemy.name} by saying you can't afford to buy anything")
            enemy.hp -= player_damage

            if enemy.hp > 0:
                print(f"The {enemy.name} attacks back by informing you that it hacked your bank account and knows you can afford upgrades which does {enemy_damage} damage to you")
                player.hp -= enemy_damage
        elif action == 'r':
            escape_chance = random.random()
            if escape_chance > 0.5:
                print("You successfully escaped the clutches of your local car dealership")
                return
            else:
                print("You failed to escape, your legs will not move further dumbo")
                enemy_damage = random.randint(enemy.min_damage, enemy.max_damage)
                print(f"The {enemy.name} attacks and does {enemy_damage} damage to you")
                player.hp -= enemy_damage
        else:
            print("Invalid input. Choose (A) attack or (R) run.")

    if player.hp <= 0:
        print(f"You have been defeated by the {enemy.name}. Game over. You gave into the temptation spwaned by repeated corprate propaganda, in other words they said buy one get one free a couple times.")
        exit()
    else:
        print(f"You defeated the {enemy.name}. You gained some HP and a special item.")
        player.hp += 30
        player.inventory.append(f"{enemy.name} goofy essence")

def main():
    print("Welcome to the car salesman RPG")

    player_name = input("Enter your adventurer's name: ")
    player = Player(name=player_name, hp=100, inventory=[])

    while True:
        walk_command = input("type 'w' to walk: ").lower()

        if walk_command == 'w':
            enemy_appeared = random.random() < 0.25

            if enemy_appeared:
                enemies = [
                    Enemy(name="Rookie salesman", min_damage=3, max_damage=5, hp=20),
                    Enemy(name="Dealership manager", min_damage=5, max_damage=8, hp=25),
                    Enemy(name="Dealership CEO :o", min_damage=10, max_damage=15, hp=30),
                    Enemy(name="Intergalactic supreme car salesman", min_damage=99999999999, max_damage=9999999999999999999, hp=9999999999999999999999999999999)
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


