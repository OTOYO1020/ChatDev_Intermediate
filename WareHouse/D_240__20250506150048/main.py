'''
Main entry point for the Ball Management application.
'''
from ball_manager import BallManager
if __name__ == "__main__":
    app = BallManager()
    N = int(input("Enter the number of balls: "))  # Prompt for the number of balls
    for _ in range(N):
        value = int(input("Enter the value of the ball: "))  # Prompt for each ball's value
        app.add_ball(value)
        print(f"Current count of balls: {app.get_count()}")  # Display current count of balls