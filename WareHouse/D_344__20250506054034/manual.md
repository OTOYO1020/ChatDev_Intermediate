Here's a detailed user manual for the String Formation application, formatted in Markdown:

```markdown
# String Formation Application

A simple application to determine the minimum cost required to form a target string using strings from multiple bags.

## Main Functions

The String Formation application allows users to:

- Input the number of bags and the strings contained within each bag.
- Specify a target string that needs to be formed.
- Calculate the minimum cost to form the target string by concatenating strings from the bags.
- Output the minimum cost or indicate if the target string cannot be formed.

## Installation

To run the String Formation application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

Make sure you have the following dependencies installed:

- Python 3.x

You can install any required packages using pip. However, this application does not have external dependencies beyond the standard library.

## How to Use the Application

1. **Clone the Repository**: If you haven't already, clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file.

   ```bash
   python main.py
   ```

3. **Input Data**:
   - When prompted, enter the number of bags (N).
   - For each bag, specify the number of strings it will contain.
   - Input the strings for each bag, separated by spaces.
   - Finally, enter the target string you wish to form.

4. **View Results**: After entering the required information, the application will calculate and display the minimum cost to form the target string. If the target string cannot be formed, it will display `-1`.

### Example Usage

```plaintext
Enter the number of bags: 2
How many strings would you like to add to bag 1? 3
Enter 3 strings for bag 1 (space separated): hello world hi
How many strings would you like to add to bag 2? 2
Enter 2 strings for bag 2 (space separated): there hi
Enter the target string: helloworld
Minimum Cost: 2
```

## Troubleshooting

- **Input Errors**: Ensure that you are entering valid integers when prompted for the number of bags and strings. The application will notify you of any input errors.
- **Target String Formation**: If the application returns `-1`, it indicates that the target string cannot be formed with the provided bags. Double-check the strings in the bags to ensure they can concatenate to form the target string.

## Additional Information

For any issues or feature requests, please contact the support team or refer to the documentation for further assistance.

Happy string forming!
```

This manual provides a comprehensive guide for users to understand the application, install it, and use it effectively.