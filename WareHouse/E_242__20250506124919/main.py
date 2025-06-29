'''
Main file to run the Palindrome Counting Application.
'''
import sys
from palindrome_generator import PalindromeGenerator
def main():
    input_data = sys.stdin.read().strip().splitlines()
    T = int(input_data[0])
    results = []
    generator = PalindromeGenerator()
    for i in range(1, T + 1):
        n, s = input_data[i].split()
        n = int(n)
        results.append(generator.generate_palindrome(n, s))
    print("\n".join(map(str, results)))
if __name__ == "__main__":
    main()