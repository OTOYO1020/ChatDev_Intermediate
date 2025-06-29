'''
Main application file for the chokudai counting application.
This program counts the number of ways to form the string 'chokudai' from the input string.
'''
def main():
    # Read input string from the user
    input_string = input().strip()  # Trim whitespace from input
    # Check if the input string is empty
    if not input_string:
        print(0)  # Return 0 since it's impossible to form "chokudai"
        return
    # Target string we want to form
    target = "chokudai"
    # Modulo value to prevent overflow
    mod = 10**9 + 7
    # DP array to store counts for each prefix of 'target' (including empty prefix)
    dp = [0] * (len(target) + 1)
    # Base case: there's one way to form the empty prefix
    dp[0] = 1
    # Iterate through each character in the input string
    for char in input_string:
        # Iterate through the target string in reverse
        for j in range(len(target) - 1, -1, -1):
            # If the character matches the target character
            if char == target[j]:
                # Update the count for the next prefix
                dp[j + 1] = (dp[j + 1] + dp[j]) % mod
    # The result is the number of ways to form the entire target string
    result = dp[len(target)]  # Use len(target) for clarity
    # Print the result
    print(result)
if __name__ == "__main__":
    main()