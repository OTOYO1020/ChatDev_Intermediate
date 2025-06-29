'''
Main application file for the Vote Counter application.
'''
from vote_counter import VoteCounter
def main():
    '''
    Main function to run the Vote Counter application.
    '''
    while True:
        try:
            N = int(input("Enter the number of voting papers (positive integer): "))  # Improved prompt
            if N < 1:
                print("Please enter a positive integer.")
                continue
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    vote_counter = VoteCounter()
    for _ in range(N):
        vote = input("Enter your vote (string, cannot be empty or whitespace): ")  # Improved prompt
        if not vote or vote.strip() == "":  # Check for empty or whitespace-only input
            print("Vote cannot be empty or whitespace. Please enter a valid vote.")
            continue
        vote_counter.add_vote(vote)
    most_voted = vote_counter.get_most_voted()
    if not most_voted:  # Check if there are no votes
        print("No votes have been cast yet.")
    else:
        for string in most_voted:
            print(string)
if __name__ == "__main__":
    main()