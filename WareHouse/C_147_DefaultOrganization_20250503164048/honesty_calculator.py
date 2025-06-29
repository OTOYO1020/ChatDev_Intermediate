'''
Module for calculating honesty based on testimonies.
'''
def is_honest(possible_honest, testimonies):
    '''
    Check if the testimonies are consistent with the set of possible honest persons.
    Parameters:
    possible_honest (set): A set of indices representing possible honest persons.
    testimonies (list): A list of testimonies for each person.
    Returns:
    bool: True if the testimonies are consistent with the honest persons, False otherwise.
    '''
    honest_set = set(possible_honest)
    for i in range(len(testimonies)):
        if i in honest_set:  # If the person is considered honest
            for x, y in testimonies[i]:
                if not (x in honest_set and y in honest_set):
                    return False  
        else:  # If the person is considered non-honest
            for x, y in testimonies[i]:
                # If a non-honest person testifies about an honest person, their testimony should not contradict
                if (x in honest_set and y not in honest_set) or (y in honest_set and x not in honest_set):
                    return False
                # Ensure that non-honest testimonies do not contradict each other
                if x not in honest_set and y not in honest_set:
                    return False  # Non-honest testimonies about non-honest persons should not be valid
                # If one is honest and the other is not, it should contradict
                if (x in honest_set and y not in honest_set) or (y in honest_set and x not in honest_set):
                    return False
    return True