Here's a detailed user manual for the user following system software, encapsulating the main functions, installation instructions, and usage guidelines.

```markdown
# User Following System

A simple application to manage user following relationships, allowing users to follow, unfollow, and check the following status of other users.

## Main Functions

The User Following System provides the following functionalities:

1. **Follow Operation**: Allows one user to follow another user.
2. **Unfollow Operation**: Allows one user to unfollow another user.
3. **Check Following Status**: Checks if two users are following each other.

## Installation

To run the User Following System, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You may need to install the following dependencies:

- Python 3.x
- No additional libraries are required for this application as it uses built-in Python features.

### Steps to Install

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**:
   The application consists of two main files: `main.py` and `user_manager.py`. You can run the application using the command line.

## Usage Instructions

### Input Format

The application expects input in the following format:

```
N Q
T_1 A_1 B_1
T_2 A_2 B_2
...
T_Q A_Q B_Q
```

- `N`: Number of users.
- `Q`: Number of operations.
- Each operation consists of:
  - `T_i`: Type of operation (1 for follow, 2 for unfollow, 3 for check status).
  - `A_i`: User ID of the first user.
  - `B_i`: User ID of the second user.

### Example Input

```
5 5
1 1 2
1 2 3
2 1 2
3 1 2
3 2 1
```

### Running the Application

1. **Prepare Input**: Create a text file (e.g., `input.txt`) with the input format described above.
2. **Run the Application**: Use the command line to execute the `main.py` file, redirecting the input from the file:
   ```bash
   python main.py < input.txt
   ```

### Output Format

The output will consist of lines with "Yes" or "No" for each check status operation (T_i = 3), printed in the order they were requested.

### Example Output

For the example input provided above, the output would be:
```
No
No
```

## Conclusion

This User Following System is a straightforward implementation for managing user relationships. It can be extended or modified to include additional features as needed. For any issues or feature requests, please contact the development team.

```

This manual provides a comprehensive overview of the software, ensuring users can easily understand how to install and utilize the application effectively.