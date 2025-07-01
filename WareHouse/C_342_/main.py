'''
Main entry point for the Character Replacer application.
'''
from character_replacer import CharacterReplacer
def main():
    # Read integer values N and Q from standard input
    N, Q = map(int, input().split())
    # Validate N and Q
    if N < 0 or Q < 0:
        raise ValueError("N and Q must be non-negative integers.")
    # Read the string S of length N from standard input
    S = input().strip()
    # Validate the length of S
    if len(S) != N:
        raise ValueError(f"The length of S must be {N}.")
    # Initialize a list to store Q pairs of characters (c_i, d_i)
    pairs = []
    # Read the pairs of characters (c_i, d_i) for Q operations
    for _ in range(Q):
        c_i, d_i = input().strip().split()  # Changed to space-separated
        if len(c_i) != 1 or len(d_i) != 1:
            raise ValueError("Both c_i and d_i must be single characters.")
        pairs.append((c_i.strip(), d_i.strip()))
    # Create a CharacterReplacer instance and perform replacements
    replacer = CharacterReplacer(S, pairs)
    modified_string = replacer.perform_replacements()
    # Print the modified string as the output
    print(modified_string)
if __name__ == "__main__":
    main()