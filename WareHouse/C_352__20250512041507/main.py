'''
Main application file for the Giant Height Calculator.
'''
from giant_height import max_head_height
def main():
    # Input number of giants
    n = int(input("Enter the number of giants (N): "))
    # Input shoulder heights
    a = list(map(int, input("Enter shoulder heights (A) (comma-separated): ").split(',')))
    # Input head heights
    b = list(map(int, input("Enter head heights (B) (comma-separated): ").split(',')))
    if len(a) != n or len(b) != n:
        raise ValueError("The length of A and B must match N.")
    max_height = max_head_height(n, a, b)
    print(f"Maximum Head Height: {max_height}")
if __name__ == "__main__":
    main()