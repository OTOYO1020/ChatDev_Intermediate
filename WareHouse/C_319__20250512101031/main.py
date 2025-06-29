'''
Main application file for the Takahashi probability calculator.
'''
from probability import calculate_probability
def main():
    grid = []
    print("Please enter the 3x3 grid values (integers between 1 and 9):")
    for i in range(3):
        while True:
            try:
                row = list(map(int, input(f"Enter row {i + 1} (3 integers separated by space): ").strip().split()))
                if len(row) != 3 or any(num < 1 or num > 9 for num in row):
                    raise ValueError
                grid.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter exactly 3 integers between 1 and 9.")
    probability = calculate_probability(grid)
    print(f"Probability of not getting disappointed: {probability:.4f}")
if __name__ == "__main__":
    main()