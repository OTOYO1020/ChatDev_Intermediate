'''
Module for sorting names based on a custom alphabetical order.
'''
def sort_names(order, names):  # Updated function name
    """
    Sorts the names based on the provided custom alphabetical order.
    Parameters:
    order (str): The custom alphabetical order.
    names (list): List of names to be sorted.
    Returns:
    list: Sorted list of names.
    """
    order_map = {char: index for index, char in enumerate(order)}
    def custom_sort(name):
        for char in name:
            if char not in order_map:
                raise ValueError(f"Invalid character '{char}' found in name '{name}'. Only lowercase letters are allowed.")
        return [order_map[char] for char in name]
    return sorted(names, key=custom_sort)