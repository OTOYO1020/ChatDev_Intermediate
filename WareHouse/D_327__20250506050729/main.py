'''
Main application file for the Good Pair Checker.
'''
from sys import stdin
from good_pair import is_good_pair
def main():
    # Read input from standard input
    input_data = stdin.read().strip().splitlines()
    n, m = map(int, input_data[0].split())
    # Read A and B from the subsequent lines
    a = []
    b = []
    for i in range(1, m + 1):
        ai, bi = map(int, input_data[i].split())
        a.append(ai)
        b.append(bi)
    # Call the function and print the result
    result = is_good_pair(n, m, a, b)
    print(result)
if __name__ == "__main__":
    main()