'''
Main application file for the Lunch Break Calculator.
'''
from lunch_break import min_lunch_break
def main():
    try:
        n = int(input("Number of Departments (N): "))
        k = list(map(int, input("Sizes of Departments (comma-separated): ").split(',')))
        if len(k) != n:
            raise ValueError("The number of departments must match N.")
        result = min_lunch_break(n, k)
        print(f"Minimum Maximum Lunch Break: {result}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()