'''
Main application file for the integer finder.
'''
from integer_finder import find_smallest_integer
def main():
    try:
        N = int(input("Enter an integer N (0 <= N <= 10^18): "))
        result = find_smallest_integer(N)
        print(f"Smallest Integer X: {result}")
    except ValueError:
        print("Input Error: Please enter a valid integer.")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()