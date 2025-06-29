'''
Main entry point for the bottle testing application.
'''
import sys
def main():
    try:
        # Read the number of bottles from standard input
        input_value = input().strip()
        if not input_value:  # Check if the input is empty
            raise ValueError("Input cannot be empty. Please enter a valid positive integer for the number of bottles.")
        N = int(input_value)
        if N <= 0:
            raise ValueError("The number of bottles must be a positive integer.")
        # Handle the case where there is only one bottle
        if N == 1:
            S = input().strip()
            if S == '1':
                print(1)  # The only bottle is spoiled
            else:
                print("No spoiled bottle detected; all bottles are safe.")
            sys.stdout.flush()
            return  # Exit the program gracefully
    except ValueError as e:
        print(f"Error: {e}")
        return  # Exit the program gracefully
    # Determine the minimum number of friends needed (M)
    M = (N - 1).bit_length()  # Minimum friends needed using binary representation
    # Check if N exceeds the maximum number of bottles that can be identified
    if N > (1 << M) - 1:
        print(f"Error: The number of bottles {N} exceeds the maximum identifiable with {M} friends.")
        return  # Exit the program gracefully
    # Prepare the bottle distribution for each friend
    bottle_distribution = [[] for _ in range(M)]
    # Distribute bottles to friends using a systematic approach
    for bottle in range(1, N + 1):
        friend_index = 0
        while (1 << friend_index) <= bottle:
            if bottle & (1 << friend_index):
                bottle_distribution[friend_index].append(bottle)
            friend_index += 1
    # Print the distribution of bottles to each friend
    for bottles in bottle_distribution:
        print(len(bottles), ' '.join(map(str, bottles)))
        sys.stdout.flush()  # Ensure output is flushed to avoid TLE
    # Read the responses from friends
    S = input().strip()
    # Check if the length of S matches the number of friends M
    if len(S) != M:
        raise ValueError(f"The length of the response string must be equal to the number of friends (M = {M}).")
    # Validate the response string
    if not all(c in '01' for c in S):
        raise ValueError("Response string must only contain '0' and '1'.")
    # Analyze the responses to determine the spoiled bottle
    spoiled_bottle = determine_spoiled_bottle(S)
    # Print the result
    if spoiled_bottle == -1:
        print("No spoiled bottle detected; all bottles are safe.")
    else:
        print(spoiled_bottle)
    sys.stdout.flush()  # Ensure output is flushed to avoid TLE
def determine_spoiled_bottle(responses):
    """
    Analyzes the responses to determine which bottle is spoiled.
    :param responses: A string of '0's and '1's indicating the friends' reactions.
    :return: The number of the spoiled bottle or -1 if none is detected.
    """
    spoiled_bottle = 0
    for i, response in enumerate(responses):
        if response == '1':
            spoiled_bottle += (1 << i)  # Use bitwise to determine the spoiled bottle
    return spoiled_bottle if spoiled_bottle > 0 else -1  # Return -1 if no spoiled bottle detected.
if __name__ == "__main__":
    main()