Here’s a detailed user manual for the modulo calculator application, formatted in Markdown as requested:

```markdown
# Modulo Calculator

A simple application to calculate the modulo of a given integer \( N \) with respect to \( 998244353 \).

## Quick Install

To run the Modulo Calculator, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Clone the Repository

You can clone the repository containing the application code using the following command:

```bash
git clone https://github.com/yourusername/modulo_calculator.git
cd modulo_calculator
```

### Install Dependencies

This application does not require any external dependencies beyond Python itself. Ensure you have Python 3.x installed.

## 🤔 What is this?

The Modulo Calculator allows users to input an integer \( N \) within the range of \(-10^{18}\) to \(10^{18}\) (inclusive) and calculates the result of \( x = N \mod 998244353 \). The result \( x \) will always be non-negative and will fall within the range of \( 0 \) to \( 998244353 - 1 \).

### Main Functions

- **Input Handling**: The application reads an integer from standard input and ensures it is within the specified range.
- **Modulo Calculation**: It calculates the modulo using the formula \( x = N \mod 998244353 \).
- **Output**: The result is printed to the console.

## 📖 How to Use

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where the application is located, and run the following command:

   ```bash
   python main.py
   ```

2. **Input an Integer**: When prompted, enter an integer within the range of \(-10^{18}\) to \(10^{18}\). For example:

   ```
   Please enter an integer within the range of -10^18 to 10^18: 1234567890123456789
   ```

3. **View the Result**: After entering a valid integer, the application will calculate and display the result. For example:

   ```
   1234567890123456789 mod 998244353 = 1234567890123456789 % 998244353 = 123456789
   ```

## Error Handling

If you enter an invalid input (e.g., a non-integer or an integer outside the specified range), the application will display an error message:

```
Invalid input: invalid literal for int() with base 10: 'abc'
```

or

```
Invalid input: Input must be within the range of -10^18 to 10^18.
```

## Conclusion

The Modulo Calculator is a straightforward tool for performing modulo calculations with large integers. It ensures that inputs are validated and provides clear feedback to users. For any further questions or support, please reach out to the development team.

```

Feel free to modify any sections as needed to better fit your branding or additional features of the application!