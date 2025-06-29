'''
Main application file to run the ball arrangement application.
'''
from logic import countArrangements
def main():
    # Read input values
    N, M, K = map(int, input("Enter N, M, K separated by spaces: ").split())
    result = countArrangements(N, M, K)
    print(f"Valid arrangements: {result}")
if __name__ == "__main__":
    main()