Here's a detailed user manual for the Adventure Potion Management application, formatted in Markdown as requested:

```markdown
# Adventure Potion Management

Manage your potions and defeat monsters in this exciting adventure game!

## Overview

The Adventure Potion Management application allows users to simulate an adventure where Takahashi collects potions and battles monsters. Users can input a series of events that dictate the actions Takahashi can take, and the application will determine if he can defeat all monsters while managing his potions effectively.

## Main Functions

- **Collect Potions**: Takahashi can collect potions of different types during the adventure.
- **Defeat Monsters**: Takahashi can attempt to defeat monsters using the potions he has collected.
- **Track Potions**: The application keeps track of the number of potions collected and the minimum number of potions required to defeat all monsters.
- **Output Results**: The application will output either the minimum number of potions required to survive or indicate failure if Takahashi cannot defeat all monsters.

## Installation

To run the Adventure Potion Management application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application code.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Required Dependencies**: Use pip to install the necessary dependencies.
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**: Execute the main application file.
   ```bash
   python main.py
   ```

2. **Input Events**: When prompted, enter the number of events followed by the events themselves in the specified format. For example:
   ```
   Enter number of events: 5
   Enter events (format: t_i x_i, separated by commas): 1 1, 1 2, 2 1, 1 1, 2 2
   ```

   - **Event Format**:
     - `t_i = 1`: Collect a potion of type `x_i`.
     - `t_i = 2`: Attempt to defeat a monster that requires a potion of type `x_i`.

3. **View Results**: After processing the events, the application will display the result, indicating either the minimum number of potions required or a failure message.

## Example

Here’s an example of how to interact with the application:

```
Enter number of events: 4
Enter events (format: t_i x_i, separated by commas): 1 1, 1 2, 2 1, 2 2
Result: K_min = 1, Actions: Collected potion 1, Collected potion 2, Defeated monster with potion 1, Defeated monster with potion 2
```

## Edge Cases

- If all events are of one type (e.g., only collecting potions), the application will handle this gracefully.
- If no potions are collected and there are monster defeat events, the application will return `-1`.

## Conclusion

The Adventure Potion Management application provides an engaging way to manage potions and defeat monsters. Follow the instructions above to set up and play the game. Enjoy your adventure!
```

This manual provides a comprehensive guide for users to understand the application, install it, and use it effectively. Let me know if you need any further modifications or additional information!