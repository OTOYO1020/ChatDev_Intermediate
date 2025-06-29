'''
Main application file for the Taro's travel distance calculator.
'''
from input_handler import InputHandler
from output_display import OutputDisplay
def main():
    input_handler = InputHandler()
    output_display = OutputDisplay()
    n, k, friends = input_handler.get_input()
    input_handler.validate_input(n, k, friends)  # Validate input before processing
    last_village = process_friends(n, k, friends)
    output_display.show_output(last_village)  # Use OutputDisplay to show output
def process_friends(n, k, friends):
    current_village = 0
    current_money = k
    friends.sort(key=lambda x: x[0])  # Sort based on the village number A_i
    for a, b in friends:
        distance = abs(a - current_village)  # Calculate distance to the friend's village
        if current_money >= distance:  # Check if Taro can reach the village
            current_money -= distance  # Deduct the cost of travel
            current_money += b  # Add the yen received from the friend
            current_village = a  # Update current village to the friend's village
        else:
            break  # Exit the loop if Taro cannot reach the next village
    # Calculate the last village Taro can reach with remaining money
    last_village_reached = current_village + current_money
    return last_village_reached  # Return the last village Taro can reach
if __name__ == "__main__":
    main()