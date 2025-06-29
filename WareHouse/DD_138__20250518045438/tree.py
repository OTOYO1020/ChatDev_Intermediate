'''
Tree class to manage the tree structure and perform operations on it.
'''
from typing import List, Tuple
class Tree:
    def __init__(self, N: int, edges: List[Tuple[int, int]]):
        self.N = N
        self.edges = edges
        self.adj_list = [[] for _ in range(N + 1)]
        self.counters = [0] * (N + 1)
        self.lazy = [0] * (N + 1)  # Lazy array for increments
        self.subtree = [[] for _ in range(N + 1)]
        self.build_tree()
        self.dfs(1, -1)  # Start DFS from node 1 with no parent
    def build_tree(self):
        seen_edges = set()  # To track added edges
        if len(self.edges) != self.N - 1:
            raise ValueError("The number of edges must be exactly N-1 for a valid tree.")
        for u, v in self.edges:
            if u != v and (u, v) not in seen_edges and (v, u) not in seen_edges:
                self.adj_list[u].append(v)
                self.adj_list[v].append(u)
                seen_edges.add((u, v))
        # Check connectivity
        visited = [False] * (self.N + 1)
        def dfs_check(node: int):
            visited[node] = True
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    dfs_check(neighbor)
        dfs_check(1)  # Start DFS from node 1
        if not all(visited[1:]):  # Check if all nodes are visited
            raise ValueError("The tree is not connected; some nodes are unreachable.")
    def dfs(self, node: int, parent: int):
        # Initialize the current node's subtree
        self.subtree[node] = [node]  # Start with the current node
        for neighbor in self.adj_list[node]:
            if neighbor != parent:
                self.dfs(neighbor, node)
                self.subtree[node].extend(self.subtree[neighbor])  # Append the child's subtree
    def increment_counters(self, p: int, x: int):
        # Update the lazy array instead of the counters directly
        if 1 <= p <= self.N:  # Ensure the node exists
            self.lazy[p] += x
    def apply_lazy(self):
        # Apply the lazy increments to the counters for all nodes
        def dfs_apply(node: int, parent: int):
            self.counters[node] += self.lazy[node]  # Apply lazy value to current node's counter
            for neighbor in self.adj_list[node]:
                if neighbor != parent:
                    # Propagate the lazy value to the child
                    self.lazy[neighbor] += self.lazy[node]
                    dfs_apply(neighbor, node)
            # Reset the lazy value for the current node after all children have been processed
            self.lazy[node] = 0
        dfs_apply(1, -1)  # Start DFS from node 1 with no parent
    def get_final_counters(self) -> List[int]:
        # Return final counters after applying lazy propagation
        return self.counters[1:]  # Exclude the 0th index