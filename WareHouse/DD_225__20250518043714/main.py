'''
Module to test the functionality of the process_queries function.
'''
import unittest
from train_network import TrainNetwork
def process_queries(N: int, Q: int, queries: list):
    network = TrainNetwork(N)
    results = []
    for query in queries:
        try:
            if query[0] == 1:  # Connect
                if 1 <= query[1] <= N and 1 <= query[2] <= N:
                    network.add_connection(query[1], query[2])
                else:
                    results.append(f"Invalid connection query: {query}")
            elif query[0] == 2:  # Disconnect
                if 1 <= query[1] <= N and 1 <= query[2] <= N:
                    try:
                        network.remove_connection(query[1], query[2])
                    except ValueError as e:
                        results.append(str(e))
                else:
                    results.append(f"Invalid disconnection query: {query}")
            elif query[0] == 3:  # Retrieve
                if 1 <= query[1] <= N:
                    component = network.get_connected_component(query[1])
                    results.append(" ".join(map(str, sorted(component))))  # Convert to space-separated string
                else:
                    results.append(f"Invalid retrieval query: {query}")
        except ValueError as e:
            results.append(str(e))  # Append the error message instead of returning
    return results  # Return the list of results as is
class TestProcessQueries(unittest.TestCase):
    def test_connect_and_retrieve(self):
        N = 5
        Q = 3
        queries = [
            (1, 1, 2),  # Connect Car 1 and Car 2
            (1, 2, 3),  # Connect Car 2 and Car 3
            (3, 1)      # Retrieve connected component for Car 1
        ]
        expected_output = ["1 2 3"]  # Updated to a space-separated string
        self.assertEqual(process_queries(N, Q, queries), expected_output)
    def test_disconnect(self):
        N = 5
        Q = 4
        queries = [
            (1, 1, 2),  # Connect Car 1 and Car 2
            (1, 2, 3),  # Connect Car 2 and Car 3
            (2, 2, 3),  # Disconnect Car 2 and Car 3
            (3, 1)      # Retrieve connected component for Car 1
        ]
        expected_output = ["1 2"]  # Updated to a space-separated string
        self.assertEqual(process_queries(N, Q, queries), expected_output)
    def test_no_connections(self):
        N = 5
        Q = 1
        queries = [
            (3, 1)  # Retrieve connected component for Car 1
        ]
        expected_output = ["1"]  # Updated to a space-separated string
        self.assertEqual(process_queries(N, Q, queries), expected_output)
    def test_invalid_queries(self):
        N = 5
        Q = 3
        queries = [
            (1, 6, 2),  # Invalid connection
            (2, 1, 7),  # Invalid disconnection
            (3, 0)      # Invalid retrieval
        ]
        expected_output = []  # No valid outputs
        self.assertEqual(process_queries(N, Q, queries), expected_output)
if __name__ == "__main__":
    unittest.main()