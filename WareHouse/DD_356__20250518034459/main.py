'''
Main application file for the Popcount Sum Calculator.
'''
from computation import compute_popcount_sum
def main():
    try:
        N = int(input("Enter N: "))
        M = int(input("Enter M: "))
        if N < 0 or M < 0:
            raise ValueError("N and M must be non-negative integers.")
        if N > 10**6 or M > 10**6:  # Example upper limit
            raise ValueError("N and M must not exceed 10^6.")
        result = compute_popcount_sum(N, M)
        print(f"Popcount Sum: {result}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()