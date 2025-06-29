'''
Main entry point for the application.
'''
from logic import count_valid_integers
def run_app():
    X = input("Enter string X: ")
    M = int(input("Enter maximum value M: "))
    result = count_valid_integers(X, M)
    print(f"Valid integers count: {result}")
if __name__ == "__main__":
    run_app()