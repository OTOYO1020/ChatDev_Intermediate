'''
Graph class to represent the slopes between spaces using an adjacency list.
'''
class Graph:
    def __init__(self, num_spaces):
        self.num_spaces = num_spaces
        self.adjacency_list = [[] for _ in range(num_spaces + 1)]
    def add_slope(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)