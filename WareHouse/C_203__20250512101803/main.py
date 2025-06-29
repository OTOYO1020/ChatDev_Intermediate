'''
Main application file for the Village Reach Calculator.
'''
import re
from village_logic import max_village_reached
def main():
    try:
        N = int(input("Enter number of friends (N): "))
        K = int(input("Enter initial yen (K): "))
        friends_input = input("Enter friends (A_i, B_i) as comma-separated tuples: ")
        # Regular expression to match the expected format of (A_i, B_i)
        pattern = r'\(\d+,\s*\d+\)'
        matches = re.findall(pattern, friends_input)
        if len(matches) != N:
            raise ValueError("Number of friends does not match N.")
        # Safely parse the input string to create a list of tuples
        friends = []
        for match in matches:
            A_i, B_i = map(int, match.strip('()').split(','))
            friends.append((A_i, B_i))
        max_village = max_village_reached(N, K, friends)
        print(f"Maximum Village Reached: {max_village}")
    except Exception as e:
        print(f"Input Error: {str(e)}")
if __name__ == "__main__":
    main()