'''
Main application file for the unique sums calculator using standard input and output.
'''
from utils import count_sequences
def main():
    # Read input from standard input
    N = int(input())
    if N < 2:
        print(1)
        return
    A = list(map(int, input().split()))
    # Calculate unique sums
    unique_count = count_sequences(N, A)
    print(unique_count)
if __name__ == "__main__":
    main()