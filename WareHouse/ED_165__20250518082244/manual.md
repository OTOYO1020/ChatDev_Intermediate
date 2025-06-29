Here's the user manual for the software, formatted in Markdown as requested:

```markdown
# Playing Fields Assignment

A Python application designed to handle the assignment of integers to playing fields for competitive scenarios.

## Main Functions

The main functionality of this software includes:

- **assign_playing_fields(N: int, M: int) -> List[Tuple[int, int]]**: This function assigns pairs of distinct integers to playing fields. It ensures that no player fights the same opponent more than once and wraps player integers around when they exceed the total number of players.

## Quick Install

To set up the environment and install the necessary dependencies, you can use pip:

```bash
pip install typing
```

## 🤔 What is this?

This application is designed to facilitate the assignment of players to fields in a competitive setting. It ensures that:

- Each playing field has two distinct players.
- Players do not fight the same opponent more than once.
- Player integers wrap around after reaching the maximum number of players.

## How to Use

1. **Run the Application**: Execute the `main.py` file in your Python environment.

   ```bash
   python main.py
   ```

2. **Input Parameters**: When prompted, enter the total number of players (N) and the number of fields (M). Ensure that the constraint `M * 2 + 1 <= N` is satisfied.

3. **View Assignments**: The application will output pairs of integers representing the players assigned to each playing field, with each pair printed on a new line.

### Example Usage

- If you have 6 players and want to assign them to 2 fields, you would input:

   ```
   Enter N (total players): 6
   Enter M (number of fields): 2
   ```

- The output might look like:

   ```
   1 2
   3 4
   ```

## 📖 Documentation

For more detailed information on the functions and their usage, please refer to the code comments within `utils.py` and `main.py`.

### Error Handling

- If the constraint `M * 2 + 1 > N` is violated, the application will raise a `ValueError` and inform the user of the input error.

### Testing

You can test the function with various values of N and M to ensure correctness and adherence to the problem constraints.

## Conclusion

This application provides a robust solution for assigning players to fields in a competitive environment, ensuring fairness and compliance with the specified rules.
```

This manual provides a comprehensive overview of the software, including installation instructions, usage guidelines, and error handling. It should help users effectively utilize the application for their needs.