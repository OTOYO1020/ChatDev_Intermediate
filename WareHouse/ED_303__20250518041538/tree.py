'''
Module to define the Tree class and related functions for star counting.
'''
class Tree:
    def __init__(self, input_data):
        self.edges = self.parse_input(input_data)
        self.degree = self.calculate_degrees()
        self.neighbors = self.calculate_neighbors()
    def parse_input(self, input_data):
        lines = input_data.strip().splitlines()
        try:
            n = int(lines[0])  # First line is the number of edges
            if n < 0:
                raise ValueError("The number of edges cannot be negative.")
            if len(lines) != n + 1:
                raise ValueError("The number of edges does not match the provided edge list.")
        except ValueError:
            raise ValueError("Error: The first line must be an integer representing the number of edges.")
        edges = []  # Use a list to maintain the order of edges
        seen_edges = set()  # To check for duplicates
        for line in lines[1:n+1]:
            try:
                u, v = map(int, line.split())
                if u <= 0 or v <= 0:
                    raise ValueError("Error: Vertex values must be positive integers.")
                edge = (u, v)
                if edge in seen_edges or (v, u) in seen_edges:
                    raise ValueError(f"Error: Duplicate edge detected: {edge}.")
                edges.append(edge)  # Add edge to the list
                seen_edges.add(edge)  # Track seen edges
            except ValueError:
                raise ValueError("Error: Each edge must be defined by two positive integers.")
        return edges  # Return the list of edges
    def calculate_degrees(self):
        degree = {}
        for u, v in self.edges:
            degree[u] = degree.get(u, 0) + 1
            degree[v] = degree.get(v, 0) + 1
        return degree
    def calculate_neighbors(self):
        neighbors = {}
        for u, v in self.edges:
            if u not in neighbors:
                neighbors[u] = []
            if v not in neighbors:
                neighbors[v] = []
            neighbors[u].append(v)
            neighbors[v].append(u)
        return neighbors
    def is_star(self, vertex):
        '''
        Check if the vertex forms a level-k star by having degree k+1 and k degree-1 neighbors.
        '''
        k = self.degree.get(vertex, 0) - 1
        if k < 0:
            return False
        # Count the number of neighbors with degree 1
        degree_one_neighbors = sum(1 for neighbor in self.neighbors[vertex] if self.degree.get(neighbor, 0) == 1)
        return degree_one_neighbors == k
    def count_stars(self):
        '''
        Count the number of level-k stars in the tree based on vertex degrees.
        '''
        if not self.edges:  # Check for empty edge list
            return "No edges provided to count stars."
        stars_count = {}
        has_star_centers = False  # Flag to check if we have any potential star centers
        for vertex, deg in self.degree.items():
            if deg > 1:  # Only consider vertices with degree greater than 1
                has_star_centers = True  # Found at least one potential star center
                k = deg - 1  # Level of the star
                if k not in stars_count:
                    stars_count[k] = 0
                # Check if this vertex forms a star of level k
                if self.is_star(vertex):  # Use the is_star method to validate
                    stars_count[k] += 1  # Count this star
        if not has_star_centers:
            return "No potential star centers found."
        if not stars_count:
            return "No stars found based on the current tree structure."
        return self.output_results(stars_count)
    def output_results(self, stars_count):
        '''
        Format the output to display the number and levels of the stars found in the tree.
        '''
        if not stars_count:
            return "No stars found based on the current tree structure."
        result = []
        for k, count in stars_count.items():
            result.append(f"Level-{k} stars: {count}")
        return "\n".join(result)