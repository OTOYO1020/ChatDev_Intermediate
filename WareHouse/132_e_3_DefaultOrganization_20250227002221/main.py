'''
Main entry point for the BFS shortest path application.
'''
from collections import deque, defaultdict
import sys
class Graph:
    def __init__(self, N):
        self.N = N
        self.edges = defaultdict(list)
    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)
    def transform_graph(self):
        transformed_edges = defaultdict(list)
        for u in self.edges:
            for v in self.edges[u]:
                for i in range(3):
                    transformed_edges[(u, i)].append((v, (i + 1) % 3))
                    transformed_edges[(v, i)].append((u, (i + 1) % 3))
        return transformed_edges
    def bfs(self, S, T):
        transformed_edges = self.transform_graph()
        queue = deque([(S, 0)])
        visited = set()
        visited.add((S, 0))
        distance = 0
        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if current_node == (T, 0):
                    return distance // 3
                for neighbor in transformed_edges[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return -1
def main():
    # Read input from standard input
    input_data = sys.stdin.read().strip().splitlines()
    N, M = map(int, input_data[0].split())
    edges = [tuple(map(int, line.split())) for line in input_data[1:M + 1]]
    S, T = map(int, input_data[M + 1].split())
    graph = Graph(N)
    for u, v in edges:
        graph.add_edge(u, v)
    result = graph.bfs(S, T)
    print(result)
if __name__ == "__main__":
    main()