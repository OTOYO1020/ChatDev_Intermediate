'''
Main entry point for the Palindromic String Counter application.
'''
from typing import List, Tuple  # Importing necessary types
from palindrome_counter import count_palindromic_strings
if __name__ == "__main__":
    T = int(input())
    test_cases = []
    for _ in range(T):
        N, S = input().split()
        test_cases.append((int(N), S))
    results = count_palindromic_strings(T, test_cases)
    print(results)