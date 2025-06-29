'''
Main entry point of the ticket purchasing application.
This script reads the number of people and the time taken per person to purchase a ticket,
then calculates and prints the finish times for each person based on their arrival times.
'''
def calculate_finish_times(N, A, arrival_times):
    """
    Calculate the finish times for each person based on their arrival times.
    Parameters:
    N (int): The number of people.
    A (int): The time taken per person to purchase a ticket.
    arrival_times (list): A list of integers representing the arrival times of each person.
    Returns:
    list: A list of finish times for each person.
    """
    current_time = 0
    finish_times = []
    for arrival_time in arrival_times:
        if current_time < arrival_time:
            current_time = arrival_time
        finish_time = current_time + A
        finish_times.append(finish_time)
        current_time = finish_time
    return finish_times
def get_user_input():
    """
    Handles user input for the number of people, time taken per person,
    and their arrival times, while ensuring input validation and error handling.
    Returns:
    tuple: A tuple containing the number of people (N), time taken per person (A),
           and a list of arrival times.
    """
    max_attempts = 3  # Set a maximum number of attempts
    attempts = 0
    while attempts < max_attempts:
        try:
            N = int(input("Enter the number of people (N): "))
            if N <= 0:
                print("N must be a positive integer. Please try again.")
                continue
            A = int(input("Enter the time taken per person to purchase a ticket (A): "))
            if A <= 0:
                print("A must be a positive integer. Please try again.")
                continue
            attempts = 0  # Reset attempts after valid input for N and A
            while True:
                arrival_times_input = input("Enter the arrival times as integers separated by commas (e.g., 1,2,3): ")
                # Validate and convert arrival times
                arrival_times = []
                valid_input = True
                for time in arrival_times_input.split(','):
                    try:
                        arrival_time = int(time.strip())
                        if arrival_time < 0:
                            print("Arrival times must be non-negative integers. Please try again.")
                            valid_input = False
                            break
                        arrival_times.append(arrival_time)
                    except ValueError:
                        print("Invalid input for arrival times. Please ensure all values are integers.")
                        valid_input = False
                        break
                if valid_input:
                    # Validate that the number of arrival times matches N
                    if len(arrival_times) != N:
                        print(f"The number of arrival times must match N ({N}). Please try again.")
                    else:
                        return N, A, arrival_times  # Return valid inputs
                else:
                    print("Please try entering the arrival times again.")
        except ValueError:
            print("Invalid input for N or A. Please enter valid integers.")
            attempts += 1  # Increment the attempt counter
    else:
        print("Maximum attempts reached. Please restart the program to try again.")
        return None, None, None  # Return None if maximum attempts reached
if __name__ == "__main__":
    N, A, arrival_times = get_user_input()
    if N is not None and A is not None and arrival_times is not None:
        # Calculate finish times
        finish_times = calculate_finish_times(N, A, arrival_times)
        # Print finish times
        print("Finish Times:")
        for time in finish_times:
            print(time)