```markdown
# Pigeon Nest Manager

A command-line application for managing the movement of pigeons between nests and tracking nests with multiple pigeons.

## Overview

The Pigeon Nest Manager allows users to efficiently manage the placement of pigeons in nests and to query the number of nests that contain multiple pigeons. The application operates entirely through standard input and output, making it suitable for environments without a graphical user interface.

## Main Functions

1. **Move Pigeon**: Move a specified pigeon to a designated nest.
   - Input format: `1 P H` where `P` is the pigeon number and `H` is the nest number.
   
2. **Count Nests with Multiple Pigeons**: Retrieve the count of nests that currently have more than one pigeon.
   - Input format: `2`

## Installation

To run the Pigeon Nest Manager, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. Clone the repository or download the files `main.py` and `pigeon_nest_manager.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where the files are located.

No additional dependencies are required beyond Python's standard library.

## How to Use

1. **Run the Application**:
   Execute the following command in your terminal:
   ```bash
   python main.py
   ```

2. **Input Format**:
   - First, input the number of pigeons `N` and the number of nests `Q`:
     ```
     N Q
     ```
   - Followed by `Q` queries, which can be either:
     - To move a pigeon:
       ```
       1 P H
       ```
     - To count nests with multiple pigeons:
       ```
       2
       ```

3. **Example Usage**:
   ```
   5 3
   1 1 3
   1 2 3
   2
   ```
   In this example:
   - There are 5 pigeons and 3 queries.
   - The first query moves pigeon 1 to nest 3.
   - The second query moves pigeon 2 to nest 3.
   - The third query counts how many nests have multiple pigeons.

4. **Output**:
   The results of all count queries will be printed sequentially after processing all queries.

## Conclusion

The Pigeon Nest Manager is a simple yet effective tool for managing pigeon placements and querying nest statuses. It is designed for efficiency and ease of use in a command-line environment.
```