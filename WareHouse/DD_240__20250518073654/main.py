'''
Main application file for the ball counting program.
'''
from ball_counter import BallCounter
def main():
    input_data = input("Enter the number of balls followed by the integers on the balls (space-separated): ")
    try:
        balls = list(map(int, input_data.split()))
        N = balls[0]  # The first number is the count of balls
        ball_list = balls[1:]  # The rest are the integers on the balls
        if len(ball_list) != N:
            raise ValueError("The number of balls does not match the provided count.")
        ball_counter = BallCounter()
        results = ball_counter.count_balls_after_insertion(N, ball_list)
        print("Results:", results)
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()