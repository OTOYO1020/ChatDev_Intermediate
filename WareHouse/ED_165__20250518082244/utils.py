'''
Utility functions for assigning playing fields.
'''
from typing import List, Tuple
def assign_playing_fields(N: int, M: int) -> List[Tuple[int, int]]:
    # Check constraint
    if M * 2 + 1 > N:
        raise ValueError("Constraint not satisfied: M * 2 + 1 must be <= N")
    assignments = []
    players = list(range(1, N + 1))
    opponent_tracker = {player: set() for player in players}  # Track opponents
    for _ in range(M):
        round_assignments = []
        for i in range(len(players)):
            for j in range(i + 1, len(players)):
                player1 = players[i]
                player2 = players[j]
                # Check if they have fought
                if player2 not in opponent_tracker[player1]:
                    round_assignments.append((player1, player2))
                    opponent_tracker[player1].add(player2)
                    opponent_tracker[player2].add(player1)
                    if len(round_assignments) == M:  # Stop if we have enough pairs
                        break
            if len(round_assignments) == M:
                break
        if len(round_assignments) < M:
            raise ValueError("Not enough distinct pairs can be formed with the given players.")
        assignments.extend(round_assignments)
        # Increment players for the next round
        players = [(player % N) + 1 for player in players]
    return assignments