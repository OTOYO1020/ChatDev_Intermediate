'''
Main entry point of the power comparison application.
'''
from power_comparer import PowerComparer
from utils import custom_pow
def main():
    try:
        input_values = input("Enter three non-negative integers A, B, and C separated by spaces: ").split()
        if len(input_values) != 3:
            print("Please enter exactly three integers.")
            return
        A, B, C = map(int, input_values)
        if A < 0 or B < 0 or C < 0:
            print("Please enter non-negative integers.")
            return
        comparer = PowerComparer()
        result = comparer.compare_powers(A, B, C)
        print(result)
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()