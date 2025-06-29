'''
Main application file for the Distance Calculator.
'''
from calculator import calculate_steps
def main():
    while True:
        try:
            R = int(input("Enter R (must be > 0): "))
            if R <= 0:
                print("R must be greater than zero. Please try again.")
                continue
            X = int(input("Enter X (must be >= 0): "))
            if X < 0:
                print("X must be a non-negative integer. Please try again.")
                continue
            Y = int(input("Enter Y (must be >= 0): "))  # Clarified prompt
            if Y < 0:
                print("Y must be a non-negative integer. Please try again.")
                continue
            steps = calculate_steps(R, X, Y)
            print(f"Minimum Steps: {steps}")
            break  # Exit the loop if all inputs are valid
        except ValueError:
            print("Please enter valid integers.")
if __name__ == "__main__":
    main()