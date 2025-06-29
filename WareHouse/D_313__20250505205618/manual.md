Here's a detailed user manual for the software based on the provided code and requirements:

```markdown
# Query Sequence Solver

A Python application designed to solve a sequence of integers based on user-defined parameters. The application reads integers, validates them, and executes a series of queries to deduce the values of a sequence.

## Main Functions

- **Input Validation**: Ensures that the provided integers N and K meet the specified constraints (1 ≤ K < N ≤ 1000 and K must be odd).
- **Query Execution**: Selects K distinct integers from the range [1, N], sends queries, and processes responses to determine the sequence values.
- **Output Generation**: Once all values are deduced, the application outputs the final sequence in the required format.

## Installation

To run the application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**:
   Execute the main script to start the application:
   ```bash
   python main.py
   ```

2. **Input Format**:
   When prompted, enter two integers N and K separated by a space:
   ```
   N K
   ```
   - **N**: The length of the sequence (1 ≤ N ≤ 1000).
   - **K**: The number of distinct integers to query (1 ≤ K < N, K must be odd).

3. **Output**:
   The application will print the final sequence in the format:
   ```
   ! A_1 A_2 ... A_N
   ```
   Ensure to check the output for correctness.

## Example Usage

To run the application with an example input:
```bash
echo "10 3" | python main.py
```
This command simulates inputting `10` for N and `3` for K.

## Error Handling

- If K is not an odd number or if the constraints are not met, the application will raise a `ValueError`.
- If an invalid query is made, the application will terminate immediately with a message indicating the error.

## Additional Information

For more details on the implementation, refer to the source code files:
- `main.py`: The entry point of the application.
- `query_handler.py`: Contains the logic for handling queries and responses.
- `utilities.py`: Includes utility functions for input validation.

For any issues or feature requests, please reach out to the development team.

```

This manual provides a comprehensive overview of the software, including its functionality, installation instructions, usage guidelines, and error handling. It is designed to help users understand how to effectively use the application.