'''
Main entry point for the Graph Painter application.
'''
import sys
from typing import List, Tuple
from graph import Graph
from utils import validate_input
def count_painting_ways(N: int, M: int, K: int, edges: List[Tuple[int, int]]) -> int:
    if not validate_input(N, M, K, edges):
        return 0  # Return 0 for invalid input
    graph = Graph(N, edges)
    return graph.count_valid_painting_ways(K)
if __name__ == "__main__":
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])
    M = int(input_data[1])
    K = int(input_data[2])
    edges = [tuple(map(int, line.split())) for line in input_data[3:M + 3]]
    result = count_painting_ways(N, M, K, edges)
    print(result)