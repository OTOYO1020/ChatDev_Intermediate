Here's the `manual.md` file that provides a detailed user manual for the software developed to handle the task assigned by the new customer:

```markdown
# Submission Processing Application

This application processes programming contest submissions, tracks penalties for incorrect submissions, and provides a summary of correct answers and total penalties.

## Main Functions

- **Submission Validation**: Validates the problem index and verdict for each submission.
- **Penalty Tracking**: Keeps track of the number of 'Wrong Answers' (WA) for each problem until a 'Correct Answer' (AC) is received.
- **Result Calculation**: Calculates the total number of correct answers and the total penalties incurred for those problems.

## Installation Instructions

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Use the following command to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Note: The `requirements.txt` file is currently empty, but you can add any future dependencies as needed.

## How to Use the Application

1. **Input Format**:
   The application expects input in the following format:
   - The first line should contain two integers, N (number of problems) and M (number of submissions).
   - The next M lines should each contain a submission in the format: `p_i S_i`, where `p_i` is the problem index (1 to N) and `S_i` is the verdict ('WA' or 'AC').

   Example Input:
   ```
   3 5
   1 WA
   2 WA
   1 AC
   3 WA
   2 AC
   ```

2. **Running the Application**:
   You can run the application by executing the following command in your terminal:
   ```bash
   python main.py
   ```

   The application will read from standard input, so you can either type the input directly or redirect from a file:
   ```bash
   python main.py < input.txt
   ```

3. **Output**:
   The application will output two integers:
   - The number of correct answers.
   - The total penalties incurred for those correct answers.

   Example Output:
   ```
   2 2
   ```

## Error Handling

The application includes validation checks for submissions. If an error is found (e.g., invalid problem index or verdict), an error message will be printed, and that submission will be skipped.

## Future Enhancements

The application is designed to be extensible. If you anticipate needing libraries for data manipulation or numerical operations in the future, you can add them to the `requirements.txt` file as comments for easy reference.

## Support

For any issues or feature requests, please contact the development team at [support@chatdev.com](mailto:support@chatdev.com).

```

This manual provides a comprehensive overview of the software, including its main functions, installation instructions, usage guidelines, and support information. It is structured to be user-friendly and informative for anyone looking to use the application.