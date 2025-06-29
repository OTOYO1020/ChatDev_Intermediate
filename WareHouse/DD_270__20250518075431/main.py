'''
Main application file for the Stone Game.
'''
from typing import List
from game_logic import max_stones_removed
def main():
    '''
    Main function to handle input and output for the Stone Game.
    '''
    try:
        # Read input values
        N = int(input("Enter number of stones (N): "))
        K = int(input("Enter number of options (K): "))
        A_input = list(map(int, input("Enter unique options (space-separated): ").split()))
        # Check for unique values
        if len(A_input) != len(set(A_input)):
            raise ValueError("All options must be unique.")
        A = sorted(set(A_input))  # Ensure sorted and unique
        if N <= 0 or K <= 0:
            raise ValueError("N and K must be positive integers.")
        if len(A) != K:
            raise ValueError("The number of unique options does not match K.")
        if K == 0:  # Check if there are no options
            print("Max stones removed by Takahashi: 0")
            return
        # Calculate the maximum stones removed by Takahashi
        result = max_stones_removed(N, K, A)
        print(f"Max stones removed by Takahashi: {result}")
    except ValueError as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()