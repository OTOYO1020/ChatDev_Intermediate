'''
Main entry point of the application that processes input strings S and T and checks for correctly typed characters.
'''
def main():
    while True:
        # Read input strings S and T from standard input with clearer instructions
        S = input("Please enter the intended string S: ")
        T = input("Please enter the typed string T: ")
        # Check for empty input
        if not S or not T:
            print("Error: Both strings must be filled out. Please try again.")
            continue  # Prompt the user to re-enter the strings
        # Check if inputs are strings
        if not isinstance(S, str) or not isinstance(T, str):
            print("Error: Both inputs must be valid strings. Please try again.")
            continue  # Prompt the user to re-enter the strings
        # Check if T is long enough to contain S
        if len(T) < len(S):
            print(f"Error: The typed string T is shorter than the intended string S by {len(S) - len(T)} characters. Please try again.")
            continue  # Prompt the user to re-enter the strings
        # Initialize an empty list to store the indices of correctly typed characters
        correct_positions = []
        # Initialize a variable to track the index of the string S
        j = 0
        # Loop through each character in string T using index i
        for i in range(len(T)):
            # Check if there are still characters left in S to match
            if j < len(S) and T[i] == S[j]:
                # If there's a match, append the index i to correct_positions
                correct_positions.append(i)
                # Move to the next character in S
                j += 1
        # Print the contents of correct_positions as a space-separated string
        if correct_positions:
            print("Correctly typed character positions:", " ".join(map(str, correct_positions)))
        else:
            print("No matches found. None of the characters from S were found in T.")
        # Check if all characters in S were matched
        if j < len(S):
            print(f"Warning: Not all characters from S were matched in T. Only {j} out of {len(S)} characters were found.")
        break  # Exit the loop after successful processing
if __name__ == "__main__":
    main()