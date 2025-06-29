'''
Main application file for finding the K-th smallest 321-like number.
'''
def is_321_like_number(x):
    '''
    Checks if a given positive integer x is a 321-like number.
    A 321-like number has digits that are strictly decreasing.
    '''
    if x <= 0:  # Validate that x is a positive integer
        return False
    digits = str(x)
    return all(digits[i] > digits[i + 1] for i in range(len(digits) - 1))
def generate_321_like_numbers():
    '''
    Generates all 321-like numbers.
    A 321-like number has digits that are strictly decreasing.
    '''
    numbers = []
    def backtrack(current_number, last_digit):
        if current_number > 0:
            numbers.append(current_number)
        for digit in range(last_digit - 1, -1, -1):
            backtrack(current_number * 10 + digit, digit)
    backtrack(0, 9)  # Start with an empty number and the largest digit
    return sorted(numbers)
def main():
    '''
    Main function to read input and find the K-th smallest 321-like number.
    '''
    while True:  # Loop until valid input is received
        try:
            K = int(input("Please enter a positive integer value for K to find the K-th smallest 321-like number: "))
            if K <= 0:
                raise ValueError("K must be a positive integer.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
    # Generate all 321-like numbers
    321_like_numbers = generate_321_like_numbers()  # Generate all valid 321-like numbers
    if K <= len(321_like_numbers):
        print(f"The {K}-th smallest 321-like number is: {321_like_numbers[K - 1]}")
    else:
        print(f"There are only {len(321_like_numbers)} 321-like numbers available.")
if __name__ == "__main__":
    main()