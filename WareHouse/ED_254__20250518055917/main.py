'''
Main entry point of the application that handles user interactions.
'''
from graph import Graph
from input_parser import parse_input
from typing import List, Tuple
def main():
    input_data = input("Enter graph details:\n")
    try:
        N, M, edges, Q, queries = parse_input(input_data)
        graph = Graph(N, edges)
        results = graph.sum_of_indices(Q, queries)
        print(f"Results: {results}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()