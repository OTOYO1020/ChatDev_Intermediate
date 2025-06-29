'''
Main application file for the string transformation using standard input and output.
'''
from operations import f
def main():
    S = input("Enter a string (format: character followed by digit): ")
    # Updated input validation to ensure correct formatting
    if len(S) < 2 or len(S) % 2 != 0 or any(not (S[i].isalpha() and S[i + 1].isdigit()) for i in range(0, len(S) - 1, 2)):
        print("Input string must have an even length with characters followed by digits.")
        return
    operations = 0
    previous_S = ""
    while len(S) > 1:
        if S == previous_S:
            print("-1")
            return
        previous_S = S
        try:
            S = f(S)
            if S == "":
                print("-1")
                return
        except ValueError as e:
            print(e)
            return
        operations += 1
    print(f"Result: {S}\nOperations: {operations % 998244353}")
if __name__ == "__main__":
    main()