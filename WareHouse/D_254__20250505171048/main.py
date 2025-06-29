'''
Main application file for the Perfect Square Counter.
'''
from calculator import count_perfect_square_pairs
def main():
    while True:
        try:
            n = int(input("Enter a positive integer N (greater than 0): "))  # Clearer prompt
            if n < 1:
                raise ValueError("N must be a positive integer.")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Input Error: {e}. Please enter a positive integer greater than 0.")  # More informative error message
    count = count_perfect_square_pairs(n)
    print(f"Number of valid pairs: {count}")
if __name__ == "__main__":
    main()