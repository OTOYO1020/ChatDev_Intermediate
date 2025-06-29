'''
Main application file for the employee work time calculator.
'''
def read_times(prompt, N, max_attempts=3):
    """
    Reads a list of times from standard input, ensuring that the input is valid.
    Parameters:
    prompt (str): The prompt message to display to the user.
    N (int): The expected number of times to read.
    max_attempts (int): The maximum number of attempts for valid input.
    Returns:
    list: A list of integers representing the times, or an empty list if input fails.
    """
    attempts = 0
    while attempts < max_attempts:
        try:
            times = list(map(int, input(prompt).split(',')))
            if len(times) != N:
                print(f"Error: You must enter exactly {N} times.")
                attempts += 1
                continue
            if any(time < 0 for time in times):
                print("Error: Times must be non-negative integers.")
                attempts += 1
                continue
            return times
        except ValueError:
            print("Error: Invalid input. Please enter integers only.")
            attempts += 1
    print("Maximum attempts reached. Please restart the program to try again.")
    return []
def main():
    """
    Main function to calculate the minimum time required to complete both works
    based on employee input for Work A and Work B.
    """
    N = int(input("Enter the number of employees (must be greater than 0): "))
    if N <= 0:
        print("Error: The number of employees must be greater than 0.")
        return
    A = read_times("Enter times for Work A (comma-separated, no spaces): ", N)
    if not A:  # Check if the input was valid
        return
    B = read_times("Enter times for Work B (comma-separated, no spaces): ", N)
    if not B:  # Check if the input was valid
        return
    min_time = float('inf')
    # Iterate through each employee 'i' from 0 to N-1
    for i in range(N):
        # Calculate the time if both works are assigned to employee 'i'
        time_both = A[i] + B[i]  # No change needed here, as i is now 0-based
        min_time = min(min_time, time_both)
    # Iterate through each pair of employees '(i, j)' where 'i' is not equal to 'j'
    for i in range(N):
        for j in range(N):
            if i != j:
                # Calculate the time if Work A is assigned to employee 'i' and Work B is assigned to employee 'j'
                time_separate = max(A[i], B[j])  # No change needed here, as i and j are now 0-based
                min_time = min(min_time, time_separate)
    print(f"Minimum Time: {min_time}")
if __name__ == "__main__":
    main()