'''
Main application file for the Ball Arrangement Calculator.
'''
from arrangement_calculator import countArrangements
def main():
    # Read input values for N and K
    try:
        N = int(input("Enter N (Total Balls): "))
        K = int(input("Enter K (Blue Balls): "))
        if N < 0 or K < 0 or K > N:
            raise ValueError("Invalid input values.")
        arrangements = countArrangements(N, K)
        print(f"Arrangements: {arrangements}")
    except ValueError as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()