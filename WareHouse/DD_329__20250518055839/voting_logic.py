'''
Voting logic for determining winners based on votes.
'''
from typing import List
def determine_winners(N: int, M: int, votes: List[int]) -> List[int]:
    if M == 0 or not votes:  # Check for empty votes list
        return []  # Return empty winners list if no votes are present
    vote_count = [0] * (N + 1)  # Initialize vote count for each candidate
    winners = []
    current_winner = 1  # Initialize with the first candidate as the default winner
    for i in range(M):
        if 1 <= votes[i] <= N:  # Validate the vote
            vote_count[votes[i]] += 1  # Count the vote for the corresponding candidate
            # Determine the maximum votes received from valid candidates
            max_votes = max(vote_count)
            # Determine the winner (smallest candidate number in case of a tie)
            current_winner = min(j for j in range(1, N + 1) if vote_count[j] == max_votes)
        else:
            print(f"Warning: Invalid vote for candidate {votes[i]} ignored.")
        winners.append(current_winner)  # Store the current winner after each vote
    return winners