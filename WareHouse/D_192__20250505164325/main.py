'''
Main application file for the base counting application.
'''
def main():
    import sys
    from utils import get_greatest_digit, count_valid_bases
    # Read input from standard input
    x = input("Enter a string (X): ")
    try:
        m = int(input("Enter an integer (M): "))
        greatest_digit = get_greatest_digit(x)
        count = count_valid_bases(x, greatest_digit, m)
        print(f"Valid bases count: {count}")
    except ValueError:
        print("Please enter a valid integer for M.")
if __name__ == "__main__":
    main()