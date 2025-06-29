Here is the `manual.md` file for the Cost Calculator application:

```markdown
# Cost Calculator

A simple application to compute the minimum expected cost based on given parameters.

## Quick Install

To run the Cost Calculator, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Make sure you have the following dependencies in your `requirements.txt`:

```
# requirements.txt
```

## 🤔 What is this?

The Cost Calculator is designed to help users determine the minimum expected cost of operations based on the number of items and specific costs associated with two different operations. The application uses a recursive approach to calculate costs efficiently.

### Main Functions

1. **Input Parameters**:
   - `N`: Total number of items (integer).
   - `A`: Divisor for the first operation (positive integer).
   - `X`: Cost for the first operation (non-negative integer).
   - `Y`: Cost for the second operation (non-negative integer).

2. **Cost Calculation**:
   - The application calculates the minimum expected cost using two operations:
     - **First Operation**: Divides `N` by `A` and adds the cost `X`.
     - **Second Operation**: Uses a die roll (1 to 6) to divide `N` and adds the cost `Y`, averaging the results.

3. **Memoization**: The application uses memoization to store previously computed costs, improving efficiency.

## 📖 How to Use

1. **Run the Application**:
   - Execute the main application file `main.py` in your terminal or command prompt:

   ```bash
   python main.py
   ```

2. **Input Values**:
   - When prompted, enter the integer values for `N`, `A`, `X`, and `Y`. Ensure that:
     - `N` is a non-negative integer.
     - `A` is a positive integer.
     - `X` and `Y` are non-negative integers.

3. **View Results**:
   - After entering the values, the application will compute and display the minimum expected cost based on the provided inputs.

## Example Usage

```bash
Enter the total number of items (N): 10
Enter the divisor for the first operation (A): 2
Enter the cost for the first operation (X): 5
Enter the cost for the second operation (Y): 3
Minimum Expected Cost: 8
```

## 🛠 Troubleshooting

- **Invalid Input**: If you enter invalid values (e.g., negative integers or non-integers), the application will prompt you to enter valid integers.
- **Dependencies**: Ensure all required dependencies are installed. If you encounter any issues, check your Python installation and the `requirements.txt` file.

## Support

For further assistance, please contact our support team or refer to the documentation for more detailed explanations of the functions and features.

```

This manual provides a comprehensive guide for users to understand and utilize the Cost Calculator application effectively.