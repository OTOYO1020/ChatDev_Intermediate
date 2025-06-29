'''
This module contains functions for calculating the number of years
required to reach a target balance.
'''
def calculate_years(target_balance):
    '''
    Calculate the number of years required to reach the target balance.
    Parameters:
    target_balance (int): The target balance to reach.
    Returns:
    int: The number of years required to reach the target balance.
    '''
    balance = 100  # Initialize balance to Takahashi's initial deposit
    years = 0  # Initialize years counter
    if target_balance <= 100:  # Check if target balance is already met or less
        return years  # Return 0 years if target balance is 100 or less
    while balance < target_balance:  # Loop until balance reaches or exceeds target
        years += 1  # Increment years
        balance += (balance // 100)  # Update balance
        if years > 1000:  # Safeguard against infinite loop
            raise RuntimeError("Target balance is unreachable with the current growth rate.")
    return years  # Return the total years required