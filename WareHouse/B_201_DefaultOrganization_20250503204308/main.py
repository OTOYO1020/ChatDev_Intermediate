'''
Main application file for the Mountain application.
'''
import sys
from mountain_utils import find_second_highest_mountain
def main():
    # Read the number of mountains with input validation
    while True:
        try:
            N = int(input("Enter the number of mountains: "))
            if N < 2:  # Ensure at least 2 mountains are required
                raise ValueError("At least two mountains are required to determine the second highest.")
            break
        except ValueError as e:
            print("Invalid input. Please enter a valid integer for the number of mountains.")
    mountains = []
    for i in range(N):
        while True:
            try:
                S_i = input("Enter the name of mountain {}: ".format(i + 1)).strip()
                if not S_i:  # Ensure the name is not empty
                    raise ValueError("Mountain name cannot be empty.")
                T_i = int(input("Enter the height of mountain {}: ".format(i + 1)))
                if T_i < 0:  # Ensure height is positive
                    raise ValueError("Mountain height must be a positive integer.")
                mountains.append((T_i, S_i))
                break
            except ValueError as e:
                print("Invalid input. Please enter a valid integer for the height of the mountain.")
    try:
        second_highest_name = find_second_highest_mountain(mountains)
        print("The second highest mountain is:", second_highest_name)
    except ValueError as e:
        print("Error:", str(e))
if __name__ == "__main__":
    main()