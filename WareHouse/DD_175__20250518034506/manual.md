Here's the `manual.md` file for the Score Game application, detailing its main functions, installation instructions, and usage guidelines.

```markdown
# Score Game

Welcome to the Score Game application! This software allows users to calculate the maximum score achievable based on a series of squares, each with its own score, and a permutation of moves.

## Main Functions

The Score Game application includes the following key functionalities:

- **Calculate Maximum Score**: The core function `max_score(N: int, K: int, C: List[int], P: List[int])` computes the maximum score based on:
  - `N`: The number of squares.
  - `K`: The maximum number of moves allowed.
  - `C`: A list of scores associated with each square.
  - `P`: A permutation of the squares indicating the movement path.

- **User Input**: The application prompts users to input the number of squares, maximum moves, scores on squares, and the permutation of squares.

- **Cycle Detection**: The application intelligently detects cycles in the movement path to maximize score calculation.

## Installation

To run the Score Game application, you need to set up your Python environment and install the necessary dependencies. Follow these steps:

1. **Install Python**: Ensure you have Python 3.6 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv score_game_env
   source score_game_env/bin/activate  # On Windows use `score_game_env\Scripts\activate`
   ```

3. **Install Dependencies**: The application requires no external libraries beyond Python's standard library. Simply ensure you have the `typing` module available (included in Python 3.5+).

## How to Use/Play

1. **Run the Application**: Execute the main application file to start the Score Game.
   ```bash
   python main.py
   ```

2. **Input Parameters**: When prompted, enter the following:
   - **Number of Squares (N)**: An integer representing how many squares are in the game.
   - **Maximum Moves (K)**: An integer indicating the maximum number of moves you can make.
   - **Scores on Squares (C)**: A comma-separated list of integers representing the scores for each square.
   - **Permutation of Squares (P)**: A comma-separated list of integers representing the order of squares you can move to.

   Example Input:
   ```
   Number of Squares (N): 5
   Maximum Moves (K): 10
   Scores on Squares (C) (comma-separated): 1,2,3,4,5
   Permutation of Squares (P) (comma-separated): 2,3,1,5,4
   ```

3. **View Results**: After entering the parameters, the application will compute and display the maximum score achievable based on your inputs.

## Example

Here’s a quick example of how to use the application:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input the following when prompted:
   ```
   Number of Squares (N): 4
   Maximum Moves (K): 5
   Scores on Squares (C) (comma-separated): 10,20,30,40
   Permutation of Squares (P) (comma-separated): 2,3,4,1
   ```

3. The application will output:
   ```
   Maximum Score: 100
   ```

## Conclusion

The Score Game application is a fun and engaging way to explore permutations and scoring strategies. We hope you enjoy using it! For any issues or feedback, please reach out to our support team.
```

This manual provides a comprehensive overview of the Score Game application, ensuring users have all the information they need to install and use the software effectively.