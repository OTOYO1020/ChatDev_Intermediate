Here's a detailed user manual for the Candy Distribution application, formatted in Markdown as requested:

```markdown
# Candy Distribution Application

Minimizing frustration in candy distribution among people based on their dislikes.

## Overview

The Candy Distribution application is designed to help distribute candies among a group of people while minimizing frustration caused by dislikes. Each person has a specific individual they dislike, and the application calculates the optimal order of candy distribution to minimize the total frustration.

## Main Functions

- **Input Handling**: The application reads the number of people and their respective dislikes and frustration values.
- **Graph Construction**: It builds a directed graph based on the dislikes.
- **Topological Sorting**: The application performs a topological sort on the graph to determine a valid order for candy distribution.
- **Frustration Calculation**: It calculates the total frustration based on the order of candy distribution.
- **Result Display**: Finally, it displays the minimum total frustration.

## Installation

To run the Candy Distribution application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

The application requires the following Python packages:

- `collections` (part of the Python standard library, no installation required)

### Quick Install

1. Ensure you have Python installed.
2. Clone the repository or download the source code.
3. Navigate to the directory containing the application files.

## Usage Instructions

1. **Run the Application**:
   Open your terminal or command prompt and navigate to the directory where `main.py` is located. Run the following command:
   ```bash
   python main.py
   ```

2. **Input Data**:
   - The application will prompt you to enter the number of people (N).
   - For each person, you will be asked to enter:
     - The index of the disliked person (0 to N-1).
     - The frustration value (must be non-negative).
   - Ensure that the disliked person index is valid and not the same as the person's index.

3. **View Results**:
   After entering all the data, the application will calculate and display the minimum total frustration.

### Example Input

```
Enter the number of people: 3
Enter disliked person index for person 1: 2
Enter frustration value for person 1: 5
Enter disliked person index for person 2: 0
Enter frustration value for person 2: 3
Enter disliked person index for person 3: 1
Enter frustration value for person 3: 4
```

### Example Output

```
Minimum Total Frustration: 8
```

## Error Handling

The application includes basic error handling for invalid inputs:
- If the disliked person index is out of range or if a person dislikes themselves, an error message will be displayed.
- If the input for frustration is negative, an error message will also be shown.

## Conclusion

The Candy Distribution application is a useful tool for managing candy distribution in a way that minimizes frustration among individuals based on their dislikes. By following the instructions above, you can easily set up and run the application to achieve optimal results.
```

This manual provides a comprehensive guide for users to understand the functionality of the Candy Distribution application, how to install it, and how to use it effectively.