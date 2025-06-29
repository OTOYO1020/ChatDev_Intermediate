'''
Main entry point for the command-line application.
'''
from calculations import calculate_f
from typing import List
def main():
    try:
        N = int(input("Enter the number of elements in sequences A and T: "))
        A = list(map(int, input("Enter values for A (space-separated): ").split()))
        T = list(map(int, input("Enter values for T (space-separated): ").split()))
        X = list(map(int, input("Enter values for X (space-separated): ").split()))
        # Validate input lengths
        if len(A) != N:
            print(f"Error: Sequence A must contain exactly {N} elements. You entered {len(A)} elements.")
            return
        if len(T) != N:
            print(f"Error: Sequence T must contain exactly {N} elements. You entered {len(T)} elements.")
            return
        if len(X) == 0:
            print("Error: The sequence X must contain at least one element.")
            return
    except ValueError as e:
        print(f"Error: {e}. Please ensure you enter valid integers.")
        return
    # Calculate results
    results = calculate_f(N, A, T, X)
    # Output results
    for result in results:
        print(result)
if __name__ == "__main__":
    main()