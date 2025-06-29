'''
Railroad application class to handle user interactions and display results.
'''
from graph import Graph
class RailroadApp:
    def __init__(self):
        self.graph = None
    def run(self):
        self.get_input()
    def get_input(self):
        try:
            num_cities = int(input("Enter the number of cities: "))
            if num_cities <= 0:
                print("Input Error: The number of cities must be a positive integer.")
                return
            num_railroads = int(input("Enter the number of railroads: "))
            if num_railroads < 0:
                print("Input Error: The number of railroads cannot be negative.")
                return
            city_x = int(input("Enter City X: ")) - 1  # Adjust for 0-based indexing
            city_y = int(input("Enter City Y: ")) - 1  # Adjust for 0-based indexing
            # Check if city_x and city_y are within valid range
            if city_x < 0 or city_x >= num_cities or city_y < 0 or city_y >= num_cities:
                print("Input Error: City indices must be within the range of the number of cities.")
                return
            # Check if City X and City Y are the same
            if city_x == city_y:
                print("Input Error: City X and City Y cannot be the same.")
                return
            self.graph = Graph(num_cities)
            for _ in range(num_railroads):
                try:
                    a = int(input("Enter city A: ")) - 1  # Adjust for 0-based indexing
                    b = int(input("Enter city B: ")) - 1  # Adjust for 0-based indexing
                    # Check if a and b are within valid range
                    if a < 0 or a >= num_cities or b < 0 or b >= num_cities:
                        print("Input Error: City indices A and B must be within the range of the number of cities.")
                        return
                    travel_time = int(input("Enter travel time: "))
                    frequency = int(input("Enter frequency: "))
                    if travel_time <= 0 or frequency <= 0:
                        print("Input Error: Travel time and frequency must be positive integers.")
                        return
                    self.graph.add_edge(a, b, travel_time, frequency)
                except ValueError:
                    print("Input Error: Please enter valid integers for railroad data.")
                    return
            earliest_time = self.graph.dijkstra(city_x, city_y)
            if earliest_time == float('inf'):
                print("City Y is unreachable.")
            else:
                print(f"Earliest arrival time at City Y: {earliest_time}")
        except ValueError:
            print("Input Error: Please enter valid integers.")