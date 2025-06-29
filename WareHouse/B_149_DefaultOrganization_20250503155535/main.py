'''
Main application file for the cookie simulation program.
'''
def get_non_negative_integer(prompt):
    """Helper function to get a non-negative integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")
def main():
    """Main function to simulate cookie actions between Takahashi and Aoki."""
    # Read integers A, B, and K from standard input with validation
    A = get_non_negative_integer("Please enter the number of cookies that Takahashi has: ")
    B = get_non_negative_integer("Please enter the number of cookies that Aoki has: ")
    K = get_non_negative_integer("Please enter the number of actions to perform: ")
    takahashi_cookies = A
    aoki_cookies = B
    # Loop K times to simulate the actions
    for _ in range(K):
        if takahashi_cookies > 0:
            takahashi_cookies -= 1
        elif aoki_cookies > 0:
            aoki_cookies -= 1
    # Print the final counts of cookies for Takahashi and Aoki
    print(f"Remaining cookies - Takahashi: {takahashi_cookies}, Aoki: {aoki_cookies}")
if __name__ == "__main__":
    main()