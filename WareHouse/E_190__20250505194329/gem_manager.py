'''
Module to define the GemManager class for managing gem logic.
'''
from gem_graph import GemGraph
class GemManager:
    def __init__(self, graph):
        self.graph = graph
    def is_possible_and_minimum_gems(self, required_gems):
        # Check if all required gems are present in the graph
        for gem in required_gems:
            if gem not in self.graph.adjacency_list:
                return (False, None)  # Return immediately if any required gem is missing
        components = self.graph.get_connected_components()
        min_gems = float('inf')  # Initialize to infinity
        found = False
        # Check each component for required gems
        for component in components:
            if all(gem in component for gem in required_gems):
                found = True
                min_gems = min(min_gems, len(component))  # Update minimum if this component is valid
        if found:
            return (True, min_gems)  # Return the minimum size of a valid component
        return (False, None)