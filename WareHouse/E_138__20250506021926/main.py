'''
Main entry point for the subsequence checking application.
'''
from utils import is_subsequence
def main():
    '''
    Main function to read input strings and check for subsequence.
    '''
    s = input("Please enter a non-empty string s: ")
    t = input("Please enter a non-empty string t: ")
    if not s or not t:
        print("Both strings must be non-empty.")
        return
    result = is_subsequence(s, t)
    if result is not None:
        print(f"Minimum copies of s needed: {result}")
    else:
        print("No valid i exists.")
if __name__ == "__main__":
    main()