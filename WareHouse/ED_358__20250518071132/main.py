'''
Main application file to run the String Counter.
'''
from string_counter import count_valid_strings
def main():
    try:
        k = int(input("Enter K (1-1000): "))
        c = list(map(int, input("Enter C (comma-separated, 0-1000): ").split(',')))
        if not validate_input(k, c):
            return
        result = count_valid_strings(k, c)
        print(f"Number of valid strings: {result}")
    except ValueError:
        print("Input Error: Please enter valid integers.")
def validate_input(k, c):
    if not (1 <= k <= 1000):
        print("Input Error: K must be between 1 and 1000.")
        return False
    if len(c) != 26:  # Ensure there are exactly 26 letters
        print("Input Error: C must contain exactly 26 integers for each letter A-Z.")
        return False
    if any(not (0 <= x <= 1000) for x in c):
        print("Input Error: Each C[i] must be between 0 and 1000.")
        return False
    return True
if __name__ == "__main__":
    main()