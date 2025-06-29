Here's a detailed user manual for the expected wins calculator software, formatted in Markdown as requested:

```markdown
# Expected Wins Calculator

A Python application for calculating the expected number of wins for players based on match results.

## Quick Install

To run the Expected Wins Calculator, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install typing
```

## 🤔 What is this?

The Expected Wins Calculator is designed to compute the expected wins for a set of players based on the results of matches between them. This application utilizes a union-find algorithm to efficiently manage team sizes and calculate probabilities of winning based on team compositions.

### Main Functions

1. **Input Handling**: The application accepts input for the number of players and their match results.
2. **Expected Wins Calculation**: The core function `calculate_expected_wins(N: int, matches: List[Tuple[int, int]]) -> List[int]` computes the expected wins for each player based on the matches provided.
3. **Modular Arithmetic**: The results are returned in a format that uses modular arithmetic to ensure they fit within specified limits.

## How to Use

1. **Run the Application**: Execute the `main.py` file in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Format**: When prompted, enter the number of players followed by pairs of matches. The format should be:

   ```
   N
   p1 q1
   p2 q2
   ...
   ```

   Where `N` is the total number of players, and each pair `p_i q_i` represents a match between player `p_i` and player `q_i`.

   **Example Input**:
   ```
   4
   1 2
   2 3
   1 3
   ```

3. **View Results**: After entering the input, the application will output the expected wins for each player.

## Example

To illustrate how to use the application, consider the following example:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input the following data when prompted:
   ```
   3
   1 2
   2 3
   ```

3. The output will display the expected wins for each player based on the matches provided.

## 📖 Documentation

For more detailed information on the implementation, please refer to the source code in `calculations.py` and `main.py`. The main logic for calculating expected wins is encapsulated in the `calculate_expected_wins` function.

### Key Components

- **Union-Find Structure**: Used to manage team memberships and sizes efficiently.
- **Probability Calculation**: Winning probabilities are calculated using the sizes of the teams involved in each match.
- **Modular Inverse**: Ensures that results are returned in a manageable format using modulo `998244353`.

## Conclusion

The Expected Wins Calculator is a powerful tool for analyzing match outcomes and predicting player performance based on team dynamics. By following the instructions above, users can easily set up and utilize the application for their needs.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and a brief explanation of its functionality.