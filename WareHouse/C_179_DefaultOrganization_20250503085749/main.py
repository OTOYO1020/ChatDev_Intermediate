'''
Main application file for the Tuple Counter.
'''
from tuple_counter import count_valid_tuples
def main():
    '''
    Main function to read input and calculate valid tuples.
    '''
    try:
        N = int(input("Enter a positive integer N: "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        count = count_valid_tuples(N)
        print(f"Number of valid tuples: {count}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()