'''
Main module to read input and calculate maximum happiness from dishes.
'''
from dish import Dish
from happiness_calculator import HappinessCalculator
def main():
    # Read integers N and T from standard input
    n, total_time = map(int, input().split())
    # Input validation for N and T
    if n <= 0 or total_time <= 0:
        print("N and T must be positive integers.")
        return
    dishes = []
    # Read N pairs of integers (A_i, B_i)
    for _ in range(n):
        eating_time, deliciousness = map(int, input().split())
        # Input validation for eating time and deliciousness
        if eating_time < 0 or deliciousness < 0:
            print("Eating time and deliciousness must be non-negative integers.")
            return
        dishes.append(Dish(eating_time, deliciousness))
    # Calculate maximum happiness
    calculator = HappinessCalculator()
    max_happiness = calculator.calculate_max_happiness(dishes, total_time)
    # Print the result
    print(max_happiness)
if __name__ == "__main__":
    main()