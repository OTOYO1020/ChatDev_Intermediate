'''
Main application file for the minimum index difference calculator.
'''
from min_index_diff import find_minimum_index_difference
def main():
    try:
        N = int(input("Enter N (positive integer): "))
        K = int(input("Enter K (positive integer): "))
        if N <= 0 or K <= 0:
            raise ValueError("N and K must be positive integers.")
        if K > N:
            raise ValueError("K cannot be greater than N.")
        P = list(map(int, input("Enter permutation P (comma-separated): ").split(',')))
        if len(P) != N:
            raise ValueError("Length of permutation P must be equal to N.")
        if len(set(P)) != N or any(x < 1 or x > N for x in P):
            raise ValueError("Permutation P must contain unique integers from 1 to N.")
        min_diff = find_minimum_index_difference(N, K, P)
        if min_diff == -1:
            print("No valid good index sequences found.")
        else:
            print(f"Minimum Index Difference: {min_diff}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()