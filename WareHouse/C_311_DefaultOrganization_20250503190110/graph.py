'''
Graph class for representing a directed graph and detecting cycles.
'''
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]  # Initialize with empty lists
    def add_edge(self, u, v):
        if 1 <= u <= self.V and 1 <= v <= self.V:  # Ensure valid vertex indices
            if u == v:  # Check for self-loop
                raise ValueError("Self-loops are not allowed.")
            self.adj_list[u - 1].append(v)  # Append the edge to the list
        else:
            raise ValueError("Vertex indices must be between 1 and N.")
    def detect_cycle(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V
        cycles = []
        def cycle_util(v, path, path_indices):
            visited[v] = True
            rec_stack[v] = True
            path.append(v + 1)  # Adjust for 1-based indexing in output
            path_indices[v] = len(path) - 1  # Store the index of the vertex in the path
            neighbors = self.adj_list[v]
            for neighbor in neighbors:
                neighbor_index = neighbor - 1  # Adjust for 0-based indexing
                if not visited[neighbor_index]:  # If the neighbor has not been visited
                    if cycle_util(neighbor_index, path, path_indices):
                        return True
                elif rec_stack[neighbor_index]:  # If the neighbor is in the recursion stack
                    if neighbor in path:  # Check if the neighbor is in the current path
                        cycle_start_index = path_indices[neighbor_index]
                        cycle = path[cycle_start_index:]
                        # Ensure the cycle is valid
                        if len(cycle) >= 2:
                            # Check if all edges exist in the cycle
                            valid_cycle = True
                            for i in range(len(cycle)):
                                if i == len(cycle) - 1:  # Check last edge back to the first
                                    if cycle[0] not in self.adj_list[cycle[i] - 1]:
                                        valid_cycle = False
                                        break
                                elif cycle[i + 1] not in self.adj_list[cycle[i] - 1]:
                                    valid_cycle = False
                                    break
                            if valid_cycle:
                                # Convert cycle to a tuple to ensure uniqueness
                                cycle_tuple = tuple(sorted(cycle))
                                if cycle_tuple not in cycles:
                                    cycles.append(cycle_tuple)
                                    return True
            path.pop()
            rec_stack[v] = False
            del path_indices[v]  # Clean up the path index
            return False
        for node in range(self.V):
            if not visited[node]:
                path_indices = {}
                cycle_util(node, [], path_indices)
        return cycles