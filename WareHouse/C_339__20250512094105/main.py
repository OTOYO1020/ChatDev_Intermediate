'''
Main application file for the Bus Passenger Calculator.
'''
import sys
from passenger_calculator import minimum_passengers
def main():
    '''
    Main function to handle input and output for the Bus Passenger Calculator.
    '''
    MAX_STOPS = 1000  # Define a maximum limit for the number of stops
    while True:  # Loop until valid input is received
        try:
            # Read number of stops from standard input
            N = int(input("Enter number of stops (N): "))
            # Validate that N is greater than zero and within the maximum limit
            if N <= 0 or N > MAX_STOPS:
                print(f"Error: The number of stops must be a positive integer and less than or equal to {MAX_STOPS}.", file=sys.stderr)
                continue  # Prompt for input again
            break  # Exit loop if input is valid
        except ValueError:
            print("Error: Please enter a valid integer for the number of stops.", file=sys.stderr)
    # Read changes in passengers from standard input
    A_input = input("Enter changes in passengers (comma-separated): ")
    try:
        A = [int(change.strip()) for change in A_input.split(',')]
    except ValueError:
        print("Error: All changes must be valid integers.", file=sys.stderr)
        return  # Exit the function early if input is invalid
    # Validate the number of changes matches the number of stops
    if len(A) != N:
        print("Error: The number of changes must match the number of stops.", file=sys.stderr)
        return  # Exit the function early if lengths do not match
    # Validate that all changes in passengers are within a reasonable range
    for change in A:
        if change < -100 or change > 100:  
            print("Error: Passenger changes must be between -100 and 100.", file=sys.stderr)
            return  # Exit the function early if any change is out of bounds
    # Calculate minimum passengers
    min_passengers = minimum_passengers(N, A)
    # Output the result
    print(f"Minimum Passengers: {min_passengers}")
if __name__ == "__main__":
    main()