'''
Module to manage the connections between toy train cars.
'''
class TrainNetwork:
    def __init__(self, N):
        # Initialize connections for N toy train cars
        self.connections = {i: set() for i in range(1, N + 1)}
    def add_connection(self, x, y):
        '''
        Adds a connection between car x and car y.
        If the connection already exists or if x is the same as y, it does nothing.
        '''
        if x == y:
            return  # No self-connections
        if y not in self.connections[x]:  # Prevent duplicate connections
            self.connections[x].add(y)
            self.connections[y].add(x)
    def remove_connection(self, x, y):
        '''
        Removes the connection between car x and car y.
        If the connection does not exist or if x is the same as y, it raises an exception.
        '''
        if x == y:
            raise ValueError(f"Cannot disconnect Car {x} from itself.")
        if y in self.connections[x]:  # Only remove if it exists
            self.connections[x].remove(y)
            self.connections[y].remove(x)
        else:
            raise ValueError(f"No connection exists between Car {x} and Car {y}.")
    def get_connected_component(self, x):
        '''
        Retrieves the connected component containing car x.
        Returns a sorted list of car numbers in the component.
        Raises an exception if the car does not exist.
        '''
        if x not in self.connections:
            raise ValueError(f"Car {x} does not exist.")
        visited = set()
        component = []
        def dfs(car):
            visited.add(car)
            component.append(car)
            for neighbor in self.connections.get(car, []):
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(x)
        return sorted(component) if component else [x]  # Return the car itself if no connections