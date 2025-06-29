'''
Main application entry point for finding the K-th smallest 321-like number.
'''
from number_utils import find_kth_321_like_number
if __name__ == "__main__":
    try:
        K = int(input("Enter K: "))
        result = find_kth_321_like_number(K)
        print(f"The {K}-th smallest 321-like Number is: {result}")
    except ValueError as e:
        print(f"Error: {e}")