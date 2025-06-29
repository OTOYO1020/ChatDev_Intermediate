'''
Main application file for the voting calculation.
'''
def main():
    # Read integers N and M from standard input
    N, M = map(int, input().split())
    # Check if N is less than M
    if N < M:
        print("No")
        return
    # Read the array A of length N, which contains the votes
    votes = list(map(int, input().split()))
    # Validate that the number of votes matches N
    if len(votes) != N:
        print("No")
        return
    # Handle the case when M is zero to allow for selection of zero items
    if M == 0:
        print("Yes")
        return
    # Calculate the total number of votes
    total_votes = sum(votes)
    # Handle the case when total_votes is zero to avoid division by zero
    if total_votes == 0:
        print("No")
        return
    # Determine the minimum threshold for selection
    threshold = total_votes / (4 * M)
    # Initialize a counter for selected items
    selected_count = sum(1 for vote in votes if vote >= threshold)
    # Check if selected_count meets the criteria
    if selected_count >= M:
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()