'''
Main application file to run the console application for calculating minimum cost.
'''
from logic import minimum_cost_to_determine_cards
from typing import List, Tuple
def main():
    # Read input values
    try:
        N = int(input("Enter the number of cards (N): "))
        M = int(input("Enter the number of conditions (M): "))
        if N <= 0 or M < 0:
            print("N must be greater than 0 and M must be non-negative.")
            return
    except ValueError:
        print("Invalid input. Please enter integers for N and M.")
        return
    conditions = []
    print("Enter conditions in the format 'X Y Z' (one per line). Type 'done' when finished:")
    while True:
        line = input()
        if line.lower() == 'done':
            break
        try:
            x, y, z = map(int, line.split())
            if x < 0 or x >= N or y < 0 or y >= N:
                print(f"Indices X and Y must be between 0 and {N-1}.")
                continue
            conditions.append((x, y, z))
        except ValueError:
            print("Invalid input. Please enter three integers separated by spaces.")
    # Check if conditions are provided
    if not conditions:
        print("No conditions provided. Please enter at least one condition.")
        return
    # Check for unique conditions against M
    if len(conditions) > M:
        print(f"Error: More conditions provided ({len(conditions)}) than allowed ({M}).")
        return
    # Calculate minimum cost
    result = minimum_cost_to_determine_cards(N, M, conditions)
    if result == -1:
        print("Conditions cannot be satisfied with the given inputs.")
    else:
        print(f"Minimum cost required: {result}")
if __name__ == "__main__":
    main()