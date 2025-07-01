'''
Main application file for the smallest integer finder.
'''
from utils import find_smallest_x
def main():
    try:
        n = int(input("Enter a non-negative integer to find the smallest integer X: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
        result = find_smallest_x(n)
        if result is not None:
            print(f"The smallest integer X is: {result}")
        else:
            print("No valid X found.")
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()