'''
Main application file for the Takahashi step calculator.
'''
from calculator import min_steps_to_reach_destination
def main():
    try:
        R = int(input("Enter Step Size (R, positive integer): "))
        X = int(input("Enter Destination X (between -10^9 and 10^9): "))
        Y = int(input("Enter Destination Y (between -10^9 and 10^9): "))
        # Ensure that R is positive and greater than zero
        if R <= 0:
            print("Input Error: Step size R must be a positive integer greater than zero.")
            return
        # Validate the ranges for X and Y
        if not (-10**9 <= X <= 10**9) or not (-10**9 <= Y <= 10**9):
            print("Input Error: X and Y must be within the range of -10^9 to 10^9.")
            return
        # Check if the destination is the origin
        if (X, Y) == (0, 0):
            print("You are already at the destination (0, 0). No steps needed.")
            return
        result = min_steps_to_reach_destination(R, X, Y)
        print(f"Minimum Steps: {result}")
    except ValueError:
        print("Input Error: Please enter valid integers for R, X, and Y.")
if __name__ == "__main__":
    main()