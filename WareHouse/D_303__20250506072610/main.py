'''
Main application file that initializes the application and handles user interactions.
'''
def calculate_time(X, Y, Z, S):
    total_time = 0
    caps_lock_on = False
    for char in S:
        if char == 'a':
            if caps_lock_on:
                total_time += Y  # Cost for pressing 'a' with Shift
            else:
                total_time += X  # Cost for pressing 'a'
        elif char == 'A':
            if not caps_lock_on:
                total_time += Z  # Cost for turning Caps Lock on
                caps_lock_on = True  # Activate Caps Lock
            total_time += Y  # Cost for pressing 'A' (when Caps Lock is off or on)
    if caps_lock_on:
        total_time += Z  # Cost for turning Caps Lock off
    return total_time
if __name__ == "__main__":
    import sys
    X, Y, Z = map(int, sys.stdin.readline().split())
    S = sys.stdin.readline().strip()
    total_time = calculate_time(X, Y, Z, S)
    print(total_time)