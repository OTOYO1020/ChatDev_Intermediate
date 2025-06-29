'''
Union-Find data structure for managing connected components.
'''
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.parity = [0] * size  # To store parity information
    def find(self, x):
        if self.parent[x] != x:
            original_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.parity[x] ^= self.parity[original_parent]  # Update parity
        return self.parent[x]
    def union(self, x, y, parity):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.parity[root_y] = self.parity[x] ^ self.parity[y] ^ parity
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.parity[root_x] = self.parity[x] ^ self.parity[y] ^ parity
            else:
                self.parent[root_y] = root_x
                self.parity[root_y] = self.parity[x] ^ self.parity[y] ^ parity
                self.rank[root_x] += 1