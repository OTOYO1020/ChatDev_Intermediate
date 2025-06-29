'''
Main application file for the minimum time calculation without GUI.
'''
from min_time import min_time_to_stage_n
def main():
    try:
        N = int(input("Enter N: "))
        if N < 1:
            raise ValueError("N must be at least 1.")
        A = list(map(int, input("Enter A (comma-separated): ").split(','))) if N > 1 else []
        B = list(map(int, input("Enter B (comma-separated): ").split(','))) if N > 1 else []
        X = list(map(int, input("Enter X (comma-separated): ").split(','))) if N > 1 else []
        # Ensure all lists have the correct length
        if len(A) != N - 1 or len(B) != N - 1 or len(X) != N - 1:
            raise ValueError(f"Invalid input: Lists A, B, and X must each have exactly {N-1} elements.")
        # Ensure all values in A, B, and X are non-negative
        if any(a < 0 for a in A) or any(b < 0 for b in B) or any(x < 1 or x > N for x in X):
            raise ValueError("Invalid input: All elements in A, B must be non-negative and elements in X must be positive integers within the range of stages.")
        min_time = min_time_to_stage_n(N, A, B, X)
        print(f"Minimum time to reach stage {N}: {min_time} seconds")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
if __name__ == "__main__":
    main()