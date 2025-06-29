'''
Main application file for calculating the middle day of the year.
'''
def calculate_middle_day():
    # Read the number of months
    while True:
        try:
            M = int(input("Enter number of months: "))
            if M <= 0:
                raise ValueError("Number of months must be a positive integer.")
            break
        except ValueError as e:
            print(e)
    days = []
    # Read the number of days for each month
    for i in range(M):
        while True:
            try:
                D_i = int(input(f"Days in month {i + 1}: "))
                if D_i <= 0:
                    raise ValueError("Number of days must be a positive integer.")
                days.append(D_i)
                break
            except ValueError as e:
                print(e)
    # Calculate the total number of days in the year
    total_days = sum(days)
    # Compute the middle day index
    middle_day_index = (total_days + 1) // 2
    current_day = 0
    month = 0
    # Loop through each month to find the middle day
    for i in range(M):
        current_day += days[i]
        if current_day >= middle_day_index:
            month = i + 1
            # Calculate the specific day of the month
            day = middle_day_index - (current_day - days[i])  # Adjust for 1-indexing
            if day < 1:
                day = 1  # Ensure day is at least 1
            break
    # Print the results in the format 'Month Day'
    print(f"Middle Day: Month {month}, Day {day}")
if __name__ == "__main__":
    calculate_middle_day()