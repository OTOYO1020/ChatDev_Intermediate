'''
Helper functions for calculating operations in hand movement.
'''
def calculate_operations(current_position, target_position, N):
    '''
    Calculate the minimum number of operations required to move from
    current_position to target_position on a circular ring of size N.
    '''
    clockwise_distance = (target_position - current_position) % N
    counter_clockwise_distance = (current_position - target_position) % N
    return min(clockwise_distance, counter_clockwise_distance)