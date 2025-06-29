'''
Utility functions for input validation.
'''
def validate_input(l, r, s):
    if not s:  # Check if the string is empty
        print("Input Error: The string S cannot be empty.")
        return False
    try:
        l = int(l)
        r = int(r)
        # Allow L to equal R and ensure R is within the bounds of the string length
        if l < 1 or r < 1 or l > r or r > len(s):
            raise ValueError("L and R must be positive integers, with L <= R and R <= length of S.")
        return True
    except ValueError as e:
        print(f"Input Error: {e}. Please enter valid integers for L and R.")
        return False