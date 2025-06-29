'''
Tournament logic implementation for finding the second place player.
'''
from typing import List
def find_second_place(N: int, A: List[int]) -> int:
    players = [(i + 1, A[i]) for i in range(N)]  # (label, rating)
    final_loser = None  # Initialize final_loser
    while len(players) > 1:
        players.sort(key=lambda x: x[0])  # Sort by label
        winners = []
        # Pair players for matches
        for i in range(0, len(players) - 1, 2):  # Pair players
            winner = players[i] if players[i][1] > players[i + 1][1] else players[i + 1]
            loser = players[i] if players[i][1] < players[i + 1][1] else players[i + 1]
            winners.append(winner)  # Track the winner
            # Track the loser for the final match
            if len(players) == 2:  # Only track losers when we are at the final match
                final_loser = loser
        # If odd number of players, last one automatically advances
        if len(players) % 2 == 1:
            winners.append(players[-1])  # Last player advances without a match
        players = winners  # Update players to only include winners
    # After the loop, we have the final match between the last two players
    if len(players) == 2:
        final_loser = players[0] if players[0][1] < players[1][1] else players[1]
    # Return the label of the player who lost in the final match
    return final_loser[0] if final_loser else players[0][0]  # Fallback if final_loser is None