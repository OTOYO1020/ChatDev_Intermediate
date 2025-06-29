'''
Main application file for the Coprime Finder.
'''
from coprime_utils import find_coprime_integers
def main():
    try:
        N = int(input("Enter number of integers (N): "))
        if N < 0:
            raise ValueError("N must be a non-negative integer.")
        M = int(input("Enter upper limit (M): "))
        if M < 1:
            raise ValueError("M must be a positive integer.")
        A = []
        if N > 0:
            while True:
                try:
                    A = list(map(int, input("Enter integers (space-separated): ").split()))
                    if len(A) != N:
                        raise ValueError("The number of integers provided does not match N.")
                    if any(a <= 0 for a in A):
                        raise ValueError("All integers in A must be positive.")
                    break  # Exit loop if input is valid
                except ValueError as e:
                    print("Invalid input for list A. Please enter positive integers only.")
        # If N is 0, we should not call find_coprime_integers
        if N == 0:
            print("No integers to check for coprimality.")
            return
        result = find_coprime_integers(N, M, A)
        if result:
            print("Coprime integers:", " ".join(map(str, result)))
        else:
            print("No coprime integers found.")
    except ValueError as e:
        print("Input Error:", str(e))
if __name__ == "__main__":
    main()