'''
Main application file for the Gem Sequence problem using standard input and output.
'''
from gem_sequence import can_form_sequence
def main():
    # Read input
    N, M = map(int, input().split())
    pairs = [tuple(map(int, input().split())) for _ in range(M)]
    required_gems = list(map(int, input().split()))
    # Call the function and get the result
    can_form, min_gems = can_form_sequence(N, M, pairs, required_gems)
    # Output the result
    if can_form:
        print(f"Valid sequence can be formed with {min_gems} gems.")
    else:
        print("Cannot form a valid sequence.")
if __name__ == "__main__":
    main()