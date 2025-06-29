'''
Main application file for the string comparison application.
'''
from string_comparison import StringComparison
def main():
    S = input("Enter String S: ")
    T = input("Enter String T: ")
    # Input validation
    if not S or not T:
        print("Both strings must be non-empty.")
        return
    if len(T) > len(S):
        print("String T must not be longer than String S.")
        return
    min_changes = StringComparison.calculate_min_changes(S, T)
    print(f"Minimum Changes: {min_changes}")
if __name__ == "__main__":
    main()