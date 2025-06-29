import tkinter as tk
from subtask import generate_random_number, check_guess
def check_input(entry, result_label, remaining_lives_label):
    global remaining_lives, target_number
    user_input = entry.get()
    entry.delete(0, tk.END)  # Clear the input field
    # Validate user input
    if not user_input.isdigit() or len(user_input) != 3 or len(set(user_input)) != 3:
        result_label.config(text="Invalid input. Please enter a three-digit number with different digits.")
        return
    result = check_guess(user_input, target_number)
    result_label.config(text=f"Hits: {result['hits']}, Blows: {result['blows']}")
    if result['hits'] == 3:
        result_label.config(text="Congratulations! You guessed the number correctly.")
        entry.config(state=tk.DISABLED)  # Disable input field
        check_button.config(state=tk.DISABLED)  # Disable check button
    else:
        remaining_lives -= 1
        remaining_lives_label.config(text=f"Remaining lives: {remaining_lives}")
        if remaining_lives == 0:
            result_label.config(text=f"Game over. The correct number was {target_number}.")
            entry.config(state=tk.DISABLED)  # Disable input field
            check_button.config(state=tk.DISABLED)  # Disable check button
def play_game():
    global target_number, remaining_lives
    target_number = generate_random_number()
    remaining_lives = 7
    window = tk.Tk()
    window.title("Hit and Blow Game")
    instruction_label = tk.Label(window, text="Enter a three-digit number:")
    instruction_label.pack()
    entry = tk.Entry(window)
    entry.pack()
    check_button = tk.Button(window, text="Check", command=lambda: check_input(entry, result_label, remaining_lives_label))
    check_button.pack()
    result_label = tk.Label(window, text="")
    result_label.pack()
    remaining_lives_label = tk.Label(window, text=f"Remaining lives: {remaining_lives}")
    remaining_lives_label.pack()
    window.mainloop()
if __name__ == "__main__":
    play_game()