Here's a detailed user manual for the software that calculates the maximum product of two integers formed by permuting the digits of a given integer.

```markdown
# Max Product Calculator

A utility for calculating the maximum product of two positive integers formed by permuting the digits of a given integer.

## Quick Install

To run the Max Product Calculator, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install itertools
```

## 🤔 What is this?

The Max Product Calculator is a Python application that takes a positive integer as input and calculates the maximum product of two integers that can be formed by permuting the digits of the input integer. This is achieved by generating all unique permutations of the digits, splitting them into two non-empty parts, and ensuring that neither part has leading zeros.

### Key Features:
- Accepts any positive integer as input.
- Generates all unique permutations of the digits.
- Validates splits to ensure no leading zeros.
- Calculates and returns the maximum product of the two integers formed.

## 📖 How to Use

1. **Run the Application:**
   To start the application, navigate to the directory where the `main.py` file is located and run the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Input a Positive Integer:**
   When prompted, enter a positive integer. For example:

   ```
   Enter a positive integer: 1234
   ```

3. **View the Result:**
   After processing the input, the application will output the maximum product of two integers formed by the permutations of the digits. For example:

   ```
   Max Product: 432
   ```

## 🛠️ Code Structure

The application consists of two main files:

- **main.py:** This is the entry point of the application. It handles user input and displays the output.
- **utils.py:** This file contains the core logic for calculating the maximum product of two integers formed by permuting the digits of the input integer.

### Example Code Snippet

Here is a brief overview of the core function in `utils.py`:

```python
from itertools import permutations

def max_product_of_separated_integers(N: int) -> int:
    digits = str(N)
    max_product = 0
    unique_permutations = set(permutations(digits))
    
    for perm in unique_permutations:
        perm_str = ''.join(perm)
        for i in range(1, len(perm_str)):
            part1 = perm_str[:i]
            part2 = perm_str[i:]
            if (part1[0] != '0' and part2[0] != '0'):
                num1 = int(part1)
                num2 = int(part2)
                product = num1 * num2
                max_product = max(max_product, product)
    
    return max_product
```

## 📚 Additional Resources

For further information and examples, please refer to the official Python documentation on [itertools](https://docs.python.org/3/library/itertools.html).

If you encounter any issues or have questions, feel free to reach out for support.

Happy calculating!
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and a brief explanation of the code structure. It is designed to help users understand how to effectively use the Max Product Calculator.