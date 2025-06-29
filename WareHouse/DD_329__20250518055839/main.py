'''
Main application file for the Voting System.
'''
from voting_logic import determine_winners
def main():
    # Read input from standard input
    N = int(input("Enter the number of candidates: "))
    votes_input = input("Enter votes (comma-separated): ")
    votes = list(map(int, votes_input.split(',')))
    M = len(votes)
    # Ensure N is a positive integer
    if N <= 0:
        print("Number of candidates must be a positive integer.")
        return
    # Determine winners
    winners = determine_winners(N, M, votes)
    # Output the results
    print("Winners after each valid vote:")
    for winner in winners:
        print(winner)
if __name__ == "__main__":
    main()