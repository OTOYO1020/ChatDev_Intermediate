'''
Main application file for checking if a string can be formed by concatenating two identical strings.
'''
def check_string(n, s):
    """
    Checks if the string S can be formed by concatenating two identical strings based on the integer N.
    Parameters:
    n (int): The length of the string S.
    s (str): The string to be checked.
    """
    # Check if N is even
    if n % 2 != 0:
        print("NO")
        return
    mid = n // 2
    first_half = s[0:mid]
    second_half = s[mid:n]
    # Compare the two halves of the string
    if first_half == second_half:
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    while True:
        try:
            n = int(input())  # Clear prompt for N
            if n <= 0:
                print("N must be a positive integer. Please try again.")
                continue
            break  # Exit loop if valid input is received
        except ValueError:
            print("Invalid input. Please enter a positive integer for N.")
    while True:
        s = input()  # Clear prompt for S
        if len(s) == 0:
            print("The string S cannot be empty. Please try again.")
            continue  # Allow re-entry if the string is empty
        if len(s) != n:
            print(f"The length of the string S must match N ({n}). Please try again.")
            continue  # Allow re-entry if the string length does not match N
        break  # Exit loop if valid input is received
    check_string(n, s)