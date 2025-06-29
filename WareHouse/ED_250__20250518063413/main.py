'''
Main application file for the set equality checker.
'''
from set_checker import check_equal_sets
def main():
    # Read input for sequences A and B
    while True:
        try:
            A = list(map(int, input("Enter sequence A (comma-separated integers): ").split(',')))
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")
    while True:
        try:
            B = list(map(int, input("Enter sequence B (comma-separated integers): ").split(',')))
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")
    # Read number of queries
    while True:
        try:
            Q = int(input("Enter number of queries: "))
            if Q < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")
    queries = []
    # Read each query
    for _ in range(Q):
        while True:
            try:
                x_i, y_i = map(int, input("Enter query (x_i, y_i): ").split(','))
                if x_i < 0 or y_i < 0:
                    raise ValueError
                queries.append((x_i, y_i))
                break
            except ValueError:
                print("Invalid input. Please enter two non-negative integers separated by a comma.")
    # Get results from the check_equal_sets function
    results = check_equal_sets(A, B, queries)
    # Print results
    for result in results:
        print(result)
if __name__ == "__main__":
    main()