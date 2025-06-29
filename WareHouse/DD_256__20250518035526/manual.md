Here's a detailed user manual for the Interval Merger application, formatted in Markdown as requested:

```markdown
# Interval Merger

A simple application for merging overlapping intervals.

## Overview

The Interval Merger application allows users to input a list of intervals and receive a merged list of intervals as output. This is particularly useful in scenarios where you need to consolidate overlapping time slots, ranges, or any other numerical intervals.

## Main Functions

- **Input Handling**: Accepts user input for intervals in the form of a list of tuples.
- **Merging Logic**: Processes the input intervals to merge any overlapping or contiguous intervals.
- **Output**: Returns a list of merged intervals in the same tuple format.

## Installation

To run the Interval Merger application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Set Up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv interval_merger_env
   source interval_merger_env/bin/activate  # On Windows use `interval_merger_env\Scripts\activate`
   ```

3. **Install Required Dependencies**: The application uses the built-in libraries, so no additional installations are required. Just ensure you have Python's standard library available.

## How to Use the Application

1. **Run the Application**:
   Navigate to the directory where `main.py` is located and run the following command:
   ```bash
   python main.py
   ```

2. **Input Format**:
   When prompted, enter the intervals in the following format:
   ```
   [(L1, R1), (L2, R2), ..., (LN, RN)]
   ```
   For example:
   ```
   Enter intervals (e.g., [(1, 3), (2, 4), (5, 7)]): [(1, 3), (2, 4), (5, 7)]
   ```

3. **Output**:
   The application will process the input and display the merged intervals:
   ```
   Merged Intervals: [(1, 4), (5, 7)]
   ```

## Error Handling

If the input format is incorrect, the application will raise an error message. Ensure that:
- The input is a list.
- Each interval is a tuple of two integers.
- The first integer is less than the second integer in each tuple.

Example of an error message:
```
Input Error: Input must be a list of tuples, each containing two integers where the first is less than the second.
```

## Conclusion

The Interval Merger application is a straightforward tool for merging overlapping intervals. By following the installation and usage instructions, users can easily consolidate their intervals and improve their data handling processes.

For any further questions or support, please reach out to our support team.
```

This manual provides a comprehensive guide for users to understand the functionality of the Interval Merger application, how to set it up, and how to use it effectively.