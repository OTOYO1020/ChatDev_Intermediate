'''
Main entry point for the Tuple Counting Application.
'''
from counting import count_tuples
def main():
    '''
    Main function to execute the tuple counting logic.
    '''
    try:
        N = int(input("Enter a positive integer N (2 <= N <= 10^6): "))
        if N < 2 or N > 10**6:
            raise ValueError("N must be between 2 and 10^6.")
        count = count_tuples(N)
        print(f"Number of valid tuples (A, B, C): {count}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()