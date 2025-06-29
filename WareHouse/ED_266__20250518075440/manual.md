Here's a detailed user manual for the die throwing game application, formatted in Markdown as requested:

```markdown
# Die Throwing Game

Welcome to the Die Throwing Game! This application allows users to simulate a game where they can throw a die for a specified number of turns and calculate the expected score based on their decisions.

## Main Functions

- **simulate_die_throw()**: Simulates a die throw, returning a random integer between 1 and 6.
- **expected_score(N: int) -> float**: Calculates the expected score based on the number of turns (N) provided by the user. It determines whether to continue the game or end it based on the expected scores calculated for each turn.

## Quick Install

To run the Die Throwing Game, you need to have Python installed on your system. You can install the required dependencies using pip. Open your terminal or command prompt and run:

```bash
pip install random
```

(Note: The `random` module is part of Python's standard library, so no additional installation is required for it.)

## How to Use/Play the Game

1. **Run the Application**: 
   - Navigate to the directory where the `main.py` file is located.
   - Execute the following command in your terminal or command prompt:
   ```bash
   python main.py
   ```

2. **Input Number of Turns**:
   - When prompted, enter the number of turns you wish to play. The number must be at least 1.
   - Example input: `3`

3. **View Expected Score**:
   - After entering the number of turns, the application will calculate and display the expected score based on your input.
   - Example output: `Expected Score: 4.50`

## Game Logic

- The game simulates throwing a die for the specified number of turns.
- For each turn, the application calculates the expected score if the game continues versus if it ends, using the current die throw value.
- The expected scores for each turn are stored in a list to track the maximum expected value.
- If the number of turns is 1, the expected score is directly returned from the die throw.

## Example Usage

1. Start the game:
   ```bash
   python main.py
   ```

2. Enter the number of turns:
   ```
   Enter number of turns: 3
   ```

3. View the expected score:
   ```
   Expected Score: 4.50
   ```

## Conclusion

The Die Throwing Game is a fun and interactive way to explore probability and decision-making based on random events. Enjoy playing and experimenting with different numbers of turns to see how the expected score changes!

For any further questions or support, feel free to reach out to our support team.
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, and usage guidelines. Let me know if you need any further modifications or additional information!