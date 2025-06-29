'''
Main application file for the card hitting cost calculator.
'''
from union_find import UnionFind
from input_handler import InputHandler
import sys
class MainApp:
    def __init__(self):
        self.n = int(sys.stdin.readline().strip())
        self.m = int(sys.stdin.readline().strip())
        self.constraints_text = []
        for _ in range(self.m):
            self.constraints_text.append(sys.stdin.readline().strip())
        self.result_label = ""
        self.calculate_min_cost()
    def calculate_min_cost(self):
        input_handler = InputHandler("\n".join(self.constraints_text), self.n)  # Pass n to InputHandler
        try:
            constraints = input_handler.get_input()
            uf = UnionFind(self.n)
            for x, y, z in constraints:
                uf.union(x, y, z)  # Ensure x and y are 0-based and z is already mod 2
            min_cost = uf.get_min_cost()
            self.result_label = f"Minimum Cost: {min_cost}"
            print(min_cost)  # Output the result as an integer
        except ValueError as e:
            print(f"Input Error: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
if __name__ == "__main__":
    MainApp()