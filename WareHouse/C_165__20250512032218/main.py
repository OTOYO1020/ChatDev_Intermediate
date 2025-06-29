'''
Main entry point of the application that handles user interactions through standard input and output.
'''
from score_calculator import ScoreCalculator
def main():
    # Read input values
    N = int(input("Enter N: "))
    M = int(input("Enter M: "))
    Q = int(input("Enter Q: "))
    # Validate input bounds
    if N <= 0 or M <= 0 or Q <= 0:
        print("N, M, and Q must be positive integers.")
        return
    queries = []
    print("Enter queries in the format a,b,c,d (one per line), end with an empty line:")
    while True:
        line = input()
        if line == "":
            break
        try:
            queries.append(tuple(map(int, line.split(','))))
        except ValueError:
            print("Invalid query format. Please use a,b,c,d format.")
            return
    # Calculate max score
    calculator = ScoreCalculator()
    max_score = calculator.max_score(N, M, Q, queries)
    print(f"Max Score: {max_score}")
if __name__ == "__main__":
    main()