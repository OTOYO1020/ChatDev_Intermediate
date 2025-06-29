'''
Main application file that handles user interactions via standard input and output.
'''
from frustration_calculator import min_frustration
from typing import List, Tuple
def main():
    # Read number of people
    N = int(input("Enter number of people (N): "))
    # Read dislikes input
    dislikes_input = input("Enter dislikes (format: person1,person2,cost;...): ")
    dislikes = []
    for pair in dislikes_input.split(';'):
        if pair:
            parts = pair.split(',')
            if len(parts) == 3:
                person_a, person_b, cost = map(int, parts)
                dislikes.append((person_a, person_b, cost))  # Ensure this is a tuple of three elements
            else:
                print("Invalid dislike format. Each dislike must be in the format person1,person2,cost.")
                return
    # Validate input
    if len(dislikes) == 0:
        print("No dislikes provided. Please enter valid dislikes.")
        return
    # Calculate minimum frustration
    result = min_frustration(N, dislikes)
    print(f"Minimum Frustration: {result}")
if __name__ == "__main__":
    main()