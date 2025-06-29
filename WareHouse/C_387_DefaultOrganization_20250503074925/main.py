'''
Main application file for counting Snake numbers within a specified range.
'''
from utils import optimized_count_snake_numbers
def on_calculate():
    try:
        L = int(input("Enter L: "))
        R = int(input("Enter R: "))
        if L < 0 or R < 0:
            raise ValueError("L and R should be non-negative integers.")
        if L > R:
            raise ValueError("L should be less than or equal to R.")
        snake_count = optimized_count_snake_numbers(L, R)
        print(f"Snake Numbers Count: {snake_count}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    on_calculate()