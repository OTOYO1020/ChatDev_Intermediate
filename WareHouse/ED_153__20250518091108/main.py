'''
Main application file for the Magic Points Calculator.
'''
from typing import List
from calculator import minimum_magic_points
def main():
    H = int(input("Enter Monster Health (H): "))
    A = list(map(int, input("Enter Spells (A) - comma separated: ").split(',')))
    B = list(map(int, input("Enter Costs (B) - comma separated: ").split(',')))
    # Check if the lengths of A and B match
    if len(A) != len(B):
        print("Error: The number of spells must match the number of costs.")
        return
    min_magic_points = minimum_magic_points(H, len(A), A, B)
    if min_magic_points == -1:
        print("It is impossible to reduce the monster's health to 0 with the given spells.")
    else:
        print(f"Minimum Magic Points: {min_magic_points}")
if __name__ == "__main__":
    main()