Here’s a detailed user manual for the substring formation checker software, written in Markdown format.

```markdown
# Substring Formation Checker

A utility for determining if a substring with specified occurrences of 'w' and 'b' can be formed from a repeating pattern.

## Overview

This software allows users to input the number of occurrences of 'w' and 'b' they wish to form into a substring. It validates the input and checks if the desired substring can be formed from the infinite repeating string `S = 'wbwbwwbwbwbw'`.

## Main Functions

1. **Input Validation**: Ensures that the input values for W and B are within the specified constraints:
   - \(0 \leq W, B \leq 100\)
   - \(W + B \geq 1\)

2. **Substring Formation Check**: Determines if a substring with W occurrences of 'w' and B occurrences of 'b' can be formed from the repeating pattern.

3. **Output**: Returns 'YES' if the substring can be formed, otherwise returns 'NO'.

## Installation

To run the software, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

You may need to install the following dependencies:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can simply run the main application without additional libraries as it uses built-in Python functions.

## How to Use

1. **Clone the Repository**: If you haven't already, clone the repository containing the software.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file `main.py`.

   ```bash
   python main.py
   ```

3. **Input Values**: When prompted, enter the values for W (occurrences of 'w') and B (occurrences of 'b').

   ```
   Enter W (occurrences of 'w'): 3
   Enter B (occurrences of 'b'): 2
   ```

4. **View Results**: The application will output whether the desired substring can be formed.

   ```
   YES
   ```

## Example Usage

- **Valid Input**: 
   - Input: `W = 3`, `B = 2`
   - Output: `YES`
   
- **Invalid Input**: 
   - Input: `W = 0`, `B = 0`
   - Output: `Invalid input. Please ensure 0 ≤ W, B ≤ 100 and W + B ≥ 1.`

## Conclusion

This software provides a straightforward way to check for substring formation from a defined repeating pattern. Ensure to follow the input constraints for accurate results. For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the software's functionality, installation process, and usage instructions.