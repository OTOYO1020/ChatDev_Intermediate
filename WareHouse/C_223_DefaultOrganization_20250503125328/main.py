'''
Main entry point for the fuse meeting point application.
'''
from fuse import FuseCalculator
if __name__ == "__main__":
    # Read the number of fuses
    N = int(input())
    calculator = FuseCalculator()
    # Read lengths and burn speeds
    for _ in range(N):
        length, burn_speed = map(int, input().split())
        calculator.add_fuse(length, burn_speed)
    # Calculate the meeting point
    meeting_point = calculator.calculate_meeting_point()
    print(int(meeting_point))  # Output as an integer