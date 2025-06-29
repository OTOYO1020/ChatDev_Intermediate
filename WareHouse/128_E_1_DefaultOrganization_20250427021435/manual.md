Here's a detailed user manual for the roadworks simulation software, formatted in Markdown:

```markdown
# Roadworks Simulation

A Python application to simulate walking through roadworks while managing blocked intervals.

## Overview

This software allows users to input roadworks data and simulate the distance a person can walk before encountering a blocked point. It efficiently handles overlapping intervals and provides quick responses to queries regarding walking times.

## Main Functions

1. **Input Handling**: Reads integers \( N \) (number of roadworks) and \( Q \) (number of queries) from standard input, followed by \( N \) triplets \((X_i, S_i, T_i)\) representing roadworks and \( Q \) integers \( D_i \) representing start times.

2. **Data Structure Initialization**: Initializes a dictionary to store blocked intervals for each coordinate.

3. **Populate Blocked Intervals**: Iterates through the roadworks data to populate the blocked intervals dictionary.

4. **Merge Intervals**: Merges overlapping or contiguous intervals for each coordinate to ensure accurate simulation.

5. **Simulate Walking**: For each query, calculates the distance a person can walk before reaching a blocked point.

6. **Binary Search**: Utilizes binary search to efficiently find the first blocked point encountered after the starting time.

7. **Output Results**: Prints the distance each person walked before stopping.

## Installation

To run the application, ensure you have Python installed on your system. You can install the required dependencies using pip. 

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Note

Currently, there are no specific dependencies listed in `requirements.txt`. You can add any future dependencies as needed.

## Usage

To run the application, you can use the following command:

```bash
python main.py < input.txt
```

### Input Format

The input should be structured as follows:

- The first line contains two integers \( N \) and \( Q \).
- The next \( N \) lines each contain three integers \( X_i, S_i, T_i \) representing the coordinate and the start and end times of the roadworks.
- The following \( Q \) lines each contain one integer \( D_i \) representing the start time for each query.

### Example Input

```
3 2
1 2 5
2 3 6
3 1 4
2
5
```

### Example Output

The output will be the distance each person can walk before encountering a blocked point, printed on separate lines.

```
1
3
```

## Conclusion

This software provides a robust solution for simulating walking through roadworks while managing blocked intervals effectively. For further assistance or inquiries, please reach out to our support team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.