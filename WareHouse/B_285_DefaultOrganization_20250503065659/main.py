'''
Main application file for the string comparison program.
'''
def main():
    while True:
        try:
            N = int(input("Enter a positive integer N (less than or equal to the length of the string): "))
            S = input("Enter a string S: ")
            if N <= 0 or N > len(S):
                print(f"Invalid input. Ensure N is a positive integer and less than or equal to the length of S ({len(S)}). Please try again.")
                continue
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid integer for N.")
            continue
    results = []  # Initialize an empty list to store results
    # Loop through each integer i from 1 to N-1
    for i in range(1, N):
        l = 0  # Initialize l to 0 for each i
        # Check characters S[l] and S[l + i] until we reach the end of the string
        while l + i < N:  # Prevent out-of-bounds access
            if S[l] != S[l + i]:
                l += 1  # Increment l if characters are not equal
            else:
                break  # Break the loop if characters are equal
        results.append(l)  # Append the final value of l to the results list
    # Print the results, each on a new line
    for result in results:
        print(result)
if __name__ == "__main__":
    main()