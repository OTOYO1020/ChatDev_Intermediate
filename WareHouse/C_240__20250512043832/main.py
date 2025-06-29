'''
Main application file for the Takahashi reachability checker.
'''
from takahashi import canReachCoordinate
from typing import List, Tuple
def parse_jumps(jumps_input: str) -> List[Tuple[int, int]]:
    '''
    Parses the jumps input string into a list of tuples.
    '''
    jumps = []
    for jump in jumps_input.split():
        if jump.count(',') != 1:  # Ensure there is exactly one comma
            print("Invalid format for jumps. Expected format: a,b")
            return []  # Return an empty list if format is incorrect
        try:
            a, b = map(int, jump.split(','))
            jumps.append((a, b))
        except ValueError:
            print("Invalid input. Please ensure both a and b are integers.")
            return []  # Return an empty list if parsing fails
    return jumps
def main():
    '''
    Main function to gather input and check reachability.
    '''
    try:
        n = int(input("Number of Jumps (N): "))
        # Check if N is 0 or negative
        if n <= 0:
            print("No")
            return
        # Gather jumps input
        jumps_input = input("Jumps (format: a1,b1 a2,b2 ...): ").strip()
        # Check if jumps input is empty
        if not jumps_input:
            print("No")
            return
        jumps = parse_jumps(jumps_input)
        # Check if the number of jumps provided matches N
        if len(jumps) != n:
            print("Number of jumps provided does not match N.")
            return
        x = int(input("Target Coordinate (X): "))
        if canReachCoordinate(n, jumps, x):
            print("Yes")
        else:
            print("No")
    except ValueError:
        print("No")
if __name__ == "__main__":
    main()