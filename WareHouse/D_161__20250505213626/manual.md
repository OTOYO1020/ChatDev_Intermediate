Here's a detailed user manual for the Lunlun Number Generator software, formatted in Markdown as requested:

```markdown
# Lunlun Number Generator

A simple application to generate and retrieve lunlun numbers based on user input.

## What are Lunlun Numbers?

Lunlun numbers are positive integers where the absolute difference between every pair of adjacent digits is at most 1. For example, 123, 321, and 232 are lunlun numbers, while 145 and 300 are not.

## Main Functions

The Lunlun Number Generator provides the following main functionalities:

- **Generate Lunlun Numbers**: Generate a list of lunlun numbers up to the specified count \( K \).
- **Retrieve the K-th Lunlun Number**: Given a positive integer \( K \), retrieve the \( K \)-th smallest lunlun number.

## Quick Install

To run the Lunlun Number Generator, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install collections
```

## How to Use the Lunlun Number Generator

1. **Clone the Repository**: If you haven't already, clone the repository containing the Lunlun Number Generator code.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the `main.py` file to start the application.

   ```bash
   python main.py
   ```

3. **Input a Positive Integer**: When prompted, enter a positive integer \( K \). This integer represents the position of the lunlun number you wish to retrieve.

   ```
   Enter a positive integer K: 5
   ```

4. **View the Output**: The application will output the \( K \)-th lunlun number.

   ```
   5th lunlun number is: 5
   ```

## Example Usage

Here’s a step-by-step example of how to use the Lunlun Number Generator:

1. Start the application by running `python main.py`.
2. When prompted, enter `10`.
3. The application will output `10th lunlun number is: 10`.

## Code Structure

The application consists of two main files:

- **main.py**: The entry point of the application that handles user input and output.
- **lunlun_generator.py**: The module that contains the logic for generating lunlun numbers.

### main.py

This file manages user interaction and calls the lunlun number generation logic.

### lunlun_generator.py

This module contains the `LunlunNumberGenerator` class, which includes methods for checking if a number is a lunlun number and generating lunlun numbers using a breadth-first search approach.

## Conclusion

The Lunlun Number Generator is a straightforward tool for generating and retrieving lunlun numbers. By following the instructions above, you can easily set up and use the application to explore lunlun numbers.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the Lunlun Number Generator, including installation instructions, usage guidelines, and a brief explanation of the code structure.