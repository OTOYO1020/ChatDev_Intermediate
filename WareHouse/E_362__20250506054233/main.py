'''
Main application file for counting arithmetic subsequences using standard input and output.
'''
from arithmetic_subsequence import ArithmeticSubsequence
def main():
    N = int(input())
    A = list(map(int, input().split()))
    results = ArithmeticSubsequence.count_arithmetic_subsequences(A)
    for k, count in enumerate(results, start=1):
        print(count)
if __name__ == "__main__":
    main()