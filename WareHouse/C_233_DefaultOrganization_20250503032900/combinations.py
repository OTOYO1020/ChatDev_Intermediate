'''
Module for counting valid combinations of ball values.
'''
def count_combinations(current_bag, current_product, target_product, bags):
    '''
    Recursive function to count valid combinations of ball values that yield the target product.
    '''
    def recursive_count(current_bag, current_product, count):
        if current_bag == len(bags):
            if current_product == target_product:  # Simplified base case check
                count[0] += 1
            return count[0]
        for ball_value in bags[current_bag]:
            if current_product == 0:  # If current_product is zero, we should not multiply
                recursive_count(current_bag + 1, ball_value, count)  # Start fresh with the ball value
            elif ball_value != 0:  # Only multiply with non-zero values
                recursive_count(current_bag + 1, current_product * ball_value, count)
        return count[0]
    count = [0]  # Use a list to allow modification within the nested function
    recursive_count(current_bag, current_product, count)
    return count[0]