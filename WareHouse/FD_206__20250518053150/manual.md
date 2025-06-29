Here's a detailed user manual for the Interval Game application, formatted in Markdown:

```markdown
# Interval Game

A fun and strategic game where players Alice and Bob take turns selecting non-overlapping intervals to determine the winner based on optimal play.

## Quick Install

To run the Interval Game application, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install typing
```

## 🤔 What is this?

The Interval Game allows two players, Alice and Bob, to compete by selecting intervals from a given set. The game is played optimally, meaning both players will make the best possible moves to win. The player who selects the last interval wins the game.

### Main Functions

1. **`determine_winner(T: int, intervals: List[Tuple[int, int]]) -> List[str]`**: 
   - This function processes multiple test cases and determines the winner for each based on the provided intervals.
   - **Parameters**:
     - `T`: The number of test cases.
     - `intervals`: A list of lists containing tuples that represent half-open intervals.
   - **Returns**: A list of strings indicating the winner for each test case.

2. **`is_non_intersecting(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> bool`**:
   - Checks if two intervals do not intersect.
   - **Parameters**:
     - `interval1`: The first interval as a tuple.
     - `interval2`: The second interval as a tuple.
   - **Returns**: `True` if the intervals do not intersect, otherwise `False`.

3. **`find_winner(intervals: List[Tuple[int, int]]) -> str`**:
   - Determines the winner based on the optimal play strategy for Alice and Bob.
   - **Parameters**:
     - `intervals`: A list of tuples representing the intervals.
   - **Returns**: A string indicating the winner ("Alice" or "Bob").

## 📖 How to Use/Play

1. **Run the Application**:
   - Execute the `main.py` file in your terminal or command prompt:
   ```bash
   python main.py
   ```

2. **Input Format**:
   - When prompted, enter your test cases in the following format:
     - Each test case consists of intervals separated by semicolons (`;`).
     - Multiple test cases are separated by a pipe (`|`).
   - Example input:
     ```
     1,2;3,4 | 5,6;7,8
     ```
   - This input represents two test cases:
     - Test Case 1: Intervals [1, 2) and [3, 4)
     - Test Case 2: Intervals [5, 6) and [7, 8)

3. **Output**:
   - The application will output the winner for each test case based on the intervals provided.
   - Example output:
     ```
     Alice
     Bob
     ```

## ⚠️ Error Handling

- If you enter an invalid interval (where L >= R), the application will raise a `ValueError` and prompt you to enter valid intervals.
- If no intervals are provided, the application will indicate that there are no intervals to process.

## Conclusion

The Interval Game is a strategic and engaging way to test your decision-making skills. Enjoy playing against your friends or challenge yourself to see how many intervals you can optimally select!

For further assistance or inquiries, please contact our support team.
```

This manual provides a comprehensive overview of the Interval Game application, including installation instructions, main functions, usage guidelines, and error handling.