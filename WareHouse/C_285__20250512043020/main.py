'''
Main application file for the Problem ID Index Calculator.
'''
from problem_id import find_problem_index
def main():
    '''
    Main function to take user input and calculate the index of the problem ID.
    '''
    problem_id = input("Enter Problem ID: ")
    try:
        index = find_problem_index(problem_id)
        print(f"Index: {index}")
    except ValueError as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()