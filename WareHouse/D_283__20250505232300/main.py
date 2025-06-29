'''
Main application file for the parentheses and letter validation program.
'''
def check_parentheses_and_letters(S):
    '''
    Checks if the string S has valid parentheses and letters.
    '''
    box = set()
    stack = []  # Stack to keep track of indices of '('
    added_letters_stack = []  # Stack to track sets of letters added after each '('
    for i in range(len(S)):
        if S[i].islower():
            if S[i] in box:
                return "NO"
            box.add(S[i])
            # Track letters added after the last '('
            if added_letters_stack:
                added_letters_stack[-1].add(S[i])  # Add to the last set corresponding to the last '('
        elif S[i] == '(':
            stack.append(i)  # Push index of '(' onto the stack
            added_letters_stack.append(set())  # Push a new set for this '('
        elif S[i] == ')':
            if not stack:  # If stack is empty, there's no matching '('
                return "NO"
            j = stack.pop()  # Pop the last '(' index
            letters_to_remove = added_letters_stack.pop()  # Pop the last set
            # Check if the substring S[j:i] is valid
            if not is_good_string(S[j:i + 1]):
                return "NO"
            # Remove letters added after the last '('
            for letter in letters_to_remove:
                box.discard(letter)
    # After processing all characters, check if there are unmatched '('
    if stack:
        return "NO"
    return "YES"
def is_good_string(substring):
    '''
    Checks if the substring is a good string, meaning it contains balanced parentheses.
    '''
    balance = 0
    for char in substring:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:  # More ')' than '(' at any point
            return False
    return balance == 0  # Must be balanced at the end
def validate_input(input_string):
    '''
    Validates the input string to ensure it consists only of lowercase letters and parentheses.
    '''
    return all(c.islower() or c in '()' for c in input_string)
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    if not validate_input(input_string):
        print("Invalid input. Please enter only lowercase letters and parentheses.")
    else:
        result = check_parentheses_and_letters(input_string)
        print(result)