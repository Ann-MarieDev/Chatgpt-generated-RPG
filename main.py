import random
import math 

class Player:
    def __init__(self, name, health, attack, defense, level):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.inventory = []

    def display_stats(self):
        print(f"{self.name} - Level {self.level} | HP: {self.health} | Attack: {self.attack} | Defense: {self.defense}")

class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.health = 20 * level
        self.attack = 5 * level
        self.defense = 2 * level

def generate_enemy(player_level):
    enemy_level = random.randint(max(1, player_level - 2), player_level + 2)
    enemy_name = random.choice(["Goblin", "Skeleton", "Orc", "Dark Wolf"])
    return Enemy(enemy_name, enemy_level)

def battle(player):
    print("You embark on a quest to defeat the evil sorcerer who has unleashed monsters upon the land.")
    print("As you travel through the mystical forest, a wild monster appears! Battle starts!")

    while player.health > 0:
        enemy = generate_enemy(player.level)
        print(f"A wild {enemy.name} appears! Battle starts!")

        while player.health > 0 and enemy.health > 0:
            player.display_stats()
            print(f"{enemy.name} - HP: {enemy.health}")

            print("1. Attack")
            print("2. Defend")
            print("3. Use item")
            choice = input("Choose your action (1/2/3): ")

            if choice == '1':
                # Player attacks
                damage = max(0, player.attack - enemy.defense)
                enemy.health -= damage
                print(f"You attack {enemy.name} for {damage} damage!")

                # Enemy attacks back
                damage = max(0, enemy.attack - player.defense)
                player.health -= damage
                print(f"{enemy.name} counterattacks for {damage} damage!")

            elif choice == '2':
                # Player defends, reducing incoming damage
                player.defense += 2
                print("You defend, increasing your defense!")

                # Enemy attacks back
                damage = max(0, enemy.attack - player.defense)
                player.health -= damage
                print(f"{enemy.name} counterattacks for {damage} damage!")

                # Reset player's defense for the next turn
                player.defense -= 2

            elif choice == '3':
                if player.inventory:
                    # Use a random item from the inventory
                    used_item = random.choice(player.inventory)
                    player.inventory.remove(used_item)
                    print(f"You use {used_item} in the battle.")
                    # Add item effects here if needed.
                else:
                    print("You have no items in your inventory.")

            else:
                print("Invalid choice. Try again.")

        if player.health > 0:
            print(f"{enemy.name} was defeated! You continue your journey.")
            player.level += 1
            print(f"You leveled up to Level {player.level}!")

    print("You were defeated. The evil sorcerer's minions have overwhelmed you. Game over.")

# Example usage:
player = Player("Brave Knight", 100, 15, 5, 1)
player.inventory = ["Health Potion", "Attack Boost"]
battle(player)
