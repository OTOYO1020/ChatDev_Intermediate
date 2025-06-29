'''
Main application file for the Ball Position Simulation.
'''
from ball_simulation import expected_position
def main():
    try:
        N = int(input("Enter number of positions (N): "))
        K = int(input("Enter number of operations (K): "))
        if N <= 0 or K < 0:
            raise ValueError("N must be a positive integer and K must be a non-negative integer.")
        result = expected_position(N, K)
        print(f"Result R: {result}")
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()