'''
Main entry point for the pathfinding application.
'''
from app import min_path_weight
import sys
from typing import List, Tuple
def parse_input() -> Tuple[int, int, List[Tuple[int, int, int]], int, List[int], List[int]]:
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])  # Number of vertices
    M = int(input_data[1])  # Number of edges
    edges = [tuple(map(int, line.split())) for line in input_data[2:M+2]]  # List of edges with weights
    K = int(input_data[M+2])  # Length of sequences
    A = list(map(int, input_data[M+3].split()))  # Sequence A
    B = list(map(int, input_data[M+4].split()))  # Sequence B
    return N, M, edges, K, A, B
if __name__ == "__main__":
    try:
        N, M, edges, K, A, B = parse_input()
        result = min_path_weight(N, M, edges, K, A, B)
        print(result)
    except Exception as e:
        print(f"Error: {e}")