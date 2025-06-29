'''
Input parser that extracts graph and query details from the input string.
'''
from typing import List, Tuple
def parse_input(input_data: str) -> Tuple[int, int, List[Tuple[int, int]], int, List[Tuple[int, int]]]:
    lines = input_data.strip().split('\n')
    N, M = map(int, lines[0].split())
    # Validate number of edges
    if M > (3 * N) // 2:
        raise ValueError("Number of edges exceeds the maximum allowed for the given number of vertices.")
    edges = [tuple(map(int, line.split())) for line in lines[1:M + 1]]
    # Validate the number of edges provided
    if len(edges) != M:
        raise ValueError("The number of edges provided does not match the specified number of edges.")
    Q = int(lines[M + 1])
    queries = [tuple(map(int, line.split())) for line in lines[M + 2:M + 2 + Q]]
    return N, M, edges, Q, queries