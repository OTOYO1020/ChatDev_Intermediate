'''
Functions to calculate happiness and find maximum happiness using DFS.
'''
def calculate_happiness(current_space, next_space, altitudes):
    # Calculate the happiness based on the altitude difference between two spaces
    if not altitudes or current_space < 1 or current_space > len(altitudes) or next_space < 1 or next_space > len(altitudes):
        return 0  # Return 0 if spaces are out of bounds or altitudes list is empty
    return abs(altitudes[current_space - 1] - altitudes[next_space - 1])  # Adjust for 0-indexing
def find_max_happiness(graph, altitudes):
    max_happiness = 0
    def dfs(space, current_happiness, visited):
        nonlocal max_happiness
        visited.add(space)  # Mark the current space as visited
        max_happiness = max(max_happiness, current_happiness)
        for neighbor in graph.adjacency_list[space]:
            if neighbor not in visited:  # Check if the neighbor has been visited
                happiness_gain = calculate_happiness(space, neighbor, altitudes)  # Pass both space and neighbor
                dfs(neighbor, current_happiness + happiness_gain, visited)
        visited.remove(space)  # Allow revisiting in other paths for different DFS calls
    # Start DFS from Space 1
    visited = set()  # Initialize visited set for the first DFS
    dfs(1, 0, visited)
    # Check for disconnected components
    for space in range(1, graph.num_spaces + 1):
        if space not in visited:
            dfs(space, 0, set())  # Create a new visited set for each disconnected component
    return max_happiness