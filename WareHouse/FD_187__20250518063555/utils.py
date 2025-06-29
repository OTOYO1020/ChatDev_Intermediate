'''
Utility functions for input parsing and edge subset generation.
'''
from itertools import combinations
def generate_edge_subsets(edges):
    subsets = []
    for r in range(len(edges) + 1):
        subsets.extend(combinations(edges, r))
    return subsets