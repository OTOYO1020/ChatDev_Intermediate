'''
Main application file to run the tree distance calculator without GUI.
'''
from tree import Tree
def main():
    n = int(input("Enter the number of vertices (N): "))
    edges = []
    print("Enter edges (A B) one per line (end with an empty line):")
    while True:
        edge_input = input()
        if edge_input == "":
            break
        edges.append(tuple(map(int, edge_input.split())))
    c = list(map(int, input("Enter sequence of C (space-separated): ").strip().split()))
    # Validate input for C
    if len(c) != n or any(x <= 0 for x in c):
        raise ValueError("Length of C must be equal to N and all values must be positive integers.")
    tree = Tree(n)
    for a, b in edges:
        tree.add_edge(a, b)
    # Calculate minimum distance sum
    min_value, min_vertex = tree.find_minimum_distance_sum(c)
    print(f"Minimum f(v): {min_value} at vertex {min_vertex}")
if __name__ == "__main__":
    main()