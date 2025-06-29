'''
Utility functions for calculating the maximum product from an array.
'''
def calculate_max_product(array, K):
    MOD = 10**9 + 7
    if K > len(array):
        raise ValueError("K cannot be greater than the number of elements in the array.")
    # Sort the array in descending order to prioritize larger values
    array.sort(reverse=True)
    max_product = 1
    negative_count = 0
    smallest_negative = None
    # Calculate the product of the first K elements
    for i in range(K):
        max_product *= array[i]
        max_product %= MOD  # Keep it within the modulo
        if array[i] < 0:
            negative_count += 1
            if smallest_negative is None or array[i] > smallest_negative:
                smallest_negative = array[i]
    # If the count of negative numbers is odd, we need to adjust the product
    if negative_count % 2 != 0:
        # Check if there's a next largest negative number available
        if K < len(array):  # Ensure there's a next element
            next_largest_negative = array[K]
            if next_largest_negative < 0:
                # Calculate the potential new product by replacing the smallest negative
                new_product = (max_product // smallest_negative) * next_largest_negative
                new_product %= MOD  # Ensure the new product is within the modulo
                max_product = max(max_product, new_product)  # Choose the maximum product
        else:
            # If no next largest negative number is available, consider the largest positive number
            for i in range(K, len(array)):
                if array[i] > 0:
                    new_product = (max_product // smallest_negative) * array[i]
                    new_product %= MOD
                    max_product = max(max_product, new_product)
    return max_product