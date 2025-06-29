'''
Main application file for the String Matcher.
'''
from string_matcher import can_match
def main():
    '''
    Main function to handle input and output for string matching.
    '''
    S = input("Enter String S: ")
    T = input("Enter String T: ")
    if can_match(S, T):
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()