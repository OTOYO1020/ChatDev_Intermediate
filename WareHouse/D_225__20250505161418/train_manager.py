'''
Module to manage the toy train cars and their connections.
'''
class TrainManager:
    def __init__(self, n):
        self.cars = {i: [] for i in range(1, n + 1)}  # Initialize with empty connections for each car
        self.n = n  # Store the number of cars
    def connect(self, x, y):
        """Connects the front of Car y to the rear of Car x."""
        if x in self.cars and y in self.cars:  # Ensure both cars exist
            # Check if y is already connected to another car
            for car in self.cars:
                if y in self.cars[car]:
                    self.cars[car].remove(y)  # Disconnect y from its current connection
                    break
            # Now connect Car y to the end of the chain starting from Car x
            last_car = x
            while self.cars[last_car]:  # Traverse to the last connected car
                last_car = self.cars[last_car][-1]
            if last_car != y and y not in self.cars[last_car]:  # Avoid duplicate connections
                self.cars[last_car].append(y)  # Connect Car y to the end of the chain
    def disconnect(self, x, y):
        """Disconnects the front of Car y from the rear of Car x."""
        if x in self.cars and y in self.cars:  # Ensure both cars exist
            # Check if y is connected to x
            if y in self.cars[x]:
                self.cars[x].remove(y)  # Remove connection from Car x to Car y
                return True
        return False  # Return false if the disconnect operation fails
    def print_connected_component(self, x):
        """
        Retrieves the list of car numbers in the connected component containing Car x.
        Parameters:
        x (int): The car number to find the connected component for.
        Returns:
        list: A list of car numbers in the connected component.
        """
        if x not in self.cars:
            print(f"Car {x} does not exist.")
            return []  # Return an empty list if Car x does not exist.
        visited = set()  # To keep track of visited cars
        component = []  # To store the connected component
        def dfs(car):
            """Depth-First Search to explore connected cars."""
            visited.add(car)
            component.append(car)
            for connected_car in self.cars[car]:
                if connected_car not in visited:
                    dfs(connected_car)
        dfs(x)  # Start DFS from car x
        # Limit the output to 1,000,000 car numbers
        if len(component) > 1000000:
            component = component[:1000000]
        return component