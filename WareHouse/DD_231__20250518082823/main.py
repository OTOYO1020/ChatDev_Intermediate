'''
Main application file for the arrangement checker.
'''
import sys
from graph import canArrangePeople
def main():
    try:
        N = int(input("Enter number of people (N): "))
        if N < 1:
            print("Input Error: The number of people (N) must be at least 1.")
            return
        M = int(input("Enter number of conditions (M): "))
        conditions = []
        conditions_set = set()  # Use a set to track unique conditions
        if M == 0:
            print("No conditions to satisfy. Any arrangement is valid.")
        elif M > 0:
            print("Enter conditions as pairs (e.g., '1 2, 2 3'):")
            conditions_input = input().strip().split(',')
            for cond in conditions_input:
                try:
                    a, b = map(int, cond.strip().split())
                    if a != b and (a, b) not in conditions_set:  # Ensure no duplicates and no self-loops
                        if 1 <= a <= N and 1 <= b <= N:  # Validate range
                            conditions.append((a, b))
                            conditions_set.add((a, b))  # Add to the set
                        else:
                            print(f"Input Error: Condition pairs must be between 1 and {N}. Invalid pair: ({a}, {b})")
                            return
                except ValueError:
                    print(f"Input Error: Invalid condition format for '{cond}'. Please enter pairs of integers.")
                    return
        result = canArrangePeople(N, M, conditions)
        print("A valid arrangement is possible." if result else "No valid arrangement is possible.")
    except ValueError:
        print("Input Error: Please enter valid integers for N and M.")
if __name__ == "__main__":
    main()