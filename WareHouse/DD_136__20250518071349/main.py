'''
Main application file for the Children Counter.
'''
from utils import validate_input, count_children
def main():
    input_string = input("Enter the string (starts with 'R' and ends with 'L'): ")
    if validate_input(input_string):
        result = count_children(input_string)
        print(f"Children count: {result}")
    else:
        print("Invalid input. Please ensure it starts with 'R' and ends with 'L' and has a length between 2 and 100,000.")
if __name__ == "__main__":
    main()