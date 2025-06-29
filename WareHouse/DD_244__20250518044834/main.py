'''
Main application file for the Hat Exchange application.
'''
from hat_exchange import canAchieveTarget
def main():
    # Read input for current hat colors (S) and target hat colors (T)
    S = input("Enter current hat colors (S) separated by commas: ").strip().split(',')
    T = input("Enter target hat colors (T) separated by commas: ").strip().split(',')
    # Validate input
    valid_colors = {'R', 'G', 'B'}
    S = [color.strip() for color in S]  # Strip whitespace from each color
    T = [color.strip() for color in T]  # Strip whitespace from each color
    if len(S) != len(T):
        print("Error: The number of hats in S and T must be the same.")
        return
    if not all(color in valid_colors for color in S) or not all(color in valid_colors for color in T):
        print("Error: Input must only contain 'R', 'G', and 'B'.")
        return
    # Check if the target configuration can be achieved
    result = canAchieveTarget(S, T)
    # Print the result
    print(result)
if __name__ == "__main__":
    main()