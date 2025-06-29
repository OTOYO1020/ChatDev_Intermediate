'''
Main entry point for the happiness calculation application.
'''
import sys
from graph import Graph
from happiness import calculate_happiness, find_max_happiness
def main():
    try:
        N = int(input("Enter number of spaces (N): "))
        M = int(input("Enter number of slopes (M): "))
        H = list(map(int, input("Enter altitudes (space-separated): ").split()))
        # Input validation for altitudes
        if len(H) != N:
            raise ValueError("Number of altitudes must match N.")
        for altitude in H:
            if not isinstance(altitude, int):
                raise ValueError("All altitudes must be integers.")
        slopes_input = input("Enter slopes (U V space-separated, pairs of integers): ").strip().split()
        # Input validation for slopes
        if len(slopes_input) % 2 != 0:
            raise ValueError("Slopes input must contain an even number of integers.")
        if len(slopes_input) // 2 != M:
            raise ValueError(f"Expected {M} pairs of slopes, but got {len(slopes_input) // 2}.")
        slopes_set = set()  # To keep track of unique slopes
        slopes = []
        for i in range(0, len(slopes_input), 2):
            try:
                u = int(slopes_input[i])
                v = int(slopes_input[i + 1])
                if u < 1 or u > N or v < 1 or v > N:
                    raise ValueError(f"Slope ({u}, {v}) must be between 1 and {N}.")
                if u == v:
                    raise ValueError(f"Slope cannot connect space {u} to itself.")
                if (u, v) in slopes_set or (v, u) in slopes_set:
                    raise ValueError(f"Slope ({u}, {v}) is a duplicate.")
                slopes_set.add((u, v))  # Add the slope to the set for uniqueness
                slopes.append((u, v))
            except ValueError:
                raise ValueError(f"Invalid slope input: ({slopes_input[i]}, {slopes_input[i + 1]}). Both must be integers.")
        graph = Graph(N)
        for u, v in slopes:
            graph.add_slope(u, v)
        max_happiness = find_max_happiness(graph, H)
        print(f"Maximum Happiness: {max_happiness}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()