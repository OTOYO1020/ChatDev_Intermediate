'''
Main application file for counting arithmetic progressions with a given sum N.
'''
from arithmetic_progression import count_arithmetic_progressions
def main():
    try:
        N = int(input("Enter a positive integer N (1 ≤ N ≤ 10^12): "))
        if N < 1 or N > 10**12:
            raise ValueError("N must be between 1 and 10^12.")
        count = count_arithmetic_progressions(N)
        print(f"Number of arithmetic progressions: {count}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()