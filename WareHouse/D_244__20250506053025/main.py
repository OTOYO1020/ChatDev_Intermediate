'''
Main file to run the Hat Color application.
'''
from hat_color import HatColorChecker  # Import the HatColorChecker class
def main():
    current = input("Enter current hat colors (RGB): ")
    desired = input("Enter desired hat colors (RGB): ")
    # Validate input
    valid_colors = {'R', 'G', 'B'}
    if len(current) != 3 or len(desired) != 3 or not (set(current).issubset(valid_colors) and set(desired).issubset(valid_colors)):
        print("Invalid input. Please ensure you enter exactly 3 characters consisting only of 'R', 'G', and 'B'.")
        return
    checker = HatColorChecker()
    result = checker.can_achieve(current, desired)
    print(result)
if __name__ == "__main__":
    main()