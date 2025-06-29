'''
Main application file for the playing fields assignment.
'''
from utils import assign_playing_fields
def main():
    try:
        N = int(input("Enter N (total players): "))
        M = int(input("Enter M (number of fields): "))
        if M * 2 + 1 > N:
            raise ValueError("Constraint not satisfied: M * 2 + 1 must be <= N")
        assignments = assign_playing_fields(N, M)
        for pair in assignments:
            print(pair[0], pair[1])  # Print each pair on a new line
    except ValueError as e:
        print(f"Input Error: {e}")
if __name__ == "__main__":
    main()