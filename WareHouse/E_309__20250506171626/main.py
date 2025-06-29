'''
Main entry point for the insurance coverage application using standard input and output.
'''
from family_tree import FamilyTree
def main():
    try:
        n, m = map(int, input().split())  # Read number of persons and insurance purchases
        if n <= 0 or m < 0:
            raise ValueError("Number of persons (N) must be positive and number of insurance purchases (M) cannot be negative.")
        parents = [0] * (n + 1)  # Index 0 is unused
        for i in range(2, n + 1):
            parent = int(input())
            parents[i] = parent
        insurance = []
        for _ in range(m):
            x, y = map(int, input().split())
            if y < 0:
                raise ValueError("The number of generations (y) must be non-negative.")
            insurance.append((x, y))
        family_tree = FamilyTree(n, parents)
        covered_people = set()
        for x, y in insurance:
            covered_people.update(family_tree.get_covered_people(x, y))
        print(len(covered_people))
    except ValueError as ve:
        print(f"Error: {str(ve)}")
    except Exception as e:
        print(f"Error: {str(e)}")
if __name__ == "__main__":
    main()