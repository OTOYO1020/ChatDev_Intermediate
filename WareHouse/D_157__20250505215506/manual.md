```markdown
# Friendship Candidate Calculator

A Python application designed to calculate potential friendship candidates based on user-defined friendships and blockships.

## Overview

This software allows users to input the number of users, friendships, and blockships, and then calculates how many potential friends each user has based on the existing relationships. The application utilizes a graph structure to manage friendships and blockships, ensuring efficient pathfinding to determine friendship candidates.

## Main Functions

- **Input Handling**: Reads integers N (number of users), M (number of friendships), and K (number of blockships) from standard input.
- **Friendship Management**: Stores friendships in an adjacency list and blockships in a set.
- **Candidate Calculation**: For each user, counts potential friends by checking for valid paths through friendships while considering blockships.
- **Output**: Prints the number of potential friends for each user as a space-separated list.

## Installation

To run the application, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Download or clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: This application uses the `collections` module, which is part of the Python standard library, so no additional installations are required.

## Usage

To use the Friendship Candidate Calculator, follow these steps:

1. **Run the Application**: Execute the main application file.

   ```bash
   python main.py
   ```

2. **Input Data**: Provide the required input in the following format:
   - First line: Three integers N, M, K.
   - Next M lines: Each line contains two integers A and B representing a friendship.
   - Next K lines: Each line contains two integers C and D representing a blockship.

   Example input:
   ```
   5 4 2
   1 2
   1 3
   2 3
   4 5
   1 4
   2 5
   ```

3. **View Output**: After entering the data, the application will process the input and output the number of potential friends for each user as a space-separated list.

   Example output:
   ```
   1 0 0 0 0
   ```

## Important Notes

- Ensure that the values for N, M, and K are within valid limits:
  - N must be positive.
  - M and K must be non-negative and should not exceed the maximum possible friendships.
- Friendships and blockships must be between valid user indices (1 to N).

## Conclusion

The Friendship Candidate Calculator is a powerful tool for analyzing social networks and understanding potential friendship dynamics. By following the instructions above, users can easily set up and utilize the application to explore friendship possibilities within their defined user groups.
```