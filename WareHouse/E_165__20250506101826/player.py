'''
Module containing the Player class for managing player data.
'''
class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.opponents = set()
    def add_opponent(self, opponent_id):
        self.opponents.add(opponent_id)
    def has_faced(self, opponent_id):
        return opponent_id in self.opponents