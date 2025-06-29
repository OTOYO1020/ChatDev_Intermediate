'''
Main file to run the Lunlun Number Generator application.
'''
import sys
from lunlun_generator import LunlunNumberGenerator
def find_kth_lunlun_number(K):
    '''
    Retrieves the K-th lunlun number based on user input.
    '''
    generator = LunlunNumberGenerator()
    lunlun_numbers = generator.generate_lunlun_numbers(K)
    print(lunlun_numbers[K - 1])  # Print the K-th lunlun number (1-indexed)
if __name__ == "__main__":
    while True:
        try:
            K = int(input("Enter a positive integer K: "))
            if K <= 0:
                raise ValueError("K must be a positive integer.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Error: {str(e)}. Please enter a valid positive integer.")
    find_kth_lunlun_number(K)