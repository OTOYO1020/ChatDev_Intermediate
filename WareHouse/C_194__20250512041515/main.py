'''
Main application file for the Sum of Squared Differences.
'''
from calculator import sum_of_squared_differences
def main():
    try:
        N = int(input("Enter the number of elements (N): "))
        if N < 2 or N > 300000:
            raise ValueError("N must be between 2 and 300000.")
        A = list(map(int, input("Enter the elements (space-separated): ").split()))
        if len(A) != N or not all(-200 <= x <= 200 for x in A):
            raise ValueError("Invalid input: Ensure the length of A is N and elements are within [-200, 200].")
        result = sum_of_squared_differences(N, A)
        print(f"Sum of Squared Differences: {result}")
    except ValueError as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()