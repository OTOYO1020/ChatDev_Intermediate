'''
Main application file for the Knight Ways Calculator.
'''
from knight import countKnightWays
def main():
    try:
        x = int(input("Enter X coordinate: "))
        y = int(input("Enter Y coordinate: "))
        ways = countKnightWays(x, y)
        print(f"Ways to reach ({x}, {y}): {ways}")
    except ValueError:
        print("Please enter valid integers.")
if __name__ == "__main__":
    main()