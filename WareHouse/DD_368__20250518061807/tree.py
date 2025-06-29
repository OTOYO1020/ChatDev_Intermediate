'''
Tree class to handle the logic for finding the minimum vertices in a tree.
'''
from collections import defaultdict
from typing import List, Tuple
class Tree:
    def __init__(self, N: int, edges: List[Tuple[int, int]]):
        self.N = N
        self.edges = edges
        self.adj_list = defaultdict(list)
        self.build_tree()
    def build_tree(self):
        # Build the adjacency list representation of the tree
        for u, v in self.edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
    def min_vertices_in_tree(self, K: int, specified_vertices: List[int]) -> int:
        # Handle edge case where K equals 1
        if K == 1:
            return 1
        specified_set = set(specified_vertices)
        visited = set()
        subtree_vertices = 0
        def dfs(node):
            nonlocal subtree_vertices
            visited.add(node)
            is_specified = node in specified_set
            count = 1 if is_specified else 0
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    count += dfs(neighbor)
            # If this node is specified, we count it towards the subtree
            if is_specified:
                subtree_vertices += 1
            return count
        # Start DFS from one of the specified vertices
        dfs(specified_vertices[0])
        # Check if we found all specified vertices
        if len(visited.intersection(specified_set)) < K:
            return -1  # Not all specified vertices are connected
        return subtree_vertices  # Return the number of vertices in the subtree