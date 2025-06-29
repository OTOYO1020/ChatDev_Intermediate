'''
Main application file for the Happiness Calculator.
This script handles user input and outputs the maximum happiness points.
'''
from happiness_calculator import max_happiness
def main():
    try:
        N = int(input("Enter the number of children (N): "))
        A = list(map(int, input("Enter activeness values (comma-separated): ").split(',')))
        if len(A) != N:
            raise ValueError("The number of activeness values must match N.")
        max_hap = max_happiness(N, A)
        print(f"Maximum Happiness Points: {max_hap}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()