'''
Main application file for the voting system using standard input and output.
'''
from vote_counter import VoteCounter
def main():
    # Read number of candidates and votes
    N, M = map(int, input().split())
    # Read the votes
    votes = list(map(int, input().split()))
    # Initialize the VoteCounter
    vote_counter = VoteCounter(N)
    # Process each vote and print the current winner
    for vote in votes:
        try:
            vote_counter.add_vote(vote)
            current_winner = vote_counter.get_current_winner()
            print(f"Current Winner: Candidate {current_winner}")  # Ensure output format matches requirement
        except ValueError as e:
            print(e)
if __name__ == "__main__":
    main()