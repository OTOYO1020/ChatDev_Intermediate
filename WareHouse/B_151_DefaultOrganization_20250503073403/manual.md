Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Score Calculator Application

A simple application to calculate the minimum score needed on the final subject to achieve a desired average score across multiple subjects.

## Main Functions

The Score Calculator Application performs the following main functions:

1. **Input Reading**: Reads integers N (number of subjects), K (maximum score for any subject), and M (desired average score) from standard input.
2. **Score Calculation**: Calculates the total score required to achieve the average of M points over N subjects and determines the minimum score needed on the final subject.
3. **Validation**: Validates the input values to ensure they are within specified constraints.
4. **Output**: Prints the minimum score needed on the final subject or an error message if the goal is unachievable.

## Installation

To run the Score Calculator Application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application does not have any external dependencies beyond the standard Python library. Ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: Clone the repository containing the application files to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file `main.py` using Python.

   ```bash
   python main.py
   ```

3. **Input Format**: When prompted, enter the values for N, K, and M, followed by the scores for the first N-1 subjects. The input should be provided in the following format:

   ```
   N K M
   score1 score2 score3 ... score(N-1)
   ```

   For example:
   ```
   5 10 7
   6 8 5 9
   ```

4. **Output**: The application will output the minimum score needed on the final subject or `-1` if the goal is unachievable.

## Example Usage

### Input
```
5 10 7
6 8 5 9
```

### Output
```
-1
```

### Explanation
In this example, the required total score to achieve an average of 7 over 5 subjects is 35. The current total score from the first 4 subjects is 28. The needed score on the final subject is 35 - 28 = 7, which is within the valid range [0, 10].

## Error Handling

The application includes input validation to ensure that:

- N is between 1 and 100.
- K and M are between 0 and 100.
- The number of scores provided matches N-1.
- Each score is within the range [0, K].

If any of these conditions are not met, an appropriate error message will be displayed.

## Conclusion

The Score Calculator Application is a straightforward tool for calculating the minimum score needed on the final subject to achieve a desired average. By following the installation and usage instructions, users can easily run the application and obtain results based on their input.
```

This manual provides a comprehensive overview of the Score Calculator Application, including its main functions, installation instructions, usage guidelines, and error handling.