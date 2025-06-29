'''
Main application file for the Quiz Points Calculator.
'''
from input_validation import InputValidation  # Ensure this line is present
def calculate_points(n, x, s):
    """
    Calculate the final points based on the answers provided.
    Parameters:
    n (int): Number of quiz questions.
    x (int): Initial points.
    s (str): String of answers consisting of 'o' and 'x'.
    Returns:
    int: Final points after processing the answers.
    """
    points = x
    for char in s:
        if char == 'o':
            points += 1
        elif char == 'x':
            if points > 0:
                points -= 1
    return points
if __name__ == "__main__":
    try:
        n = input("Please enter the number of quiz questions (N, positive integer): ")
        x = input("Please enter the initial points (X, non-negative integer): ")
        # Validate N and X before conversion
        if not InputValidation.validate_integer(n) or int(n) <= 0:
            raise ValueError("Number of Questions (N) must be a positive integer.")
        if not InputValidation.validate_integer(x) or int(x) < 0:
            raise ValueError("Initial Points (X) must be a non-negative integer.")
        # Convert inputs to integers after validation
        n = int(n)
        x = int(x)
        while True:
            s = input("Please enter the answers string (S) consisting of 'o' and 'x': ")
            # Validate the answers string before checking its length
            if not InputValidation.validate_string(s):
                print("Invalid input. Answers string must only contain 'o' and 'x'. Please try again.")
                continue
            # Validate the length of the answers string (S) against the number of questions (N)
            if len(s) != n:
                print("Invalid input. The length of the answers string (S) must match the number of questions (N). Please try again.")
                continue
            break  # Exit the loop if valid input is received
        final_points = calculate_points(n, x, s)
        print(f"Final Points: {final_points}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")