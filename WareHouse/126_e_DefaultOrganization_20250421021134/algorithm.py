'''
Algorithm class to encapsulate the main logic for cost calculation.
'''
from union_find import UnionFind
class Algorithm:
    def __init__(self, n, m, constraints):
        self.n = n
        self.m = m
        self.constraints = constraints
        self.uf = UnionFind(n)
    def calculate_min_cost(self):
        for x, y, z in self.constraints:
            self.uf.union(x, y, z % 2)
        # Count connected components
        component_count = len(set(self.uf.find(i) for i in range(self.n)))
        return component_count