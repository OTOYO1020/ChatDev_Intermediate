'''
Main application file for the ScoreApp.
'''
import sys
from score_processor import process_scores  # Import the function
def main():
    '''
    Main function to execute the score processing.
    '''
    N = int(input("Enter the number of players: "))
    if N < 2:
        print("Not enough players to determine second lowest.")
        return
    A = list(map(int, input("Enter the scores of players (space-separated): ").split()))
    if len(A) != N:
        print("The number of scores does not match the number of players.")
        return
    # New validation for non-negative scores
    if any(score < 0 for score in A):
        print("Scores must be non-negative integers.")
        return
    second_lowest_index = process_scores(A)  # Call the imported function
    if second_lowest_index is not None:
        print(f"Player with second lowest score: Player {second_lowest_index}")
    else:
        print("Not enough unique players to determine second lowest.")
if __name__ == "__main__":
    main()