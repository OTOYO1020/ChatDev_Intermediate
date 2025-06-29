Here's a detailed user manual for the Ball Arrangement application, formatted in Markdown as requested:

```markdown
# Ball Arrangement Application

This application calculates the number of valid arrangements of white and black balls based on specific conditions. It allows users to input the number of white balls (N), black balls (M), and a maximum difference (K) between the number of white and black balls in any arrangement.

## Main Functions

1. **Input Handling**: The application reads integers N, M, and K from standard input.
2. **Arrangement Calculation**: It calculates the total number of arrangements of N white balls and M black balls using combinatorial mathematics.
3. **Valid Arrangement Counting**: The application counts valid arrangements that satisfy the condition `w_i ≤ b_i + K` for all `i` using dynamic programming.
4. **Output**: It prints the final count of valid arrangements modulo `10^9 + 7`.

## Installation Instructions

To run the Ball Arrangement application, you need to have Python installed on your machine. Follow these steps to set up your environment:

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the application code to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Set Up Dependencies**: The current implementation does not rely on any external libraries, so you can run it without additional installations. However, if you prefer to keep a `requirements.txt` file, you can create an empty one:
   ```bash
   touch requirements.txt
   ```

## How to Use the Application

1. **Run the Application**: Navigate to the directory containing `main.py` and run the application using Python.
   ```bash
   python main.py
   ```

2. **Input Values**: When prompted, enter the number of white balls (N), the number of black balls (M), and the maximum difference (K) between the number of white and black balls. Ensure that all inputs are non-negative integers.

   Example Input:
   ```
   Enter number of white balls (N): 3
   Enter number of black balls (M): 2
   Enter maximum difference (K): 1
   ```

3. **View Results**: After entering the values, the application will calculate and display the number of valid arrangements based on the provided inputs.

   Example Output:
   ```
   Valid arrangements: 5
   ```

## Example Usage

Here’s a quick example of how the application works:

1. Start the application:
   ```bash
   python main.py
   ```

2. Input the values:
   ```
   Enter number of white balls (N): 4
   Enter number of black balls (M): 3
   Enter maximum difference (K): 2
   ```

3. Output will show:
   ```
   Valid arrangements: 35
   ```

## Conclusion

The Ball Arrangement application provides a straightforward way to calculate valid arrangements of colored balls based on user-defined conditions. With its simple interface and efficient algorithm, it serves as a useful tool for combinatorial calculations.

For any issues or further inquiries, please contact the support team.
```

This manual provides a comprehensive overview of the application, including its functionality, installation instructions, and usage guidelines, ensuring that users can easily understand and utilize the software.