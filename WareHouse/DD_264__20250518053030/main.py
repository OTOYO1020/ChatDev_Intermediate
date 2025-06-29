'''
Main application file for the Atcoder swap calculator.
'''
from atcoder_utils import min_operations_to_atcoder
def main():
    input_string = input("Enter a permutation of 'atcoder': ")
    try:
        result = min_operations_to_atcoder(input_string)
        if result == -1:
            print("Error: Input is not a valid permutation of 'atcoder'.")
        else:
            print(f"Minimum swaps needed: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()