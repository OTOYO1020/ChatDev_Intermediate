'''
Main application file for the subsequence checker.
'''
from utils import is_subsequence, find_minimum_i
def main():
    s = input("Enter string s: ")
    t = input("Enter string t: ")
    min_i = find_minimum_i(s, t)
    if min_i == -1:
        print("No valid i found.")
    else:
        print(f"The minimum i is: {min_i}")
if __name__ == "__main__":
    main()