'''
Main application file for the meeting participant calculator.
'''
def calculate_participants():
    N = int(input("Enter number of bases: "))
    if N <= 0:  # Check for N being 0 or less
        print(0)
        return
    W = []  # List to store the number of employees at each base
    X = []  # List to store the local time at each base
    for i in range(N):
        # Read number of employees and local time for each base
        employees, local_time = map(int, input(f"Enter number of employees and local time for base {i + 1} (space-separated): ").split())
        if local_time < 0 or local_time > 23:  # Validate local time
            print("Local time must be between 0 and 23.")
            return
        W.append(employees)
        X.append(local_time)
    # Convert local time to UTC
    UTC = [(X[i] + 24) % 24 for i in range(N)]
    # Calculate valid meeting start and end times for each base
    start = [(9 - UTC[i] + 24) % 24 for i in range(N)]
    end = [(18 - UTC[i] + 24) % 24 for i in range(N)]
    max_participants = 0  # Variable to track the maximum number of participants
    # Iterate through all possible meeting start times from 0 to 23
    for start_time in range(24):
        end_time = (start_time + 1) % 24  # Calculate end time for the meeting
        # Count total number of employees that can participate based on valid time slots
        count = sum(W[i] for i in range(N) if 
                    (start[i] <= start_time < end[i]) or 
                    (start[i] > end[i] and (start_time < end[i] or start_time >= start[i])))
        # Update maximum participants if current count is greater
        max_participants = max(max_participants, count)
    print(max_participants)  # Print the maximum number of participants
if __name__ == "__main__":
    calculate_participants()