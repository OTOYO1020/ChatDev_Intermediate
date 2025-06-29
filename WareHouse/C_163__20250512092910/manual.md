Here's a detailed user manual for the subordinate counter software, formatted in Markdown as requested:

```markdown
# Subordinate Counter

A simple application for counting immediate subordinates based on boss relationships in an organizational structure.

## Overview

The Subordinate Counter is designed to help organizations understand their hierarchical structure by counting how many immediate subordinates each member has. The software accepts the number of members and their immediate bosses, and returns a list of subordinate counts for each member.

## Main Functions

- **count_subordinates(N: int, A: List[int]) -> List[int]**: This function takes the number of members and a list of immediate bosses, and returns a list of counts of immediate subordinates for each member.

## Installation

To run the Subordinate Counter, you need to have Python installed on your machine. You can install the required dependencies using pip. 

1. Clone the repository or download the source code.
2. Navigate to the project directory in your terminal.
3. Install the dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Input Format**:
   - The first line of input should contain an integer `N`, representing the number of members.
   - The second line should contain `N-1` integers, representing the immediate bosses for members 2 to N. Each integer should be in the range `[1, i-1]` for each `i` in `[2, N]`.

2. **Running the Application**:
   - You can run the application by executing the `main.py` file. Use the following command in your terminal:

   ```bash
   python main.py
   ```

3. **Example Input**:
   ```
   5
   1 2 2 3
   ```

   In this example:
   - There are 5 members.
   - Member 2 reports to member 1, members 3 and 4 report to member 2, and member 5 reports to member 3.

4. **Expected Output**:
   - The output will be a space-separated string of subordinate counts for members 1 to N. For the example input above, the output would be:

   ```
   0 2 1 0 0
   ```

   This indicates:
   - Member 1 has 2 subordinates (members 2 and 3).
   - Member 2 has 1 subordinate (member 4).
   - Members 3 and 4 have no subordinates.

## Error Handling

- If the length of the list `A` is not equal to `N-1`, a `ValueError` will be raised.
- If any boss ID in the list `A` is out of the valid range, a `ValueError` will also be raised, indicating the invalid boss ID and its position.

## Conclusion

The Subordinate Counter is a straightforward tool for analyzing organizational structures. By providing the necessary inputs, users can quickly obtain insights into the number of immediate subordinates each member has.

For further assistance or support, please reach out to our development team.
```

This manual provides a comprehensive guide for users to understand the functionality, installation, and usage of the Subordinate Counter software. Let me know if you need any further modifications or additional information!