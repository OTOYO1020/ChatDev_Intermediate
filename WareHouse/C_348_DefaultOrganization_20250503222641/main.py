'''
Main application file for the Bean Deliciousness Calculator.
'''
from collections import defaultdict
import sys
from bean_handler import BeanHandler  # Importing the BeanHandler class
def main():
    '''
    Main function to read input and compute maximum minimum deliciousness.
    '''
    while True:
        try:
            N = int(input("Enter the number of types of beans (positive integer): "))
            if N <= 0:
                raise ValueError("Number of beans must be a positive integer.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")
    bean_handler = BeanHandler()
    for _ in range(N):
        attempts = 3  # Set a maximum number of attempts
        while attempts > 0:
            try:
                A_i, C_i = input("Enter deliciousness (integer) and color (non-empty string) separated by space: ").split()
                A_i = int(A_i)
                C_i = C_i.strip()
                if not C_i:  # Check if color is empty
                    raise ValueError("Color cannot be empty.")
                bean_handler.add_bean(A_i, C_i)
                break  # Exit the loop if input is valid
            except ValueError as e:
                attempts -= 1
                print(f"Invalid input: {e}. You have {attempts} attempts left. Please enter an integer for deliciousness and a non-empty string for color.")
                if attempts == 0:
                    print("Maximum attempts reached. The program will now terminate.")
                    return  # Exit the program if maximum attempts are reached
    max_min_deliciousness = bean_handler.compute_max_min_deliciousness()
    if max_min_deliciousness is None:
        print("No beans were processed. Please ensure you enter valid data.")
    else:
        print(f"Maximum Minimum Deliciousness: {max_min_deliciousness}")
if __name__ == "__main__":
    main()