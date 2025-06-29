'''
Main application file for the Adventure Potion Management without GUI.
'''
from typing import List, Tuple  # Added imports for type hinting
from adventure_logic import adventure
def main():
    try:
        N = int(input("Enter number of events: "))
        events_input = input("Enter events (format: t_i x_i, separated by commas): ").strip().split(',')
        events = [tuple(map(int, event.split())) for event in events_input]
        if len(events) != N:
            raise ValueError("Number of events does not match the input count.")
        K_min, actions = adventure(N, events)
        display_result(K_min, actions)
    except Exception as e:
        print(f"Input Error: {e}")
def display_result(K_min, actions):
    if K_min == -1:
        print("Result: -1")
    else:
        actions_str = ', '.join(actions)
        print(f"Result: K_min = {K_min}, Actions: {actions_str}")
if __name__ == "__main__":
    main()