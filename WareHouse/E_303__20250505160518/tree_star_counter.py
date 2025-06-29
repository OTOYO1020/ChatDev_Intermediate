'''
Module for counting level-k stars in a tree.
'''
class TreeStarCounter:
    '''
    Class to represent a tree and count level-k stars.
    '''
    def __init__(self, n):
        self.n = n
        self.adjacency_list = {i: [] for i in range(1, n + 1)}
        self.degree = {i: 0 for i in range(1, n + 1)}
    def add_edge(self, u, v):
        '''
        Adds an edge to the tree and updates the degree of vertices.
        '''
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
        self.degree[u] += 1
        self.degree[v] += 1
    def count_stars(self):
        '''
        Counts the number of level-k stars in the tree.
        '''
        star_count = 0
        for vertex in range(1, self.n + 1):
            if self.degree[vertex] == 1:  # Leaf node
                connected_vertex = self.adjacency_list[vertex][0]  # Get the connected vertex
                if self.degree[connected_vertex] >= 2:
                    star_count += 1  # Increment star count for each valid leaf connection
        return star_count