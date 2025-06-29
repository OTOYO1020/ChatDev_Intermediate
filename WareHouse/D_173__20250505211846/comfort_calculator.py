'''
Module for calculating total comfort based on player friendliness.
'''
class ComfortCalculator:
    def __init__(self, friendliness):
        # Pair each friendliness value with its original index and sort in descending order
        self.friendliness = sorted(enumerate(friendliness), key=lambda x: x[1], reverse=True)
        self.original_friendliness = friendliness  # Store original friendliness values for access
    def calculate_total_comfort(self):
        total_comfort = 0
        n = len(self.friendliness)
        for i in range(n):
            if i == 0:
                # First player's comfort is set to 0
                comfort = 0
            else:
                # Get the original indices of the adjacent players
                left_index = (i - 1) % n  # Previous player (circular)
                right_index = (i + 1) % n  # Next player (circular)
                # Use the original indices to access the correct players' friendliness values
                left_player_original = self.friendliness[left_index][0]  # Original index of the left player
                right_player_original = self.friendliness[right_index][0]  # Original index of the right player
                comfort = min(self.original_friendliness[left_player_original], self.original_friendliness[right_player_original])
            total_comfort += comfort
        return total_comfort