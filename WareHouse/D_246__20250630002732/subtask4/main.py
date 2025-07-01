'''
Main application file for finding the smallest integer X that satisfies the given conditions.
'''
from computation import Computation
def main():
    '''
    Main function to read input and find the smallest integer X.
    '''
    try:
        n = int(input("Enter an integer N: "))
        computation = Computation()
        result = computation.find_x(n)
        print(f"The smallest X is: {result}")
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()