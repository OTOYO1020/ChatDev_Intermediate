Here's a detailed user manual for the voting system software, formatted in Markdown as requested:

```markdown
# Voting System

A simple and efficient voting system to count votes for candidates and determine the current winner in real-time.

## Main Functions

The Voting System provides the following main functionalities:

- **Vote Counting**: Accurately counts votes for each candidate.
- **Current Winner Tracking**: Keeps track of the candidate with the most votes and updates after each vote is cast.
- **Input Validation**: Ensures that only valid votes are counted and provides feedback for invalid votes.

## Installation

To run the Voting System, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

1. **Clone the Repository**: If you haven't already, clone the repository containing the voting system code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Required Packages**: The Voting System does not require any external packages beyond Python's standard library. However, ensure you have Python 3.x installed.

## How to Use the Voting System

1. **Run the Application**: Open your terminal or command prompt and navigate to the directory where `main.py` is located. Run the application using the following command:

   ```bash
   python main.py
   ```

2. **Input Format**: The application expects input in the following format:
   - First line: Two integers, N (number of candidates) and M (number of votes).
   - Second line: An array of M integers, where each integer represents a vote for a candidate (1 to N).

   **Example Input**:
   ```
   3 5
   1 2 1 3 2
   ```

3. **Output**: After each vote is counted, the application will print the current winner in the format:
   ```
   Current Winner: Candidate X
   ```

   Where `X` is the candidate number with the most votes.

## Example Usage

Here’s an example of how to use the Voting System:

1. Start the application:
   ```bash
   python main.py
   ```

2. Provide the input:
   ```
   3 5
   1 2 1 3 2
   ```

3. The output will be:
   ```
   Current Winner: Candidate 1
   Current Winner: Candidate 1
   Current Winner: Candidate 1
   Current Winner: Candidate 2
   Current Winner: Candidate 2
   ```

## Error Handling

If an invalid vote is cast (e.g., a vote for a candidate number that does not exist), the application will raise a `ValueError` and print an error message indicating the issue.

## Conclusion

The Voting System is designed to be simple yet effective for counting votes and determining the current winner in real-time. For any issues or feature requests, please contact the development team.

```

This manual provides a comprehensive overview of the voting system, including installation instructions, usage guidelines, and examples to help users effectively interact with the software.