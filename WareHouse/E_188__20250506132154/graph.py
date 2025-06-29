'''
Graph representation for towns and roads.
'''
class Graph:
    def __init__(self, num_towns):
        self.num_towns = num_towns
        self.adj_list = [[] for _ in range(num_towns)]
    def add_edge(self, u, v):
        if 0 <= u < self.num_towns and 0 <= v < self.num_towns:  # Validate indices
            if u != v and v not in self.adj_list[u]:  # Prevent self-loops and duplicates
                self.adj_list[u].append(v)
        else:
            raise ValueError("Town indices are out of range.")
    def dfs(self, start, prices):
        '''
        Perform depth-first search to find the maximum selling price of gold
        reachable from the starting town.
        '''
        visited = set()  # Use a set to track visited nodes
        stack = [start]
        max_price = prices[start]  # Initialize with the price of the starting town
        visited.add(start)  # Mark the starting town as visited
        while stack:
            node = stack.pop()
            max_price = max(max_price, prices[node])  # Update max_price with the current node's price
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:  # Check if neighbor has been visited
                    visited.add(neighbor)
                    stack.append(neighbor)
        return max_price  # Return the max price found