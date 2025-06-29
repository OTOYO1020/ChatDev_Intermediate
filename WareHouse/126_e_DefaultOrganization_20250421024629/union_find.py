'''
Union-Find data structure implementation for managing connected components.
'''
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.parity = [0] * size
    def find(self, x):
        if self.parent[x] != x:
            original_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.parity[x] ^= self.parity[original_parent]
        return self.parent[x]
    def union(self, x, y, parity):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # Calculate the new parity for the root of the merged component
            new_parity = self.parity[x] ^ self.parity[y] ^ parity  # Use current parities of x and y
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.parity[root_y] = self.parity[x] ^ new_parity  # Correct parity assignment
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.parity[root_x] = self.parity[y] ^ new_parity  # Correct parity assignment
            else:
                self.parent[root_y] = root_x
                self.parity[root_y] = self.parity[x] ^ new_parity  # Correct parity assignment
                self.rank[root_x] += 1
    def get_min_cost(self):
        components = set()
        for i in range(len(self.parent)):
            components.add(self.find(i))
        return len(components)