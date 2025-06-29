'''
Main application file for the Stage Clear application.
'''
from calculator import calculate_minimum_time
def main():
    try:
        N = int(input("Number of Stages (N): "))
        A = list(map(int, input("First Clear Times (A) (comma-separated): ").split(',')))
        B = list(map(int, input("Subsequent Clear Times (B) (comma-separated): ").split(',')))
        X = int(input("Number of Clears (X): "))
        # Validate input lengths
        if len(A) != N or len(B) != N:
            raise ValueError("The lengths of A and B must match N.")
        total_time = calculate_minimum_time(N, A, B, X)
        print(f"Total Time: {total_time} units")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()