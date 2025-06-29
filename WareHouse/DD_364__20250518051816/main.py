'''
Main application file for the Distance Calculator.
'''
from distance_calculator import find_kth_closest_distance
def main():
    # Input parsing with validation
    while True:
        try:
            N = int(input("Enter the number of points in A: "))
            A = list(map(int, input("Enter points A (comma-separated): ").split(',')))
            if len(A) != N:
                raise ValueError("The number of points in A does not match N.")
            if any(not isinstance(a, int) for a in A):
                raise ValueError("All points in A must be integers.")
            if any(a < 0 for a in A):  # Check for non-negative integers
                raise ValueError("All points in A must be non-negative integers.")
            break
        except ValueError as e:
            print(f"Invalid input for points A: {e}. Please enter integers only and try again.")
    while True:
        try:
            Q = int(input("Enter the number of points in B: "))
            B = list(map(int, input("Enter points B (comma-separated): ").split(',')))
            if len(B) != Q:
                raise ValueError("The number of points in B does not match Q.")
            if any(not isinstance(b, int) for b in B):
                raise ValueError("All points in B must be integers.")
            if any(b < 0 for b in B):  # Check for non-negative integers
                raise ValueError("All points in B must be non-negative integers.")
            break
        except ValueError as e:
            print(f"Invalid input for points B: {e}. Please enter integers only and try again.")
    while True:
        try:
            K = list(map(int, input("Enter K values (comma-separated): ").split(',')))
            if len(K) != Q:
                raise ValueError("The number of K values must match Q.")
            if any(k <= 0 for k in K):
                raise ValueError("All K values must be positive integers.")
            break
        except ValueError as e:
            print(f"Invalid input for K values: {e}. Please enter integers only and try again.")
    # Calculate results
    try:
        results = find_kth_closest_distance(N, Q, A, B, K)
        print(f"Results: {results}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()