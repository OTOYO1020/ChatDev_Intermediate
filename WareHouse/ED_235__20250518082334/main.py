'''
Main entry point for the MST Queries application.
'''
from app import minimum_spanning_tree_queries
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().splitlines()
    N, M = map(int, input_data[0].split())
    edges = [tuple(map(int, line.split())) for line in input_data[1:M+1]]
    Q = int(input_data[M+1])
    queries = [tuple(map(int, line.split())) for line in input_data[M+2:M+2+Q]]
    results = minimum_spanning_tree_queries(N, M, edges, Q, queries)
    for result in results:
        print(result)