'''
Main application file for the Unique String Counter.
'''
from unique_string_counter import UniqueStringCounter
def main():
    '''
    Main function to read input and calculate unique strings.
    '''
    input_string = input("Enter a string: ")
    if not input_string:
        print("Input string cannot be empty.")
        return
    try:
        num_swaps = int(input("Enter number of swaps: "))
        counter = UniqueStringCounter(input_string, num_swaps)
        unique_count = counter.calculate_unique_strings()
        print(f"Unique strings count: {unique_count}")
    except ValueError:
        print("Please enter a valid number for swaps.")
if __name__ == "__main__":
    main()