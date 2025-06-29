'''
This module contains the CandyDistributionApp class which manages the logic for calculating minimum frustration.
'''
from collections import deque
class CandyDistributionApp:
    def __init__(self):
        self.dislikes = []
        self.frustrations = []
    def get_input(self):
        try:
            N = int(input("Enter the number of people: "))
            self.dislikes = []
            self.frustrations = []
            for i in range(N):
                dislike = int(input(f"Enter disliked person index for person {i + 1}: "))
                if dislike < 0 or dislike >= N:
                    raise ValueError("Disliked person index must be between 0 and N-1.")
                if dislike == i:  # Check for self-dislike
                    raise ValueError("A person cannot dislike themselves.")
                frustration = int(input(f"Enter frustration value for person {i + 1}: "))
                if frustration < 0:
                    raise ValueError("Frustration value must be non-negative.")
                self.dislikes.append(dislike)
                self.frustrations.append(frustration)
            total_frustration = self.calculate_frustration(N)
            self.display_result(total_frustration)
        except ValueError as e:
            print(f"Input Error: {e}")
    def build_graph(self, N):
        graph = {i: [] for i in range(N)}
        for i in range(N):
            disliked_person = self.dislikes[i]
            graph[i].append(disliked_person)  # Create a directed edge from person i to their disliked person
        return graph
    def topological_sort(self, graph):
        in_degree = {i: 0 for i in graph}
        for edges in graph.values():
            for edge in edges:  # Iterate through each disliked person
                in_degree[edge] += 1
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        sorted_order = []
        while queue:
            node = queue.popleft()
            sorted_order.append(node)
            for neighbor in graph[node]:  # Iterate through each disliked person
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        # Check if topological sort was successful (i.e., no cycles)
        if len(sorted_order) != len(graph):
            raise ValueError("The graph has at least one cycle, which makes topological sorting impossible.")
        return sorted_order
    def calculate_frustration(self, N):
        graph = self.build_graph(N)
        sorted_order = self.topological_sort(graph)
        total_frustration = 0
        # Create a set to track disliked persons who have already received candies
        received_candies = set()
        for person in sorted_order:
            disliked_person = self.dislikes[person]
            # Check if the disliked person has already received candies
            if disliked_person in received_candies:
                total_frustration += self.frustrations[person]
            # Mark this person as having received candies
            received_candies.add(person)
            # Also mark the disliked person as having received candies
            received_candies.add(disliked_person)
        return total_frustration
    def display_result(self, total_frustration):
        print(f"Minimum Total Frustration: {total_frustration}")
    def run(self):
        self.get_input()