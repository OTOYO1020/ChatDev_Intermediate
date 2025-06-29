'''
Main application file for the Word Fit application.
'''
from word_fit import min_window_width
def main():
    try:
        N = int(input("Number of Words (N): "))
        M = int(input("Number of Lines (M): "))
        L = list(map(int, input("Widths of Words (comma-separated): ").split(',')))
        # Input validation
        if N <= 0 or M <= 0:
            raise ValueError("N and M must be positive integers.")
        if not L:  # Check if L is empty
            raise ValueError("The list of widths cannot be empty.")
        if any(width < 0 for width in L):
            raise ValueError("All widths must be non-negative integers.")
        if len(L) != N:
            raise ValueError("The number of widths must match N.")
        min_width = min_window_width(N, M, L)
        print(f"Minimum Width: {min_width}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()