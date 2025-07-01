'''
Main application file for the smallest integer finder.
'''
from utils import find_smallest_x
def main():
    try:
        n = int(input("Please enter a non-negative integer N: "))
        result = find_smallest_x(n)
        if result is not None:
            print(f"The smallest integer X is: {result}")
        else:
            print("No valid X found within the maximum attempts.")
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()