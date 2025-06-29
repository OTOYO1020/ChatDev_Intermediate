'''
Main application file for the Vote Counter application.
This program reads the number of voters and their votes for candidates,
then determines and outputs the candidate with the most votes.
'''
def main():
    # Read the number of voters and ensure it is a positive integer
    while True:
        try:
            N = int(input())
            if N <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    vote_count = {}
    # Loop to read each candidate's name and count votes
    for _ in range(N):
        candidate_name = input().strip()  # Strip whitespace
        while not candidate_name:  # Check for empty string
            print("Candidate name cannot be empty. Please enter a valid name.")
            candidate_name = input().strip()
        vote_count[candidate_name] = vote_count.get(candidate_name, 0) + 1
    # Determine the winner based on the vote count
    winner = determine_winner(vote_count)
    # Output the winner's name
    print(winner)  # This will now print only the single winner's name
def determine_winner(vote_count):
    """
    Determines the candidate with the highest number of votes.
    Parameters:
    vote_count (dict): A dictionary containing candidate names as keys and their vote counts as values.
    Returns:
    str: The name of the candidate with the most votes. In case of a tie, the first candidate in alphabetical order is returned.
    """
    max_votes = -1
    winners = []  # List to hold candidates with the maximum votes
    for candidate, votes in vote_count.items():
        if votes > max_votes:
            max_votes = votes
            winners = [candidate]  # Start a new list with the current candidate
        elif votes == max_votes:
            winners.append(candidate)  # Add candidate to the list of winners
    if len(winners) > 1:
        print("There is a tie between candidates:", ", ".join(winners))
    return sorted(winners)[0]  # Return the first candidate in alphabetical order in case of a tie
if __name__ == "__main__":
    main()