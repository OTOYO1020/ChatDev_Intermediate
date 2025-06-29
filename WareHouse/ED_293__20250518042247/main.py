'''
Main application file for the Geometric Series Calculator.
'''
import sys
from calculations import calculate_sum
def main():
    try:
        A = int(input("Enter A: "))
        X = int(input("Enter X: "))
        M = int(input("Enter M: "))
        # Check input constraints immediately after reading
        if not (1 <= A <= 10**9) or not (1 <= M <= 10**9) or not (1 <= X <= 10**12):
            raise ValueError("Input values are out of bounds.")
        result = calculate_sum(A, X, M)
        print(f"Result: {result}")
    except ValueError as ve:
        print(f"Input Error: {str(ve)}")
    except Exception as e:
        print(f"Calculation Error: {str(e)}")
if __name__ == "__main__":
    main()