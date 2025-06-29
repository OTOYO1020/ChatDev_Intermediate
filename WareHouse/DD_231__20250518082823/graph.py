'''
Graph module to handle adjacency relationships and arrangement checking.
'''
from collections import defaultdict, deque  # Import deque for efficient queue operations
def canArrangePeople(N: int, M: int, conditions: list) -> bool:
    '''
    Determines if a valid arrangement of people is possible based on adjacency conditions.
    Parameters:
    N (int): The number of people.
    M (int): The number of conditions.
    conditions (list): A list of tuples representing adjacency requirements.
    Returns:
    bool: True if a valid arrangement exists, otherwise False.
    '''
    if M == 0:
        return True  # No conditions means any arrangement is valid
    graph = Graph(N)
    for a, b in conditions:
        # Validate that the condition pairs are within the range of 1 to N
        if a < 1 or a > N or b < 1 or b > N:
            raise ValueError(f"Condition pairs must be between 1 and {N}. Invalid pair: ({a}, {b})")
        graph.add_edge(a, b)  # Add directed edge from a to b
    return graph.is_valid_arrangement(conditions)
class Graph:
    def __init__(self, vertices):
        '''
        Initializes the graph with a specified number of vertices.
        Parameters:
        vertices (int): The number of vertices in the graph.
        '''
        self.V = vertices
        self.adj_list = defaultdict(list)
    def add_edge(self, u, v):
        '''
        Adds a directed edge from vertex u to vertex v.
        Parameters:
        u (int): The starting vertex of the edge.
        v (int): The ending vertex of the edge.
        '''
        self.adj_list[u].append(v)  # Edge from u to v (directed)
    def is_valid_arrangement(self, conditions):
        '''
        Checks if a valid arrangement is possible by detecting cycles in the directed graph.
        Returns:
        bool: True if no cycles are found, otherwise False.
        '''
        visited = [False] * (self.V + 1)
        rec_stack = [False] * (self.V + 1)  # To track the recursion stack
        for i in range(1, self.V + 1):
            if not visited[i]:
                if self.has_cycle(i, visited, rec_stack):
                    return False
        sorted_order = self.topological_sort()
        if len(sorted_order) != self.V:  # Check if all vertices are included
            return False
        position = {person: idx for idx, person in enumerate(sorted_order)}
        for a, b in conditions:
            if position[a] >= position[b]:  # Ensure a comes before b
                return False
        return True
    def has_cycle(self, v, visited, rec_stack):
        '''
        Detects cycles in the directed graph using DFS.
        Parameters:
        v (int): The current vertex.
        visited (list): List to track visited vertices.
        rec_stack (list): List to track vertices in the current recursion stack.
        Returns:
        bool: True if a cycle is detected, otherwise False.
        '''
        visited[v] = True
        rec_stack[v] = True
        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                if self.has_cycle(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True
        rec_stack[v] = False
        return False
    def topological_sort(self):
        '''
        Performs topological sorting on the directed graph.
        Returns:
        list: A valid order of vertices if possible, otherwise an empty list.
        '''
        in_degree = {i: 0 for i in range(1, self.V + 1)}
        for u in self.adj_list:
            for v in self.adj_list[u]:
                in_degree[v] += 1
        queue = deque([u for u in in_degree if in_degree[u] == 0])  # Use deque
        sorted_order = []
        while queue:
            u = queue.popleft()  # Efficiently pop from the front
            sorted_order.append(u)
            for v in self.adj_list[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        # Check if the sorted order includes all vertices
        return sorted_order if len(sorted_order) == self.V else []  # Return valid order or empty list