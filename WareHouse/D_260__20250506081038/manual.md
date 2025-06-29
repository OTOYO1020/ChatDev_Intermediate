Here's a detailed user manual for the card game software, formatted in Markdown as requested:

```markdown
# Card Game Application

A fun and interactive card game application that allows users to simulate a card stacking game based on permutations.

## Main Functions

- **Input Handling**: Users can input the number of cards (N), the number of cards to be eaten (K), and the permutation of cards (P).
- **Game Logic**: The application processes the card stacking game according to the defined rules, tracking which cards are eaten and when.
- **Output Display**: Results are displayed in a user-friendly interface, showing the move in which each card was eaten or indicating if it was never eaten.

## Installation

To run the Card Game Application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open your terminal or command prompt and run the following command to install the required libraries:
   ```bash
   pip install tkinter
   ```

## How to Use/Play the Game

1. **Run the Application**: Navigate to the directory where the `main.py` file is located and run the following command:
   ```bash
   python main.py
   ```

2. **Input Values**:
   - **Enter N**: Input the total number of cards.
   - **Enter K**: Input the number of cards to be eaten at once.
   - **Enter Permutation P**: Input the permutation of cards as a comma-separated list (e.g., `3,1,2`).

3. **Submit**: Click the "Submit" button to start the game. The application will process the input and display the results.

4. **View Results**: The results will be displayed in the output frame, indicating the move in which each card was eaten or if it was never eaten.

## Example

- If you input:
  - N: `5`
  - K: `2`
  - P: `5,3,1,4,2`
  
  The output might look like:
  ```
  [0, 1, -1, 2, -1]
  ```
  This indicates that the first card was eaten in move 0, the second card in move 1, and the fourth card in move 2, while the third and fifth cards were never eaten.

## Troubleshooting

- **Invalid Input**: If you enter invalid values (e.g., K greater than N, or P not being a valid permutation), the application will print an error message in the console.
- **No Output**: Ensure that you have entered all required values correctly and that the application is running without errors.

## Conclusion

Enjoy playing the card game and explore the logic behind card stacking! For any further questions or issues, feel free to reach out for support.
```

This manual provides a comprehensive overview of the card game application, including its main functions, installation instructions, usage guidelines, and troubleshooting tips.