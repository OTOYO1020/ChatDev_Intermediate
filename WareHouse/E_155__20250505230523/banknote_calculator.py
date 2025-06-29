'''
Module for calculating the minimum number of banknotes needed for payment and change.
'''
def calculate_min_banknotes(N_str):
    N = int(N_str)  # Convert to integer for calculations
    # Determine the smallest banknote value greater than or equal to N
    power_of_ten = 1
    while power_of_ten < N:
        power_of_ten *= 10  # Find the next power of ten greater than N
    # Calculate the number of banknotes used by the user
    user_banknotes = 1  # One banknote of value power_of_ten
    # Calculate the change
    change = power_of_ten - N
    # Calculate the number of banknotes the clerk will use to give back the change
    clerk_banknotes = 0
    if change > 0:
        change_power_of_ten = 1
        # Find the largest banknote value less than or equal to change
        while change_power_of_ten <= change:
            change_power_of_ten *= 10
        change_power_of_ten //= 10  # Get the largest banknote less than or equal to change
        # Calculate the number of banknotes for the change
        while change > 0:
            clerk_banknotes += change // change_power_of_ten  # Count how many banknotes of this value
            change %= change_power_of_ten  # Reduce the change by the total value of those banknotes
            change_power_of_ten //= 10  # Move to the next smaller banknote value
    total_banknotes = user_banknotes + clerk_banknotes
    return total_banknotes