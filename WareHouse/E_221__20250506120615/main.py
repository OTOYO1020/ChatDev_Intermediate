'''
Main application file for the subsequence calculator.
This program reads an integer N representing the length of a sequence,
reads the sequence of integers A, and calculates the number of valid
subsequences that can be formed with elements of A.
'''
def calculate_subsequences(N, sequence):
    count = 0  # Initialize count to 0
    sorted_A = sorted(sequence)
    dp = [0] * N  # Dynamic programming array to store counts of subsequences ending at each element
    dp[0] = 1  # Initialize dp[0] to 1 for the first element
    for k in range(1, N):  # Start from the second element
        A_k = sorted_A[k]
        valid_count = binary_search(sorted_A, A_k)  # Use binary search to find count of valid A_1 elements
        dp[k] = (dp[k-1] + valid_count) % 998244353  # Update dp[k] with the count of valid subsequences
        count = (count + dp[k]) % 998244353  # Increment count by the number of valid subsequences
    return count  # Return the count instead of using a global variable
if __name__ == "__main__":
    import sys
    from utils import binary_search
    N = int(sys.stdin.readline().strip())
    sequence = list(map(int, sys.stdin.readline().strip().split()))
    if len(sequence) != N:
        raise ValueError("The number of elements does not match N.")
    count = calculate_subsequences(N, sequence)  # Capture the returned count
    print(count)  # Print the final value of count