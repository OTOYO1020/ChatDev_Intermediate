'''
Main application file for the Takahashi operations checker.
'''
import sys
from operations import can_complete_operations
def main():
    user_input = input("Enter the sequence of operations: ")
    result = can_complete_operations(user_input)
    if result:
        print("Takahashi can complete the operations.")
    else:
        print("Takahashi faints!")
if __name__ == "__main__":
    main()