'''
Logic for determining the second place player in a tournament.
'''
def find_second_place(N, A):
    # Validate N and the size of A
    if N < 0 or (2 ** N) > 1024:  # Example limit for players
        raise ValueError("N must be such that 2^N is a valid number of players (e.g., <= 1024).")
    if len(A) != 2 ** N:
        raise ValueError(f"Ratings array must have exactly {2 ** N} elements.")
    # Ensure that the number of players is a power of two
    if (len(A) & (len(A) - 1)) != 0:  # Check if the length is a power of two
        raise ValueError("The number of players must be a power of two.")
    winners = list(range(1, 2**N + 1))  # Player labels from 1 to 2^N
    for i in range(1, N + 1):
        next_winners = []  # Create a new list for the winners of the current round
        for j in range(0, 2**(N - i)):
            player1 = winners[2 * j]      # Get the label of player 1
            player2 = winners[2 * j + 1]  # Get the label of player 2
            # Determine the winner based on ratings
            if A[player1 - 1] > A[player2 - 1]:  # Access ratings using 0-based index
                next_winners.append(player1)  # Player1 wins
            elif A[player1 - 1] < A[player2 - 1]:
                next_winners.append(player2)  # Player2 wins
            else:
                # Tie-breaking: raise an exception if there's a tie
                raise ValueError(f"Tie between players {player1} and {player2} with rating {A[player1 - 1]}.")
        winners = next_winners  # Update winners to the next round's winners
    # Last two players in winners are the finalists
    finalists = winners  
    # Determine the second place based on the final match
    if A[finalists[0] - 1] > A[finalists[1] - 1]:
        second_place = finalists[1]  # Finalist 2 loses
    else:
        second_place = finalists[0]  # Finalist 1 loses
    return second_place