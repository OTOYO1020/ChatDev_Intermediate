'''
Main entry point of the Bounce Application.
'''
from bounce_calculator import calculate_bounces
def main():
    N, X = map(int, input("Enter N and X on the first line:\n").split())
    L = list(map(int, input("Enter the list of L on the second line:\n").split()))
    bounce_count = calculate_bounces(N, X, L)
    print(f"Number of bounces: {bounce_count}")
if __name__ == "__main__":
    main()