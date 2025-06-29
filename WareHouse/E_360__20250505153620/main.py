'''
Main entry point of the Ball Swapper application.
'''
from ball_swapper import BallSwapper
def main():
    try:
        N = int(input("Enter number of balls (N): "))
        K = int(input("Enter number of swaps (K): "))
        if N < 1 or K < 0:
            raise ValueError("N must be >= 1 and K must be >= 0.")
        ball_swapper = BallSwapper(N)
        result = ball_swapper.get_expected_position(K)
        print(f"Expected Position R: {result}")
    except ValueError as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()