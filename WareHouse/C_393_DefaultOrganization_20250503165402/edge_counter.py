'''
Utility class for counting edges to remove from a graph to make it simple.
This class provides a method to count the number of multi-edges in a list of edges.
'''
class EdgeCounter:
    def count_edges_to_remove(self, edges):
        edges_set = set()
        removal_count = 0
        for u, v in edges:
            edge = (min(u, v), max(u, v))  # Store edges in a consistent order
            if edge in edges_set:
                removal_count += 1  # Increment removal count for multi-edges
            else:
                edges_set.add(edge)  # Add the edge to the set if it's unique
        return removal_count