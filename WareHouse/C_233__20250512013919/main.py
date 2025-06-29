'''
Main file to run the Ball Picker application.
'''
from ball_picker import countWays
def main():
    '''
    Main function to gather input data and calculate the number of ways to pick balls.
    '''
    try:
        N = int(input("Enter number of bags (N): "))
        L = list(map(int, input("Enter counts of balls (L): ").split(',')))
        A = [list(map(int, x.split(','))) for x in input("Enter balls in bags (A): ").split(';')]
        # Input validation
        if len(L) != N or len(A) != N:
            raise ValueError("Error: The length of L and A must match N.")
        X = int(input("Enter target product (X): "))
        result = countWays(N, L, A, X)
        print(f"Number of ways: {result}")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()