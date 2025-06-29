'''
Main application file for processing input from standard input.
'''
from input_handler import insert_left, append_right
def main():
    try:
        n = int(input("Enter an integer N (length of string S): "))
        s = input("Enter a string S (composed only of 'L' and 'R'): ")
        if len(s) != n:
            raise ValueError("Length of string S must be equal to N.")
        # Validate that S contains only 'L' and 'R'
        if any(char not in 'LR' for char in s):
            raise ValueError("String S must only contain characters 'L' and 'R'.")
        # Initialize the list A with a single element [0]
        A = [0]
        for i in range(1, n + 1):
            if s[i - 1] == 'L':
                insert_left(A, i)
            elif s[i - 1] == 'R':
                append_right(A, i)
        # Prepare the final contents of A
        print("Result:", ' '.join(map(str, A)))
    except ValueError as e:
        print("Input Error:", str(e))
if __name__ == "__main__":
    main()