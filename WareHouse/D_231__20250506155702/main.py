'''
Main application file for the adjacency condition checker.
'''
from graph_utils import can_line_up
def main():
    # Read number of people and adjacency conditions
    n, m = map(int, input("Enter number of people (N) and number of adjacency conditions (M): ").split())
    # Check if there are no people
    if n <= 0:
        print("NO")
        return
    # Initialize adjacency list
    adjacency_list = {i: set() for i in range(n)}  # Use a set to prevent duplicates
    print("Enter pairs (A, B) for adjacency conditions (0-indexed, one pair per line):")
    for _ in range(m):
        try:
            a, b = map(int, input().split())
            # Validate the input to ensure it falls within the range [0, N-1]
            if 0 <= a < n and 0 <= b < n:
                if a != b:  # Prevent self-loops
                    if b not in adjacency_list[a]:  # Check for duplicates before adding
                        adjacency_list[a].add(b)  # Add to set
                        adjacency_list[b].add(a)  # Add to set
                    else:
                        print(f"Duplicate input: ({a}, {b}) has already been entered.")
                else:
                    print(f"Invalid input: ({a}, {b}) cannot be a self-loop. Please enter different values.")
            else:
                print(f"Invalid input: ({a}, {b}) is out of range. Please enter values between 0 and {n-1}.")
        except ValueError:
            print("Invalid input: Please enter two integers separated by a space.")
    # Convert sets back to lists for compatibility with DFS
    adjacency_list = {k: list(v) for k, v in adjacency_list.items()}
    # Check if a valid arrangement exists
    if can_line_up(adjacency_list):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()