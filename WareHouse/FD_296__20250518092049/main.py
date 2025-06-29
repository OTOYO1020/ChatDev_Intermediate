'''
Main application file for checking if two sequences can be made equal.
'''
from utils import can_make_equal
def main():
    # Read input sequences from standard input
    sequence_a = input("Enter Sequence A (comma-separated integers, no spaces): ")
    sequence_b = input("Enter Sequence B (comma-separated integers, no spaces): ")
    if not sequence_a or not sequence_b:
        print("Both sequences must be provided.")
        return
    try:
        list_a = list(map(int, sequence_a.replace(" ", "").split(',')))
        list_b = list(map(int, sequence_b.replace(" ", "").split(',')))
        # Check if lengths of both lists are equal
        if len(list_a) != len(list_b):
            print("The lengths of both sequences must be equal.")
            return
        result = can_make_equal(list_a, list_b)
        print(result)
    except ValueError:
        print("Please enter valid integers separated by commas.")
if __name__ == "__main__":
    main()