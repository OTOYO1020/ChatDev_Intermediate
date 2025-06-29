'''
Main file to run the egg cost calculator application.
'''
from egg_cost_calculator import EggCostCalculator
def main():
    try:
        n = int(input("Enter the number of eggs needed: "))
        s = int(input("Enter the cost of 6-egg pack: "))
        m = int(input("Enter the cost of 8-egg pack: "))
        l = int(input("Enter the cost of 12-egg pack: "))
        calculator = EggCostCalculator(n, s, m, l)
        min_cost = calculator.calculate_min_cost()
        if min_cost == float('inf'):
            print("Not possible to fulfill the order.")
        else:
            print(f"Minimum Cost: {min_cost}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()