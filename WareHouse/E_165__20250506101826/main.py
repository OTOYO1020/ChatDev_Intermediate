'''
Main application file for the Player Assignment App.
'''
import random
from player import Player
class PlayerAssignmentApp:
    def __init__(self):
        self.players = []
        self.assignments = []
    def assign_players(self, N, M):
        self.players = [Player(i) for i in range(1, N + 1)]
        self.assignments = []
        self.generate_assignments(N, M)
    def generate_assignments(self, N, M):
        opponents_faced = {player.player_id: set() for player in self.players}  # Track opponents faced by each player
        current_player_ids = [player.player_id for player in self.players]  # Maintain original player IDs
        for _ in range(M):
            round_assignments = []  # Store assignments for the current round
            for player_id in current_player_ids:
                available_opponents = [opponent for opponent in current_player_ids 
                                       if opponent != player_id and 
                                       opponent not in opponents_faced[player_id]]
                if len(available_opponents) >= 2:  # Ensure at least two opponents are available
                    # Randomly select two distinct opponents
                    opponent_id, second_opponent = random.sample(available_opponents, 2)
                    # Add opponents to the player's record
                    opponents_faced[player_id].add(opponent_id)
                    opponents_faced[player_id].add(second_opponent)
                    # Append the assignments for the current round
                    round_assignments.append((player_id, opponent_id))
                    round_assignments.append((player_id, second_opponent))
            self.assignments.extend(round_assignments)  # Add current round assignments to the overall assignments
            self.rotate_players(current_player_ids)  # Rotate players after all assignments for the current playing field
    def rotate_players(self, current_player_ids):
        # Rotate players by incrementing their IDs and wrapping around using modulo
        for i in range(len(current_player_ids)):
            current_player_ids[i] += 1
            if current_player_ids[i] > len(self.players):
                current_player_ids[i] = 1
    def print_assignments(self):
        for assignment in self.assignments:
            print(f"{assignment[0]} vs {assignment[1]}")
if __name__ == "__main__":
    N = int(input())
    M = int(input())
    app = PlayerAssignmentApp()
    app.assign_players(N, M)
    app.print_assignments()