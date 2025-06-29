'''
Main application file for the potion tracking adventure.
'''
from event import Event
from potion_tracker import PotionTracker
def main():
    N = int(input("Enter the number of events: "))
    events = []
    potion_tracker = PotionTracker()
    for _ in range(N):
        t, x = map(int, input("Enter event (t x): ").split())
        events.append(Event(t, x))
    failure_flag = False
    actions = []  # To track actions taken by Takahashi
    K_min = float('inf')  # Initialize K_min to infinity
    actions_at_K_min = []  # To track actions taken when K_min is updated
    for event in events:
        if event.t == 1:
            potion_tracker.add_potion(event.x)
            actions.append(f"Added potion type {event.x}")
        elif event.t == 2:
            if potion_tracker.remove_potion(event.x):
                actions.append(f"Removed potion type {event.x}")
            else:
                failure_flag = True
                break
        # Update current_potions and K_min after processing each event
        current_potions = potion_tracker.get_current_potions()
        if current_potions <= K_min:  # Change from < to <=
            K_min = current_potions
            actions_at_K_min = actions.copy()  # Store actions when K_min is updated
    # After processing all events
    if failure_flag:
        print(-1)
    else:
        print(f"Minimum maximum potions needed: {K_min}")
        print("Actions taken by Takahashi:")
        for action in actions_at_K_min:  # Use actions_at_K_min instead of actions
            print(action)
if __name__ == "__main__":
    main()