'''
This module defines the Graph class to represent a graph and perform BFS.
'''
from collections import deque, defaultdict
import sys
class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adj_list = defaultdict(list)
        for u, v in edges:
            self.add_edge(u, v)
        self.transformed_graph = self.transform()
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def transform(self):
        '''
        Transforms the graph into a three-layer structure where each vertex
        is expanded into three states based on modulo 3. It allows transitions
        between the same state and the next state based on the original edges.
        '''
        transformed = defaultdict(list)
        for u in self.adj_list:
            for state in range(3):
                for v in self.adj_list[u]:
                    transformed[(u, state)].append((v, state))  # Same state transition
                    transformed[(u, state)].append((v, (state + 1) % 3))  # Next state transition
        return transformed
    def bfs(self, start, target):
        '''
        Performs a breadth-first search (BFS) on the transformed graph to find
        the shortest path from the start node to the target node.
        '''
        queue = deque([(start, 0)])
        visited = set()
        visited.add((start, 0))
        distance = 0
        while queue:
            for _ in range(len(queue)):
                current, state = queue.popleft()
                if current == target and state == 0:
                    return distance // 3
                if (current, state) in self.transformed_graph:  # Check if the key exists
                    for neighbor in self.transformed_graph[(current, state)]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            distance += 1
        return -1
def main():
    input_data = sys.stdin.read().strip().splitlines()
    N, M = map(int, input_data[0].split())
    edges = [tuple(map(int, line.split())) for line in input_data[1:M+1]]
    S, T = map(int, input_data[M+1].split())
    graph = Graph(N, edges)
    result = graph.bfs(S, T)
    print(result)
if __name__ == "__main__":
    main()