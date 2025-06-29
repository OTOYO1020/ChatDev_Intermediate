'''
Main application file for the Road Explorer.
'''
from graph import Graph
class RoadExplorerApp:
    def __init__(self):
        self.num_towns = 0  # Initialize number of towns
        self.num_roads = 0  # Initialize number of roads
        self.roads = []  # Initialize list of roads
        self.graph = None  # Initialize Graph as None
    def set_parameters(self, num_towns, num_roads):
        try:
            self.num_towns = int(num_towns)
            self.num_roads = int(num_roads)
            if self.num_towns <= 0 or self.num_roads < 0:
                raise ValueError("Number of towns must be positive and number of roads cannot be negative.")
            self.graph = Graph(self.num_towns)  # Initialize Graph with num_towns
            print("Parameters set successfully.")
        except ValueError as e:
            print(f"Input Error: {e}")
    def add_road(self, a, b, c):
        try:
            a = int(a)  # Read Town A
            b = int(b)  # Read Town B
            c = int(c)  # Read Length of Road
            if 1 <= a <= self.num_towns and 1 <= b <= self.num_towns and c > 0:
                self.roads.append((a, b, c))
                self.graph.add_edge(a, b, c)
                print("Road added successfully.")
            else:
                print("Input Error: Towns must be between 1 and the number of towns, and road length must be positive.")
        except ValueError:
            print("Input Error: Please enter valid integers.")
    def calculate_max_length(self):
        max_length = self.graph.find_max_length()
        print(max_length)  # Print only the max length as per output format
if __name__ == "__main__":
    app = RoadExplorerApp()
    # Read number of towns and roads from standard input
    num_towns, num_roads = map(int, input().split())
    app.set_parameters(num_towns, num_roads)  # Set number of towns and roads
    # Read each road from standard input
    for _ in range(num_roads):
        a, b, c = map(int, input().split())
        app.add_road(a, b, c)  # Add roads
    app.calculate_max_length()  # Calculate and print max length