'''
Main application file for the grid reachability program using BFS.
'''
from bfs import canReach
def main():
    try:
        n = int(input("Enter grid size (N): "))
        m = int(input("Enter distance squared (M): "))
        # Input validation
        if n <= 0:
            print("Grid size (N) must be a positive integer.")
            return
        if m < 0:
            print("Distance squared (M) must be a non-negative integer.")
            return
        results = canReach(n, m)
        display_results(results)
    except ValueError:
        print("Please enter valid integers for N and M.")
def display_results(results):
    for i, j, reachable, min_operations in results:
        print(f"({i}, {j}): Reachable: {reachable}, Min Operations: {min_operations}")
if __name__ == "__main__":
    main()