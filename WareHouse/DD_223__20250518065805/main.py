'''
Main application file for the Lexicographically Smallest Permutation application.
'''
from permutation import find_lexicographically_smallest_permutation, ConstraintError
def main():
    try:
        N = int(input("Enter N: "))
        M = int(input("Enter M: "))
        constraints = []
        if M > 0:
            print("Enter Constraints (A B) separated by semicolons:")
            constraints_input = input().strip().split(';')
            constraints = [tuple(map(int, c.split())) for c in constraints_input if c]
        result = find_lexicographically_smallest_permutation(N, M, constraints)
        if result == -1:
            print("No valid permutation exists due to a cycle in constraints.")
        else:
            print("Permutation:", ' '.join(map(str, result)))
    except ConstraintError as ce:
        print("Constraint Error:", str(ce))
    except Exception as e:
        print("Input Error:", str(e))
if __name__ == "__main__":
    main()