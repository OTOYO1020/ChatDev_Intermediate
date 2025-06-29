Here is the `manual.md` file that provides a detailed user manual for the Survivor Game application, including installation instructions, main functions, and usage guidelines.

```markdown
# Survivor Game

Welcome to the Survivor Game application! This software allows you to simulate a game where players answer questions and compete to survive based on their scores.

## Main Functions

The Survivor Game application consists of the following main functions:

- **determine_survivors(N: int, K: int, Q: int, A: List[int]) -> List[int]**: This function determines the indices of players who have scores greater than 0 after processing the answers. It initializes scores for all players, decrements scores for players who did not answer correctly, and returns the list of surviving players.

- **main()**: The entry point of the application that handles user input, validates it, and displays the results.

- **display_results(survivors: List[int])**: This function formats and prints the indices of surviving players in ascending order.

## Quick Install

To run the Survivor Game application, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install typing
```

## 🤔 What is this?

The Survivor Game is a fun and interactive application where players answer questions, and based on their performance, they either survive or get eliminated. Each player starts with a score, and for each correct answer, the scores of all other players are decremented. The goal is to see who can survive the longest!

## How to Use/Play the Game

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Format**: When prompted, enter the values for N (number of players), K (initial score), Q (number of answers), and the list of answers (indices of players who answered correctly) in a comma-separated format. For example:

   ```
   Enter N, K, Q and answers (comma-separated): 5, 3, 3, 0, 1, 2
   ```

   In this example:
   - There are 5 players.
   - Each player starts with a score of 3.
   - There are 3 answers, and players at indices 0, 1, and 2 answered correctly.

3. **View Results**: After entering the input, the application will process the answers and display the indices of surviving players. For example:

   ```
   Survivors: 3, 4
   ```

   If no players survive, it will display:

   ```
   No survivors.
   ```

## Edge Cases

- The application validates the input to ensure that the number of answers matches Q and that all answers are valid indices between 0 and N-1.
- If all players are eliminated, the application will inform you that there are no survivors.

## Testing

The application has been tested with various test cases to ensure correctness and performance within the given constraints. You can modify the input values to test different scenarios.

## Conclusion

Enjoy playing the Survivor Game! Feel free to reach out if you have any questions or need further assistance.
```

This manual provides a comprehensive overview of the Survivor Game application, ensuring users understand how to install, run, and interact with the software effectively.