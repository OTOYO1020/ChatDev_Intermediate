'''
Main application file for counting even-digit palindromes.
'''
from palindrome_counter import count_even_digit_palindromes
def main():
    try:
        N = int(input("Enter a number (1 ≤ N < 10^12): "))
        if 1 <= N < 10**12:
            count = count_even_digit_palindromes(N)
            print(f"Count of even-digit palindromes: {count}")
        else:
            print("Error: N must be in the range 1 ≤ N < 10^12.")
    except ValueError:
        print("Error: Please enter a valid integer.")
if __name__ == "__main__":
    main()