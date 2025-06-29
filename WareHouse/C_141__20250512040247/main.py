'''
Main application file for the Survivor Game.
'''
from typing import List
from logic import determine_survivors
def main():
    input_data = input("Enter N, K, Q and answers (comma-separated): ")
    try:
        parts = input_data.split(',')
        N = int(parts[0].strip())
        K = int(parts[1].strip())
        Q = int(parts[2].strip())
        A = list(map(int, parts[3:]))  # Collect all remaining parts as answers
        # Validate the number of answers
        if len(A) != Q:
            raise ValueError(f"Expected {Q} answers, but got {len(A)}. Please provide the correct number of answers.")
        # Validate that all answers are within the valid range
        if any(answer < 0 or answer >= N for answer in A):
            raise ValueError("All answers must be valid indices between 0 and N-1.")
        survivors = determine_survivors(N, K, Q, A)
        display_results(survivors)
    except Exception as e:
        print(f"Error: {str(e)}")
def display_results(survivors: List[int]):
    if survivors:
        print("Survivors: " + ', '.join(map(str, survivors)))
    else:
        print("No survivors.")
if __name__ == "__main__":
    main()