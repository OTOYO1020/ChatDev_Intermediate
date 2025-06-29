'''
Main entry point for the coprime calculator application.
'''
from gcd_util import gcd
def calculate_coprimes(N, M, A):
    result = []
    # Loop through each integer k from 1 to M (inclusive)
    for k in range(1, M + 1):
        is_coprime = True
        # Loop through each integer A_i in A
        for A_i in A:
            # Check if gcd(A_i, k) is not equal to 1
            if gcd(A_i, k) != 1:
                is_coprime = False
                break
        # If 'is_coprime' remains True after checking all A_i, append k to 'result'
        if is_coprime:
            result.append(k)
    return result
def main():
    # Read integers N and M from standard input
    N, M = map(int, input("Enter N and M (space-separated): ").split())
    # Read the sequence of positive integers A
    A = list(map(int, input(f"Enter {N} positive integers for A (space-separated): ").split()))
    # Validate input length
    if len(A) != N:
        print(f"Expected {N} integers in A, but got {len(A)}.")
        return
    results = calculate_coprimes(N, M, A)
    # Print all integers in 'result' as the output
    print("Coprimes:", ', '.join(map(str, results)))
if __name__ == "__main__":
    main()