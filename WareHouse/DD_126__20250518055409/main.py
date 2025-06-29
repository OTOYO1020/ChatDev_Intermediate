'''
Main entry point of the Tree Coloring application.
'''
from tree_coloring import color_tree
from input_validation import InputValidation
import sys
from typing import List, Tuple
def main():
    input_data = sys.stdin.read().strip().splitlines()
    try:
        N = int(input_data[0])
        if N < 1:
            print("The number of vertices must be a positive integer.")
            return
    except ValueError:
        print("The first line must be an integer representing the number of vertices.")
        return
    edges = []
    for line in input_data[1:]:
        parts = line.split(',')
        if len(parts) != 3:
            print("Each edge must be in the format 'u,v,w'")
            return
        try:
            u, v, w = map(int, parts)
            edges.append((u, v, w))
        except ValueError:
            print("Edge values must be integers.")
            return
    # Validate edges using InputValidation class
    if not InputValidation.validate_edges(N, edges) or not InputValidation.is_connected(N, edges):
        print("Invalid edges provided. Please ensure that the edges are in the correct format and that the number of edges is N - 1, forming a connected graph.")
        return
    colors = color_tree(N, edges)
    print(' '.join(colors))
if __name__ == "__main__":
    main()