'''
Main entry point for the Fuse Burning application.
'''
from fuse_calculator import find_meeting_point
def main():
    try:
        n = int(input("Enter the number of fuses: "))
        a = list(map(float, input("Enter lengths of fuses (comma-separated): ").split(',')))
        b = list(map(float, input("Enter burn speeds (comma-separated): ").split(',')))
        if len(a) != n or len(b) != n:
            raise ValueError("Length of A and B must match N.")
        if any(length <= 0 for length in a) or any(speed <= 0 for speed in b):
            raise ValueError("Lengths and speeds must be positive values.")
        meeting_point = find_meeting_point(n, a, b)
        print(f"Meeting Point: {meeting_point:.2f}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()