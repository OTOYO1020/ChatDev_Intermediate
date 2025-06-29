'''
Main application file to run the path counting application.
'''
from graph import Graph
from typing import List, Tuple
def count_paths(N: int, M: int, roads: List[Tuple[int, int]]) -> int:
    graph = Graph(N)
    for u, v in roads:
        graph.add_road(u, v)
    return graph.count_paths(1, N)
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])
    M = int(input_data[1])
    roads = [tuple(map(int, line.split())) for line in input_data[2:M+2]] if M > 0 else []
    result = count_paths(N, M, roads)
    print(result)