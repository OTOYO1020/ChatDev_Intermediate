'''
Main application file to run the permutation counting application.
'''
from permutation_logic import PermutationLogic
def main():
    n = int(input("Enter n (3-20): "))
    if n < 3 or n > 20:
        raise ValueError("n must be between 3 and 20.")
    p = list(map(int, input("Enter permutation (space-separated): ").split()))
    if len(p) != n or not all(1 <= x <= n for x in p) or len(set(p)) != n:
        raise ValueError("Invalid permutation input.")
    logic = PermutationLogic(n, p)
    count = logic.count_valid_elements()
    print(f"Count of valid elements: {count}")
if __name__ == "__main__":
    main()