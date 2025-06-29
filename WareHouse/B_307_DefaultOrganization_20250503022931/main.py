'''
Main application file for the Palindrome Checker.
'''
from palindrome_checker import is_palindrome
def main():
    n = int(input())  # Read number of strings from standard input
    strings = []
    for i in range(n):
        string = input()  # Read each string from standard input
        strings.append(string)
    found_palindrome = False
    for i in range(n):
        for j in range(i + 1, n):  # Start j from i + 1 to avoid checking the same pair twice
            concat_str1 = strings[i] + strings[j]  # Concatenate strings
            concat_str2 = strings[j] + strings[i]  # Also check the reverse concatenation
            if is_palindrome(concat_str1) or is_palindrome(concat_str2):
                found_palindrome = True
                break
        if found_palindrome:
            break
    if found_palindrome:
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()