'''
Main application file for the CLI to calculate the sum of f(S_i, S_j).
'''
import sys
from calculations import calculate_f, sum_of_f
def main():
    try:
        N = int(input("Enter number of sets (N): "))
        M = int(input("Enter the number of elements in each set (M): "))  # New input for M
        sets_input = input("Enter sets (comma-separated integers, separated by semicolons, e.g., '1,2,3;4,5,6'): ").strip().split(';')
        # Validate and create sets
        sets = []
        for s in sets_input:
            elements = list(map(str.strip, s.split(',')))  # Strip whitespace
            if len(elements) != len(set(elements)):
                raise ValueError(f"Set '{s}' contains duplicate elements.")
            if len(elements) != M:  # Check if the set size matches M
                raise ValueError(f"Set '{s}' does not contain exactly {M} elements.")
            try:
                sets.append(set(map(int, elements)))  # Convert to integers and create a set
            except ValueError:
                raise ValueError(f"Set '{s}' contains non-integer elements.")
        if len(sets) != N:
            raise ValueError("Number of sets does not match N.")
        result = sum_of_f(N, sets)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
if __name__ == "__main__":
    main()