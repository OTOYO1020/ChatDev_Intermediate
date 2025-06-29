'''
Main application file for the minimum distance calculator.
'''
from utils import is_consecutive
def calculate_min_distance(N, K, P):
    if K > N:
        print("Error: K cannot be greater than N. Please enter valid values.")
        return -1  # Return -1 to indicate an error
    if K == 1:
        return 0  # Any single index is valid
    min_distance = float('inf')
    for i_1 in range(1, N - K + 2):
        i_K = i_1 + K - 1
        subsequence = P[i_1 - 1:i_K]  # Convert to 0-based index
        if is_consecutive(subsequence, K):
            min_distance = min(min_distance, i_K - i_1)
    return min_distance if min_distance != float('inf') else -1  # Return -1 if no valid subsequence found
if __name__ == "__main__":
    try:
        N, K = map(int, input("Enter the total number of elements (N) and the length of the subsequence (K): ").split())
        P = list(map(int, input("Enter the permutation array (space-separated integers from 1 to N): ").split()))
        # Input validation to check if P is a valid permutation
        if sorted(P) != list(range(1, N + 1)):
            print("The permutation array must contain integers from 1 to N without duplicates.")
        else:
            result = calculate_min_distance(N, K, P)
            if result == -1:
                print("No valid consecutive subsequence found.")
            else:
                print(f"Minimum Distance: {result}")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid integers and a valid permutation array.")