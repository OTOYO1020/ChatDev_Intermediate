Here's a detailed user manual for the ball position simulation software, formatted in Markdown:

```markdown
# Ball Position Simulation

A simulation tool to calculate the expected position of a black ball after a series of random swap operations.

## Overview

This software allows users to simulate the expected position of a black ball after performing a specified number of random swap operations between positions. The user can input the total number of positions and the number of operations to be performed. The software will then calculate and return the expected position of the black ball in a modular arithmetic format.

## Main Functions

- **expected_position(N: int, K: int) -> int**: 
  - Calculates the expected position of the black ball after K operations.
  - Takes two parameters:
    - `N`: The total number of positions (must be a positive integer).
    - `K`: The number of swap operations (must be a non-negative integer).
  - Returns the result R such that R * Q ≡ P (mod 998244353), where P is the expected position and Q is the number of operations.

## Installation

To run the Ball Position Simulation, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Open your terminal or command prompt and run the following command to install the required dependencies:
   ```bash
   pip install fractions
   ```

## How to Use

1. **Run the Application**: 
   - Navigate to the directory where the `main.py` file is located.
   - Execute the following command in your terminal:
     ```bash
     python main.py
     ```

2. **Input Parameters**:
   - You will be prompted to enter the number of positions (N) and the number of operations (K).
   - Ensure that N is a positive integer and K is a non-negative integer. If the input is invalid, an error message will be displayed.

3. **View Results**:
   - After entering valid inputs, the application will calculate the expected position of the black ball and print the result R.

## Example Usage

```plaintext
Enter number of positions (N): 5
Enter number of operations (K): 10
Result R: 123456789
```

## Error Handling

- If you enter a non-integer value or an invalid integer (e.g., negative for N or K), the application will display an error message:
  ```plaintext
  Input Error: N must be a positive integer and K must be a non-negative integer.
  ```

## Conclusion

The Ball Position Simulation software provides a simple yet effective way to understand the expected position of a black ball after a series of random operations. By following the installation and usage instructions, users can easily run the simulation and explore different scenarios.

For further assistance or inquiries, please contact our support team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.