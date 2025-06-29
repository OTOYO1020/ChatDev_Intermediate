'''
Module containing the logic for calculating the minimum time to type a given string.
'''
def min_time_to_type(S: str, X: int, Y: int, Z: int) -> int:
    total_time = 0
    caps_lock_on = False  # Initialize Caps Lock state as off
    for char in S:
        if char == 'A':
            if not caps_lock_on:
                time_shift_a = Y + Z  # Time for Shift + 'A' and toggling Caps Lock
                time_caps_a = X + Z  # Time for toggling Caps Lock then pressing 'A'
                if time_shift_a < time_caps_a:
                    total_time += time_shift_a
                    caps_lock_on = True  # Toggle Caps Lock on
                else:
                    total_time += time_caps_a
                    # Keep Caps Lock off
            else:
                total_time += X  # Just press 'A'
        elif char == 'a':
            if not caps_lock_on:
                total_time += X  # Just press 'a'
            else:
                time_shift_a = Y  # Time for Shift + 'a'
                time_toggle = Z + X  # Time for toggling Caps Lock then pressing 'a'
                if time_shift_a < time_toggle:
                    total_time += time_shift_a  # Press Shift + 'a'
                else:
                    total_time += time_toggle  # Toggle Caps Lock and press 'a'
                    caps_lock_on = False  # Toggle Caps Lock off
    return total_time