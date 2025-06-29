'''
Utility functions for graph operations, including checking arrangements.
'''
def can_line_up(adjacency_list):
    visited = {}
    # Initialize visited dictionary for each person
    for node in adjacency_list:
        visited[node] = False
    def dfs(node, parent):
        visited[node] = True
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:  # If the neighbor has not been visited
                if not dfs(neighbor, node):  # Recursively visit the neighbor
                    return False
            elif neighbor != parent:  # If the neighbor is visited and is not the parent, a cycle exists
                return False
        return True
    # Perform DFS for each person to check for cycles
    for person in adjacency_list:
        if not visited[person]:  # If the person has not been visited
            if not dfs(person, -1):  # Start DFS with no parent (-1)
                return False
    return True