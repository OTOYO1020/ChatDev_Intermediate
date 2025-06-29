'''
Main application file for the ABC counter application.
'''
import sys  # Import sys for graceful exit
from counting import count_ABC
def get_valid_input(prompt, validation_func, max_attempts=3):
    for attempt in range(max_attempts):
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print(f"Invalid input. Attempt {attempt + 1} of {max_attempts}.")
    print("Maximum attempts exceeded. Exiting.")
    sys.exit(1)
def main():
    print("Welcome to the ABC Counter Application. Please enter the values as prompted.")
    N, Q = map(int, get_valid_input("Enter N and Q: ", lambda x: x.isdigit() and all(int(i) > 0 for i in x.split()), 3))
    if N > 1000 or Q > 1000:
        print("Both N and Q must be less than or equal to 1000. Exiting.")
        return
    S = list(get_valid_input("Enter the string S: ", lambda x: len(x) == N and all(char.isupper() for char in x), 3))
    for _ in range(Q):
        query = get_valid_input("Enter query (index and character): ", 
                                lambda x: len(x.split()) == 2 and 
                                           x.split()[0].isdigit() and 
                                           len(x.split()[1]) == 1 and 
                                           x.split()[1].isupper(), 3)
        X_i = int(query.split()[0]) - 1  # Adjust for 0-based indexing
        C_i = query.split()[1]
        if not (0 <= X_i < N):
            print("Index out of bounds. Please try again.")
            continue
        S[X_i] = C_i
        count = count_ABC(''.join(S))  # Convert list back to string for counting
        print(count)
if __name__ == "__main__":
    main()