'''
Main application file for the smallest integer finder.
'''
from utils import find_smallest_x
def main():
    try:
        n = int(input("Enter an integer N: "))
        result = find_smallest_x(n)
        print(f"The smallest integer X is: {result}")
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()