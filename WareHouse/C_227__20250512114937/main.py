'''
Main application file for counting valid triples (A, B, C) using standard input and output.
'''
from counting import count_triples
def main():
    try:
        N = int(input("Enter a number N: "))
        if N < 1:
            raise ValueError("N must be a positive integer.")
        result = count_triples(N)
        print(f"Number of valid triples: {result}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()