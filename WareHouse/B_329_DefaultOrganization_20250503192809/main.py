'''
Main application file for the Second Largest Finder.
'''
from utils import find_second_largest_value
def main():
    '''
    Main function to read input and find the second largest integer.
    '''
    try:
        N = int(input("Enter the number of integers: "))
        if N <= 0:
            print("Error: The number of integers must be a positive integer.")
            return
        A = list(map(int, input("Enter the integers separated by spaces: ").split()))
        if len(A) != N:
            print("Error: The number of integers provided does not match N.")
            return
    except ValueError:
        print("Error: Please enter valid integers.")
        return
    second_largest = find_second_largest_value(A)
    if second_largest is not None:
        print(f"Second Largest: {second_largest}")
    else:
        print("There is no second largest integer.")
if __name__ == "__main__":
    main()