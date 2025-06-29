'''
Main application file for the Friendship Candidate Counter.
'''
from friendship import count_friend_candidates
def main():
    '''
    Main function to handle user input and output for counting friend candidates.
    '''
    try:
        N = int(input("Enter number of users (N): "))
        friendships_input = input("Enter friendships (e.g., 1,2; 2,3): ")
        blockships_input = input("Enter blockships (e.g., 1,3; 2,4): ")
        # Parse friendships input and convert to set to remove duplicates
        friendships = set(tuple(map(int, pair.split(','))) for pair in friendships_input.split(';') if pair)
        # Parse blockships input and convert to set to remove duplicates
        blockships = set(tuple(map(int, pair.split(','))) for pair in blockships_input.split(';') if pair)
        result = count_friend_candidates(N, list(friendships), list(blockships))
        print(f"Friend Candidates: {result}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)} - Please ensure you enter valid integers.")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()