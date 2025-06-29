'''
Main application file for the sum calculation application.
'''
from utils import sum_of_first_k  # Import the function from utils
def main():
    import sys
    # Read integers N, M, K from standard input
    N, M, K = map(int, sys.stdin.readline().strip().split())
    # Read the integer sequence A of length N from standard input
    A = list(map(int, sys.stdin.readline().strip().split()))
    # Initialize an empty list 'results' to store the sums for each valid i
    results = []
    # Loop through each index i from 1 to N - M + 1
    for i in range(1, N - M + 2):  # Adjusted to start from 1 and go to N - M + 1
        # Extract the subarray 'subarray = A[i-1:i-1 + M]' (using zero-based indexing)
        subarray = A[i-1:i-1 + M]
        # Sort the 'subarray' in ascending order
        subarray.sort()
        # Calculate the sum of the first K elements in the sorted 'subarray' and store it in 'results'
        result = sum_of_first_k(subarray, K)
        results.append(result)
    # Print each value in 'results' on a new line
    for result in results:
        print(result)
if __name__ == "__main__":
    main()