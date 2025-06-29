'''
Main entry point for the shortest distance calculator application.
'''
from graph import Graph, ShortestDistanceCalculator
from typing import List, Tuple
def shortest_distance_excluding_edge(N: int, M: int, edges: List[Tuple[int, int]]) -> List[int]:
    graph = Graph(N)
    for u, v in edges:
        graph.add_edge(u, v)
    calculator = ShortestDistanceCalculator(graph, edges)  # Pass edges to the calculator
    return calculator.calculate_shortest_distances()
def main():
    # Example input for testing
    N = 5  # Number of vertices
    M = 6  # Number of edges
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (2, 5)]  # List of directed edges
    results = shortest_distance_excluding_edge(N, M, edges)
    print(results)
if __name__ == "__main__":
    main()