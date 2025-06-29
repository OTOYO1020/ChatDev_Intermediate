'''
Main application file for the Pentagon Distance Calculator.
'''
import math
from pentagon import get_coordinates
def main():
    '''
    Main function to execute the Pentagon Distance Calculator.
    It reads four characters from the user, validates them, 
    retrieves their coordinates, calculates distances, and compares them.
    '''
    valid_characters = "ABCDE"
    while True:
        # Read input characters from the user
        S1 = input("Enter S1 (A, B, C, D, E): ").strip()
        S2 = input("Enter S2 (A, B, C, D, E): ").strip()
        T1 = input("Enter T1 (A, B, C, D, E): ").strip()
        T2 = input("Enter T2 (A, B, C, D, E): ").strip()
        # Check if inputs are single characters and within the valid set
        if (len(S1) != 1 or S1 not in valid_characters or 
            len(S2) != 1 or S2 not in valid_characters or 
            len(T1) != 1 or T1 not in valid_characters or 
            len(T2) != 1 or T2 not in valid_characters):
            print("Invalid input. Use single characters A, B, C, D, E.")
            continue  # Prompt for input again
        # Ensure S1 is not equal to S2 and T1 is not equal to T2
        if S1 == S2 or T1 == T2:
            print("Invalid input. S1 must not be equal to S2 and T1 must not be equal to T2.")
            continue  # Prompt for input again
        break  # Exit the loop if all inputs are valid
    try:
        # Get coordinates for each vertex
        x1, y1 = get_coordinates(S1)
        x2, y2 = get_coordinates(S2)
        x3, y3 = get_coordinates(T1)
        x4, y4 = get_coordinates(T2)
    except ValueError as e:
        print(e)
        return
    # Calculate the distance between points S1 and S2
    distance_S = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    # Calculate the distance between points T1 and T2
    distance_T = math.sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
    # Compare the distances using a tolerance level for floating-point precision
    if math.isclose(distance_S, distance_T, rel_tol=1e-9):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()