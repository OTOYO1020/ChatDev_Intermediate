'''
Main entry point for the Ball Swap application.
'''
from ball_manager import BallManager
def main():
    try:
        n = int(input("Enter the number of balls (N): "))
        if n <= 0:
            raise ValueError("N must be a positive integer.")
        q = int(input("Enter the number of operations (Q): "))
        if q <= 0:
            raise ValueError("Q must be a positive integer.")
        operations = list(map(int, input(f"Enter {q} operations (space-separated): ").split()))
        if len(operations) != q:
            raise ValueError("Number of operations does not match Q.")
        ball_manager = BallManager(n)
        for operation in operations:
            ball_manager.swap_balls(operation)
        print(" ".join(map(str, ball_manager.balls)))
    except ValueError as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()