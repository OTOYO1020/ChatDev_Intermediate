'''
Main application file for the Bounce Calculator.
'''
from bounce_calculator import calculate_bounces
def read_input():
    N = int(input("Enter N (number of bounces): "))
    X = int(input("Enter X (bounce limit): "))
    L = list(map(int, input("Enter L (bounces list, space-separated): ").split()))
    if len(L) != N:
        raise ValueError("Length of L must be equal to N.")
    return N, X, L
if __name__ == "__main__":
    try:
        N, X, L = read_input()
        bounce_count = calculate_bounces(N, X, L)
        print(f"Number of bounces: {bounce_count}")
    except ValueError as e:
        print(f"Input Error: {e}")