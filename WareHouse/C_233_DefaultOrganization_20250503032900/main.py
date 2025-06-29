'''
Main application file for the ball combination calculator.
'''
from combinations import count_combinations
class MainApp:
    def __init__(self):
        self.bags = []
        self.get_input()
    def get_input(self):
        N = int(input("Enter the number of bags (N): "))  # Enhanced prompt for clarity
        for i in range(N):
            L_i = int(input(f"Enter the number of balls in bag {i + 1}: "))
            ball_values = []
            for j in range(L_i):
                a_ij = int(input(f"Enter the value of ball {j + 1} in bag {i + 1}: "))
                ball_values.append(a_ij)
            self.bags.append(ball_values)
        X = int(input("Enter the target product: "))
        count = count_combinations(0, 1, X, self.bags)  # Pass bags here
        print(f"Valid Combinations: {count}")
if __name__ == "__main__":
    app = MainApp()