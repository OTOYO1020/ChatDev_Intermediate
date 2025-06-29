'''
Main application file for the workdays calculator.
'''
def calculate_workdays(N, K, C, S):
    """
    Calculate the workdays based on the input parameters.
    Parameters:
    N (int): Total number of days.
    K (int): Number of workdays to find.
    C (int): Number of days off after working.
    S (str): String representing work ('o') and off ('x') days.
    Returns:
    list: A list of workdays (1-indexed).
    """
    workdays = []
    current_day = 0
    # Loop until we find K workdays or exceed the number of days
    while len(workdays) < K and current_day < N:
        if current_day < N and S[current_day] == 'o':  # Check if the current day is a workday
            workdays.append(current_day + 1)  # Append 1-indexed day
            current_day += C + 1  # Skip C days off
        else:
            current_day += 1  # Move to the next day
    return workdays
if __name__ == "__main__":
    # Read input from standard input: N (total days), K (workdays to find), C (days off)
    N, K, C = map(int, input().split())
    S = input().strip()
    # Calculate workdays
    workdays = calculate_workdays(N, K, C, S)
    # Print the output: List of workdays (1-indexed)
    print(workdays)