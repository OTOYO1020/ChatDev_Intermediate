'''
Module for calculating the minimum number of banknotes needed for a given amount.
'''
def min_banknotes(N: int) -> int:
    '''
    Calculates the minimum number of banknotes needed to pay at least N.
    '''
    # Create a list of banknote values as powers of 10
    banknote_values = [10 ** i for i in range(101)]  # 10^0 to 10^100
    # Handle case where N is less than 1
    if N < 1:
        raise ValueError("Amount must be at least 1.")
    # Determine the smallest power of 10 that is greater than or equal to N
    payment_amount = next(value for value in banknote_values if value >= N)
    # Calculate the number of banknotes used for payment
    payment_banknotes = 0
    for value in reversed(banknote_values):  # Start from the largest denomination
        if payment_amount >= value:
            payment_banknotes += payment_amount // value
            payment_amount %= value
            if payment_amount == 0:
                break
    # Calculate change
    change = payment_amount - N  # Use the original payment amount for change calculation
    # If change is zero, return the payment banknotes
    if change == 0:
        return payment_banknotes
    # Calculate the number of banknotes used for change
    change_banknotes = 0
    for value in reversed(banknote_values):  # Start from the largest denomination
        if change >= value:
            change_banknotes += change // value
            change %= value
    # Total banknotes used
    return payment_banknotes + change_banknotes