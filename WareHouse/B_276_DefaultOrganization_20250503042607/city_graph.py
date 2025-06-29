'''
Module to define the CityGraph class for managing city connections.
'''
class CityGraph:
    def __init__(self, num_cities):
        # Initialize connections with the correct number of cities
        self.connections = [set() for _ in range(num_cities)]  # Changed to num_cities
    def add_road(self, city_a, city_b):
        # Ensure city indices are within the valid range
        if city_a < 1 or city_a > len(self.connections) or city_b < 1 or city_b > len(self.connections):
            raise ValueError(f"City indices must be between 1 and {len(self.connections)}.")  # Updated range
        if city_a == city_b:
            raise ValueError("A city cannot connect to itself.")  # New check for self-connection
        # Adjusted for 0-based index
        self.connections[city_a - 1].add(city_b)  
        self.connections[city_b - 1].add(city_a)  
    def get_connections(self):
        result = []
        for i in range(len(self.connections)):
            connected_cities = sorted(self.connections[i])
            d_i = len(connected_cities)
            result.append(f"{d_i} " + " ".join(map(str, connected_cities)))
        return result