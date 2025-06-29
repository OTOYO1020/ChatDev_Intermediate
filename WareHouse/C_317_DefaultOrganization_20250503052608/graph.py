'''
Graph class to represent towns and roads, and to perform DFS for maximum path length.
'''
class Graph:
    def __init__(self, num_towns):
        self.adjacency_list = {}
        self.max_length = 0  # Global variable to track maximum path length
        self.num_towns = num_towns  # Store the number of towns
    def add_edge(self, a, b, c):
        '''
        Adds a road (edge) between two towns (nodes) with a specified length.
        '''
        if a not in self.adjacency_list:
            self.adjacency_list[a] = []
        if b not in self.adjacency_list:
            self.adjacency_list[b] = []
        self.adjacency_list[a].append((b, c))
        self.adjacency_list[b].append((a, c))  # Assuming undirected graph
    def dfs(self, town, visited, current_length):
        '''
        Performs depth-first search to explore all paths from a given town.
        Updates the maximum path length found during the exploration.
        '''
        visited.add(town)  # Mark the current town as visited
        for neighbor, length in self.adjacency_list.get(town, []):
            if neighbor not in visited:  # Only visit unvisited towns
                # Calculate new length only when moving to a new town
                new_length = current_length + length
                # Update max_length if the new path length is greater
                self.max_length = max(self.max_length, new_length)
                self.dfs(neighbor, visited, new_length)  # Recursive call to explore further
        visited.remove(town)  # Backtrack: unmark the town as visited
    def find_max_length(self):
        '''
        Iterates over all towns and initiates DFS to find the maximum path length.
        Ensures all towns are considered, even if they have no roads.
        '''
        self.max_length = 0  # Reset max_length before starting
        for town in range(1, self.num_towns + 1):  # Iterate through all towns
            # Always call DFS for each town, even if it has no roads
            self.dfs(town, set(), 0)
        return self.max_length