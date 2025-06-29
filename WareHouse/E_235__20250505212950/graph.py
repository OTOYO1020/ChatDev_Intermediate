'''
Graph class to represent a graph and compute its minimum spanning tree.
'''
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []
        self.mst_edges = set()  # Store MST edges for quick lookup
    def add_edge(self, a, b, weight):
        # Adjusting for 1-based index input
        self.edges.append((weight, a - 1, b - 1))
    def find_mst(self):
        if len(self.edges) < self.V - 1:
            print("Not enough edges to form a valid MST.")
            return False, []  # Indicate that the MST cannot be formed
        parent = list(range(self.V))
        self.edges.sort()
        mst_edges = []
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for weight, a, b in self.edges:
            root_a = find(a)
            root_b = find(b)
            if root_a != root_b:
                parent[root_a] = root_b
                mst_edges.append((a + 1, b + 1, weight))  # Store as 1-based index
        # Check if we have a valid MST (all vertices must be connected)
        if len(mst_edges) != self.V - 1:
            print("Graph is disconnected, MST cannot be formed.")
            return False, []  # Indicate that the MST is not valid
        self.mst_edges = set(mst_edges)  # Store MST edges as a set for quick lookup
        return True, mst_edges  # Indicate that the MST is valid and return the edges
    def is_edge_in_mst(self, edge, mst_edges):
        if not mst_edges:  # Check if MST is valid
            return False
        return (edge[0] - 1, edge[1] - 1, edge[2]) in mst_edges or (edge[1] - 1, edge[0] - 1, edge[2]) in mst_edges