Here's a detailed user manual for the stair climbing application, formatted in Markdown as requested:

```markdown
# Stair Climbing Ways Calculator

This application calculates the number of ways to climb a staircase with a given number of steps, accounting for broken steps that cannot be used.

## Main Functions

- **Input Handling**: The application reads the total number of steps (N) and the number of broken steps (M) from the user. It also accepts a list of broken steps.
- **Dynamic Programming Logic**: The application uses dynamic programming to compute the number of ways to reach the N-th step while avoiding broken steps.
- **Output**: The result is displayed, showing the number of ways to climb the stairs modulo `1,000,000,007`.

## Installation

To run the application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

Currently, there are no external dependencies required for this application. However, if you plan to extend its functionality in the future, you may want to include additional libraries.

## How to Use the Application

### Running from Command Line

1. **Clone the Repository**: If you have the application code in a repository, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file.
   ```bash
   python main.py
   ```

3. **Input Data**: Follow the prompts to enter:
   - The total number of steps (N).
   - The number of broken steps (M).
   - A list of broken steps (comma-separated if using GUI).

4. **View Results**: After entering the data, the application will calculate and display the number of ways to climb the stairs.

### Running the GUI

1. **Run the GUI Application**: Execute the GUI file.
   ```bash
   python gui.py
   ```

2. **Input Data**: Fill in the fields for:
   - Number of steps (N).
   - Number of broken steps (M).
   - Broken steps (comma-separated).

3. **Calculate**: Click the "Calculate Ways" button to compute the result.

4. **View Results**: The result will be displayed below the button indicating the number of ways to climb the stairs.

## Example Usage

1. **Command Line Example**:
   ```
   Input:
   5 2
   2 4

   Output:
   Ways to climb: 3
   ```

2. **GUI Example**:
   - Enter `5` for N.
   - Enter `2` for M.
   - Enter `2,4` for broken steps.
   - Click "Calculate Ways".
   - Result: "Ways to climb: 3".

## Error Handling

The application includes error handling for the following scenarios:
- Non-negative integers for N and M.
- The number of broken steps must match M.
- Broken steps must be within the range from 0 to N.

If any input is invalid, an error message will be displayed.

## Conclusion

This application provides a simple yet effective way to calculate the number of ways to climb stairs while avoiding broken steps. It can be easily extended or modified to include additional features or functionalities as needed.
```

This manual provides a comprehensive overview of the application, including its functions, installation instructions, usage guidelines, and error handling. It should serve as a useful resource for users looking to understand and utilize the stair climbing application effectively.