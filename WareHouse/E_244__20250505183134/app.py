'''
Module to define the App class for the console application.
'''
from graph import Graph
from sequence_counter import SequenceCounter
class App:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.k = 0
        self.s = 0
        self.t = 0
        self.x = 0
    def run(self):
        self.read_input()
        graph = Graph(self.n)
        self.read_edges(graph)
        counter = SequenceCounter(graph, self.k, self.s, self.t, self.x)
        result = counter.count_sequences(self.s, self.k, 0) % 998244353
        print(f"Number of valid sequences: {result}")
    def read_input(self):
        max_attempts = 5  # Set a maximum number of attempts
        attempts = 0
        while attempts < max_attempts:
            try:
                self.n, self.m, self.k, self.s, self.t, self.x = map(int, input("Enter N, M, K, S, T, X: ").split())
                if not (1 <= self.s <= self.n and 1 <= self.t <= self.n and 1 <= self.x <= self.n):
                    raise ValueError("S, T, and X must be within the range of 1 to N.")
                break
            except ValueError as e:
                attempts += 1
                print(f"Invalid input: {e}. Please enter valid integers. Attempts left: {max_attempts - attempts}")
        else:
            print("Maximum attempts reached. Exiting.")
            exit(1)  # Exit the program if maximum attempts are reached
    def read_edges(self, graph):
        edges_read = 0
        max_attempts = 5  # Set a maximum number of attempts
        while edges_read < self.m:
            attempts = 0
            while attempts < max_attempts:
                try:
                    u, v = map(int, input("Enter edge (u v): ").split())
                    if not (1 <= u <= self.n and 1 <= v <= self.n):
                        raise ValueError("Vertices must be within the range of 1 to N.")
                    if v in graph.adjacency_list[u]:  # Check for duplicate edge
                        print("Edge already exists. Please enter a different edge.")
                        continue  # Skip to the next attempt
                    graph.add_edge(u, v)
                    edges_read += 1  # Increment the count of edges read
                    break  # Exit the inner loop on successful input
                except ValueError as e:
                    attempts += 1
                    print(f"Invalid edge input: {e}. Please enter valid integers. Attempts left: {max_attempts - attempts}")
            else:
                print("Maximum attempts reached for edge input. Exiting.")
                exit(1)  # Exit the program if maximum attempts are reached