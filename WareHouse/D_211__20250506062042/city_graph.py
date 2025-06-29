'''
Module to define the CityGraph class for managing cities and roads.
'''
from collections import deque, defaultdict
class CityGraph:
    def __init__(self, N):
        self.N = N
        self.graph = defaultdict(list)
        self.roads_set = set()  # To track added roads
    def add_road(self, A, B):
        '''
        Adds a road between city A and city B in both directions.
        Prevents adding self-loops and duplicate roads.
        '''
        if A == B:
            print(f"Invalid road: Self-loops are not allowed for cities {A}.")
            return False
        if (A, B) not in self.roads_set:  # Check if the road already exists
            self.graph[A].append(B)
            self.graph[B].append(A)
            self.roads_set.add((A, B))  # Track the added road
            return True
        return False
    def find_shortest_paths(self):
        '''
        Implements BFS to find the number of shortest paths from City 1 to City N.
        Returns the number of shortest paths modulo (10^9 + 7).
        Initializes distance and count for all cities.
        '''
        MOD = 10**9 + 7
        # If there is only one city, return 1 as the only path is to stay in the same city
        if self.N == 1:
            return 1
        # Check if there are no roads and more than one city
        if self.N > 1 and not any(self.graph.values()):
            return 0  # No paths exist if there are multiple cities and no roads
        # Initialize distances to infinity and counts to 0 for all cities
        distance = {i: float('inf') for i in range(1, self.N + 1)}
        count = {i: 0 for i in range(1, self.N + 1)}
        queue = deque([1])
        distance[1] = 0  # Distance to the starting city is 0
        count[1] = 1     # There is one way to reach the starting city
        while queue:
            current = queue.popleft()
            for neighbor in self.graph[current]:
                # If a shorter path to neighbor is found
                if distance[neighbor] > distance[current] + 1:
                    distance[neighbor] = distance[current] + 1
                    count[neighbor] = count[current]
                    queue.append(neighbor)
                # If another shortest path to neighbor is found
                elif distance[neighbor] == distance[current] + 1:
                    count[neighbor] = (count[neighbor] + count[current]) % MOD
        # Check if City N is reachable
        if distance[self.N] == float('inf'):
            return 0  # City N is not reachable
        return count[self.N]  # Return the number of shortest paths to City N