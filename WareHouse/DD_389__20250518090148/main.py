'''
Main application file for the Square Counter.
'''
from square_counter import count_squares_within_circle
if __name__ == "__main__":
    # Read the radius R from standard input
    try:
        radius = int(input("Enter radius R: "))
        count = count_squares_within_circle(radius)
        print(f"Number of squares: {count}")
    except ValueError:
        print("Please enter a valid integer.")