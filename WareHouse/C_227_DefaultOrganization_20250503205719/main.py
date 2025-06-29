'''
Main application file for the Triple Counter.
'''
from triple_counter import calculate_triples
def main():
    """
    Main function to run the Triple Counter application.
    It reads a positive integer N from standard input and calculates the count of valid triples.
    """
    while True:
        try:
            N = int(input("Please enter a positive integer N: "))
            if N <= 0:
                raise ValueError("N must be a positive integer.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Error: {str(e)}. Please try again.")
    count = calculate_triples(N)
    print(f"Count of valid triples: {count}")
if __name__ == "__main__":
    main()