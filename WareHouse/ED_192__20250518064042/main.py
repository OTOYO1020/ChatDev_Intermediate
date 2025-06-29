'''
Main entry point of the railroad scheduling application.
'''
from railroad_graph import RailroadGraph
from typing import List, Tuple, Union
def earliest_arrival_time(N: int, M: int, X: int, Y: int, railroads: List[Tuple[int, int, int, int]]) -> Union[int, str]:
    graph = RailroadGraph(N, M, railroads)
    return graph.earliest_arrival_time(X, Y)
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    N = int(input_data[0])
    M = int(input_data[1])
    X = int(input_data[2])
    Y = int(input_data[3])
    railroads = []
    for i in range(4, 4 + M):
        try:
            # Strip whitespace and split by comma
            parts = input_data[i].strip().split(',')
            if len(parts) != 4:
                raise ValueError(f"Invalid railroad entry at line {i + 1}. Expected format: A,B,K,T")
            A, B, K, T = map(int, parts)
            railroads.append((A, B, K, T))
        except ValueError:
            raise ValueError(f"Invalid railroad entry at line {i + 1}. Ensure format is A,B,K,T with integers.")
    result = earliest_arrival_time(N, M, X, Y, railroads)
    print(result)