'''
Main application file for the Vote Counter.
'''
from vote_processor import find_most_voted_strings
from typing import List
def main():
    try:
        N = int(input("Enter number of votes (must be a positive integer): "))
        if N <= 0:
            raise ValueError("Number of votes must be greater than zero.")
        votes_input = input(f"Enter exactly {N} votes (comma separated, no leading/trailing spaces): ").strip()
        votes = [vote.strip() for vote in votes_input.split(',') if vote.strip()]  # Ensure no empty votes
        # Check for valid input
        if len(votes) != N:
            print(f"Please enter exactly {N} votes. You entered {len(votes)} votes.")
            return  # Exit if invalid input
        results = find_most_voted_strings(N, votes)
        print("Most Voted Strings:")
        for result in results:
            print(result)
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()