'''
Main application file for the String Modifier application.
'''
from string_modifier import StringModifier
def main():
    # Read the integer values N and Q from standard input
    n = int(input())
    s = input()
    q = int(input())
    if len(s) != n:
        raise ValueError("Length of string S must be equal to N.")
    operations = []
    for _ in range(q):
        operation = input().strip()
        c_i, d_i = operation.split(',')
        if len(c_i.strip()) != 1 or len(d_i.strip()) != 1:
            raise ValueError("Both c_i and d_i must be single characters.")
        operations.append((c_i.strip(), d_i.strip()))
    modified_string = modify_string(s, operations)
    print(modified_string)
def modify_string(s, operations):
    '''
    Perform the character replacements on the string S.
    '''
    modifier = StringModifier(s)
    for c_i, d_i in operations:
        modifier.replace_character(c_i, d_i)
    return modifier.get_modified_string()
if __name__ == "__main__":
    main()