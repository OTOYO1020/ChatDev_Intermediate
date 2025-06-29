'''
Main entry point for the application that handles input and output.
'''
from utils import evaluate_combinations
def main():
    try:
        n = int(input("Enter an integer N: "))
        s = input("Enter a binary string S (with '?'): ")
        max_value = evaluate_combinations(s, n)
        print(max_value if max_value != -1 else "-1")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()