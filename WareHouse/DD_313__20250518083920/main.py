'''
Main application file for the sequence determination task.
'''
from query_manager import QueryManager
import sys
class MainApp:
    def __init__(self):
        self.n, self.k = map(int, input().split())
        if not (self.validate_input(self.n, self.k)):
            print("Invalid input. Ensure K is odd and 1 ≤ K < N ≤ 1000.")
            sys.exit(1)
        self.query_manager = QueryManager(self.n, self.k)
        self.run_queries()
    def validate_input(self, n, k):
        return k % 2 == 1 and 1 <= k < n <= 1000
    def run_queries(self):
        while not self.query_manager.is_sequence_determined():
            if self.query_manager.query_count >= self.n:
                print("Maximum number of queries reached. Terminating program.")
                sys.exit(1)
            query = self.query_manager.generate_query()
            print(f"? {' '.join(map(str, query))}")
            # Input validation for response T
            while True:
                try:
                    response = int(input())
                    if response in [-1, 0, 1]:
                        break
                    else:
                        print("Invalid input. Please enter -1, 0, or 1.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            if response == -1:
                print("Query was invalid. Terminating program.")
                sys.exit(1)
            try:
                self.query_manager.process_response(response, query)
            except ValueError as e:
                print(e)
                sys.exit(1)
        self.display_result()
    def display_result(self):
        result_sequence = self.query_manager.get_sequence()
        print(f"! {' '.join(map(str, result_sequence))}")
if __name__ == "__main__":
    MainApp()