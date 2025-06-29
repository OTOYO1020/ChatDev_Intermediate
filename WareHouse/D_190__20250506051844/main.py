'''
Main application file for the Arithmetic Progression Calculator.
'''
from utils import calculate_arithmetic_progressions
def main():
    '''
    Main function to read input and calculate arithmetic progressions.
    '''
    try:
        N = int(input("Enter a positive integer N to calculate valid arithmetic progressions: "))
        if N <= 0:
            print("Please enter a positive integer greater than zero.")
            return
        count = calculate_arithmetic_progressions(N)
        print(f"Number of valid arithmetic progressions: {count}")
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()