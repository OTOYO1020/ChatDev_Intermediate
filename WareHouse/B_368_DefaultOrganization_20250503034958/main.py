'''
Main application file for the Operation Counter.
'''
from operation_counter import OperationCounter
def main():
    '''
    Main function to read input and count operations.
    '''
    try:
        N = int(input("Enter the number of positive integers: "))
        input_data = list(map(int, input(f"Enter {N} positive integers (space-separated): ").split()))
        if len(input_data) != N or any(x <= 0 for x in input_data):
            print("Please ensure you enter exactly N positive integers.")
            return
        counter = OperationCounter(input_data)
        operation_count = counter.count_operations()
        print(f"Operations Count: {operation_count}")
    except ValueError:
        print("Invalid input. Please enter integers only.")
if __name__ == "__main__":
    main()