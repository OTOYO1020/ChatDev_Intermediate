'''
This module contains the GarbageCollectionApp class which manages the logic for garbage collection scheduling.
'''
class GarbageCollectionApp:
    def __init__(self):
        self.n = 0
        self.q = []
        self.r = []
    def run(self):
        self.get_input()
        self.process_queries()
    def get_input(self):
        while True:
            try:
                user_input = input("Enter the number of garbage types (N) or type 'exit' to quit: ")
                if user_input.lower() == 'exit':
                    print("Exiting the input process.")
                    return  # Exit the method gracefully
                self.n = int(user_input)
                if self.n <= 0:
                    print("Please enter a positive integer for the number of garbage types.")
                    continue
                break
            except ValueError:
                print("Input Error: Please enter a valid integer or type 'exit' to quit.")
        self.q = []
        self.r = []
        for i in range(self.n):
            while True:
                try:
                    values = input(f"Enter collection period and remainder for garbage type {i + 1} (format: period remainder) or type 'exit' to quit: ")
                    if values.lower() == 'exit':
                        print("Exiting the input process.")
                        return  # Exit the method gracefully
                    q_value, r_value = map(int, values.split())
                    if q_value <= 0:
                        print("Collection period must be a positive integer.")
                        continue
                    if r_value < 0 or r_value >= q_value:
                        print("Remainder must be non-negative and less than the collection period.")
                        continue
                    self.q.append(q_value)
                    self.r.append(r_value)
                    break
                except ValueError:
                    print("Input Error: Please enter valid integers for both period and remainder or type 'exit' to quit.")
    def process_queries(self):
        while True:
            try:
                user_input = input("Enter the number of queries (Q) or type 'exit' to quit: ")
                if user_input.lower() == 'exit':
                    print("Exiting the query input.")
                    return  # Exit the method gracefully
                Q = int(user_input)
                if Q <= 0:
                    print("Please enter a positive integer for the number of queries.")
                    continue
                break
            except ValueError:
                print("Input Error: Please enter a valid integer or type 'exit' to quit.")
        results = []
        for i in range(Q):
            while True:
                try:
                    query_input = input(f"Enter query {i + 1} (type day) or type 'exit' to quit: ")
                    if query_input.lower() == 'exit':
                        print("Exiting the query input.")
                        return  # Exit the method gracefully
                    # Split and validate input
                    parts = query_input.split()
                    if len(parts) != 2:
                        print("Please enter exactly two integers: type and day.")
                        continue
                    t_j, d_j = map(int, parts)
                    if t_j < 1 or t_j > self.n or d_j <= 0:
                        print("Please enter valid integers: type must be between 1 and N, and day must be positive.")
                        continue
                    next_day = self.calculate_next_collection(t_j, d_j)
                    results.append(f"Next collection for type {t_j} on day {next_day}.")
                    break  # Exit the loop for this query if valid
                except ValueError:
                    print("Input Error: Please enter valid integers for type and day.")
                except Exception as e:
                    print(f"Error: {e}")
        self.display_results(results)
    def calculate_next_collection(self, t_j, d_j):
        # Validate garbage type before processing
        if t_j < 1 or t_j > self.n:
            raise ValueError("Garbage type out of range.")
        period = self.q[t_j - 1]
        remainder = self.r[t_j - 1]
        if d_j % period == remainder:
            return d_j
        else:
            next_day = d_j + (remainder - (d_j % period) + period) % period
            return next_day
    def display_results(self, results):
        for result in results:
            print(result)