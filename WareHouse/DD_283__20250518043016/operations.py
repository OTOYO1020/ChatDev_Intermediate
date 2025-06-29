'''
Contains the logic to check if Takahashi can complete the operations.
'''
def can_complete_operations(S: str) -> bool:
    box = set()
    added_balls = []  # List to keep track of added balls and their indices
    stack = []  # Stack to keep track of indices of '('
    def is_good_string(sub: str) -> bool:
        filtered_sub = ''.join([char for char in sub if not char.islower()])
        while '()' in filtered_sub:
            filtered_sub = filtered_sub.replace('()', '')
        return len(filtered_sub) == 0
    for i in range(len(S)):
        if S[i].islower():
            if S[i] in box:
                return False
            box.add(S[i])
            added_balls.append((S[i], i))  # Track the added ball with its index
        elif S[i] == '(':
            stack.append(len(added_balls))  # Push the count of added balls onto the stack
        elif S[i] == ')':
            if not stack:  # No matching '(' found
                return False
            last_added_count = stack.pop()  # Get the count of added balls at the last '('
            if is_good_string(S[last_added_count:i + 1]):
                # Remove balls from box that were added in operations between last '(' and current ')'
                for ball, index in added_balls[last_added_count:]:
                    box.remove(ball)
                added_balls = added_balls[:last_added_count]  # Keep only the balls added before the last '('
            else:
                return False  # If the string is not good, return False
    return True