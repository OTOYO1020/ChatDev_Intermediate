'''
Main application file for the sequence combination checker.
'''
from utils import can_select_elements
def main():
    try:
        # Input sequences
        A = list(map(int, input("Enter sequence A (comma-separated): ").split(',')))
        B = list(map(int, input("Enter sequence B (comma-separated): ").split(',')))
        C = list(map(int, input("Enter sequence C (comma-separated): ").split(',')))
        X = list(map(int, input("Enter sequence X (comma-separated): ").split(',')))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return
    # Check combinations
    results = can_select_elements(A, B, C, X)
    # Output results
    for x, res in zip(X, results):
        print(f"{x}: {'Yes' if res else 'No'}")
if __name__ == "__main__":
    main()