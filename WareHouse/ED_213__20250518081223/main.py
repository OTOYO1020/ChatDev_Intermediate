'''
Main application file for the Takahashi Punches Calculator.
'''
from logic import min_punches
def main():
    # Read input values
    H = int(input("Enter Height (H): "))
    W = int(input("Enter Width (W): "))
    print("Enter Grid (each row on a new line):")
    S = [input().strip() for _ in range(H)]
    # Calculate minimum punches needed
    punches_needed = min_punches(H, W, S)
    print(f"Minimum Punches Needed: {punches_needed}")
if __name__ == "__main__":
    main()