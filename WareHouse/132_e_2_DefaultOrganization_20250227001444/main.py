'''
Main application file that handles input and output for the graph BFS shortest path finder.
'''
from collections import deque, defaultdict
import sys
class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
    def add_edge(self, u, v):
        # Connect each state of vertex u to the corresponding state of vertex v
        for state in range(3):
            self.adjacency_list[(u, state)].append((v, (state + 1) % 3))
            self.adjacency_list[(v, state)].append((u, (state + 1) % 3))
    def bfs(self, start, target):
        start_node = (start, 0)
        target_node = (target, 0)
        queue = deque([start_node])
        visited = set([start_node])
        distance = 0
        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == target_node:
                    return distance  # Return the distance directly
                for neighbor in self.adjacency_list[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return -1  # Return -1 if no path is found
def main():
    input_data = sys.stdin.read().strip().splitlines()
    n, m = map(int, input_data[0].split())
    edges = [tuple(map(int, line.split())) for line in input_data[1:m+1]]
    start, target = map(int, input_data[m+1].split())
    graph = Graph()
    for u, v in edges:
        graph.add_edge(u, v)
    result = graph.bfs(start, target)
    if result != -1:
        print(result // 3)  # Divide the distance by 3 to get the minimum number of moves
    else:
        print(result)
if __name__ == "__main__":
    main()