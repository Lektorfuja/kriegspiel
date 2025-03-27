import random

class Kriegspiel:
    def __init__(self):
        self.board_size = 8
        self.player_units = {'Infantry': 5, 'Cavalry': 3, 'Artillery': 2}
        self.enemy_units = {'Infantry': 5, 'Cavalry': 3, 'Artillery': 2}
        self.turn = 1
    
    def display_status(self):
        print(f"Turn {self.turn}")
        print("Your forces:")
        for unit, count in self.player_units.items():
            print(f"  {unit}: {count}")
        print("Enemy forces:")
        for unit, count in self.enemy_units.items():
            print(f"  {unit}: {count}")
        print()
    
    def player_attack(self):
        print("Choose a unit to attack with:")
        for unit in self.player_units:
            print(f"  {unit}")
        choice = input("Enter unit name: ")
        if choice not in self.player_units or self.player_units[choice] == 0:
            print("Invalid choice or no units left.")
            return
        
        enemy_unit = random.choice(list(self.enemy_units.keys()))
        print(f"Your {choice} attacks enemy {enemy_unit}!")
        if random.random() > 0.5:
            self.enemy_units[enemy_unit] -= 1
            print(f"Enemy {enemy_unit} unit destroyed!")
            if self.enemy_units[enemy_unit] == 0:
                del self.enemy_units[enemy_unit]
        else:
            print("Attack missed!")
        
    def enemy_attack(self):
        if not self.enemy_units:
            return
        enemy_unit = random.choice(list(self.enemy_units.keys()))
        player_unit = random.choice(list(self.player_units.keys()))
        print(f"Enemy {enemy_unit} attacks your {player_unit}!")
        if random.random() > 0.5:
            self.player_units[player_unit] -= 1
            print(f"Your {player_unit} unit was destroyed!")
            if self.player_units[player_unit] == 0:
                del self.player_units[player_unit]
        else:
            print("Enemy attack missed!")
    
    def check_game_over(self):
        if not self.player_units:
            print("You have lost the battle!")
            return True
        elif not self.enemy_units:
            print("You have won the battle!")
            return True
        return False
    
    def play(self):
        print("Welcome to Kriegspiel!")
        while True:
            self.display_status()
            self.player_attack()
            if self.check_game_over():
                break
            self.enemy_attack()
            if self.check_game_over():
                break
            self.turn += 1
        print("Game Over.")

if __name__ == "__main__":
    game = Kriegspiel()
    game.play()
