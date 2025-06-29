'''
Main application file for counting integers without the digit '7' in decimal and octal representations.
'''
from count_logic import calculate_count
def main():
    try:
        N = int(input("Please enter a positive integer (N) to count valid integers: "))
        if N < 1:
            raise ValueError("N must be a positive integer.")
        count = calculate_count(N)
        print(f"Count of valid integers: {count}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()