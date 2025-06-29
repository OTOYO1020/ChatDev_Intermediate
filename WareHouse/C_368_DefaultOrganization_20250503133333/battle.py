'''
Module to handle the battle logic for the enemies.
'''
class EnemyBattle:
    def __init__(self, health_list):
        self.health = health_list  # List of health values for each enemy
        self.turns = 0  # Counter for the number of turns taken
    def take_turn(self):
        # Check if there are any enemies left to battle
        if not self.health:
            return
        self.turns += 1  # Increment the turn counter
        # Check if the frontmost enemy has health greater than or equal to 1
        if self.health[0] >= 1:
            # If the turn number is a multiple of 3, decrease health by 3
            if self.turns % 3 == 0:
                self.health[0] -= 3
            else:
                self.health[0] -= 1  # Otherwise, decrease health by 1
            # If the frontmost enemy's health drops to 0 or less, remove that enemy from the list
            if self.health[0] <= 0:
                self.health.pop(0)
    def is_battle_over(self):
        # Check if there are no enemies left
        return len(self.health) == 0  
    def get_turns(self):
        # Return the total number of turns taken
        return self.turns