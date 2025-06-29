'''
Module for reading input and counting numbers with exactly 9 positive divisors.
'''
from divisor_counter import count_numbers_with_nine_divisors
def main():
    try:
        N = int(input("Enter an integer N: "))
        if N < 1:
            print("Input Error: Please enter a positive integer greater than 0.")
            return
        result = count_numbers_with_nine_divisors(N)  # Ensure this function is called
        print(f"Count of numbers with exactly 9 divisors: {result}")
    except ValueError:
        print("Input Error: Please enter a valid integer.")
if __name__ == "__main__":
    main()