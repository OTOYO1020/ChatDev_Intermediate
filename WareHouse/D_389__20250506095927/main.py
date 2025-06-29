'''
This is the main application file that reads the radius from standard input
and calculates the number of squares contained within a circle.
'''
from circle_square_counter import CircleSquareCounter
def main():
    try:
        radius = int(input("Enter the radius of the circle: "))
        counter = CircleSquareCounter(radius)
        count = counter.count_squares()
        print(f"Number of squares: {count}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()