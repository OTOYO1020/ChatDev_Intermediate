'''
Main application file for the Star Tree Checker.
'''
import sys
from star_tree import is_star_tree
def main():
    '''
    Main function to read input for the star tree checker and output the result.
    It reads the number of vertices and the edges, then checks if the tree is a star tree.
    '''
    try:
        N = int(input("Enter the number of vertices (N): "))
        if N < 2:
            print("Error: A tree must have at least 2 vertices.")
            return
        edges = []
        edge_set = set()  # To track unique edges
        print(f"Please enter {N-1} edges (format: a b) separated by new lines:")
        while len(edges) < N - 1:
            edge_input = input()
            try:
                a, b = map(int, edge_input.split())
            except ValueError:
                print("Error: Please enter the edge in the correct format (two integers separated by a space).")
                continue
            if a < 1 or a > N or b < 1 or b > N:
                print(f"Error: Vertices must be in the range 1 to {N}.")
                continue
            if a == b:
                print(f"Error: An edge cannot connect a vertex to itself (e.g., (1, 1)).")
                continue
            if (a, b) in edge_set or (b, a) in edge_set:  # Check for duplicate edges
                print(f"Error: Edge ({a}, {b}) is a duplicate.")
                continue
            edge_set.add((a, b))  # Add edge to the set
            edges.append((a, b))
        # Validate the number of edges
        if len(edges) != N - 1:
            print(f"Error: You must enter exactly {N-1} edges. You entered {len(edges)} edges.")
            return
        # Initialize degree array
        degree = [0] * (N + 1)
        for a, b in edges:
            degree[a] += 1
            degree[b] += 1
        # Directly check if the tree is a star
        result = is_star_tree(degree)
        print(result)
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()