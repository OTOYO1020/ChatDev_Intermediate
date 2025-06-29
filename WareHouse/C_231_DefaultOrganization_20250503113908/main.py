'''
Main application file for the Student Height Query application.
'''
from utils import count_students
def get_heights(N):
    while True:
        attempts = 3  # Maximum attempts for valid input
        try:
            heights = list(map(int, input(f"Enter {N} heights separated by spaces: ").split()))
            if len(heights) != N:
                raise ValueError(f"Expected {N} heights, but got {len(heights)}.")
            return heights
        except ValueError as e:
            attempts -= 1
            print(f"Invalid input. {e} You have {attempts} attempts left.")
            if attempts == 0:
                raise ValueError("Exceeded maximum attempts for heights input. Please restart the program.")
def get_query_height():
    attempts = 3  # Reset attempts for each query
    while attempts > 0:
        try:
            query_height = int(input("Enter the query height: "))
            return query_height
        except ValueError:
            attempts -= 1
            print(f"Invalid input. Please enter a valid integer for the query height. You have {attempts} attempts left.")
            if attempts == 0:
                raise ValueError("Exceeded maximum attempts for query input. Please restart the program.")
def main():
    try:
        # Read integers N and Q from standard input
        N, Q = map(int, input().split())
        if N <= 0 or Q <= 0:
            raise ValueError("N and Q must be positive integers.")
        # Read the heights of the students
        heights = get_heights(N)
        # Sort the heights for binary search
        heights.sort()
        results = []
        # Process each query
        for _ in range(Q):
            query_height = get_query_height()
            count = count_students(heights, query_height)
            results.append(count)
        # Print each result on a new line
        for result in results:
            print(result)
    except ValueError as e:
        print(f"Input error: {e}")
if __name__ == "__main__":
    main()