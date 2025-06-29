'''
Main application file for the Height Checker.
'''
from height_checker import canBeNonDecreasing
def main():
    try:
        N = int(input("Enter the number of squares (N): "))
        heights = list(map(int, input("Enter the heights (space-separated): ").split()))
        if len(heights) != N:
            raise ValueError("Number of heights does not match N.")
        result = canBeNonDecreasing(N, heights)
        print("Result: " + ("YES" if result else "NO"))
    except ValueError as e:
        print("Input Error:", str(e))
if __name__ == "__main__":
    main()