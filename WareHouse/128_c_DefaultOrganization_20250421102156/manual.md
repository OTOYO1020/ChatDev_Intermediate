Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Bulb-Switch Combination Calculator

This application calculates the valid combinations of switch states that can light up a set of bulbs based on their connections to switches and required parity.

## Main Functions

The Bulb-Switch Combination Calculator performs the following key functions:

1. **Input Reading**: Reads the number of switches (N) and bulbs (M) from the user.
2. **Bulb Configuration**: For each bulb, it reads the number of connected switches, their indices, and the required parity (even or odd).
3. **Combination Generation**: Generates all possible combinations of on and off states for the switches.
4. **Validation**: Checks each combination to see if it meets the requirements for all bulbs.
5. **Output**: Prints the total count of valid combinations that can light all bulbs.

## Installation

To run the Bulb-Switch Combination Calculator, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

Create a `requirements.txt` file to manage dependencies. Currently, there are no external dependencies required for this application, but you can add any future dependencies as needed.

```plaintext
# requirements.txt
# Placeholder for future dependencies
```

### Installation Steps

1. Clone the repository or download the files `main.py` and `bulb.py`.
2. Navigate to the directory containing the files in your terminal.
3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install any required packages (if added in the future):
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Application

1. **Run the Application**: Execute the main application file using Python.
   ```bash
   python main.py
   ```

2. **Input Data**: Follow the prompts to enter the required data:
   - Enter the number of switches (N).
   - Enter the number of bulbs (M).
   - For each bulb, provide:
     - The number of connected switches.
     - The indices of the connected switches (comma-separated).
     - The required parity (0 for even, 1 for odd).

3. **View Results**: After entering all the required data, the application will calculate and display the total count of valid combinations that can light all bulbs.

### Example Usage

```plaintext
Enter the number of switches (N): 3
Enter the number of bulbs (M): 2
Enter the number of connected switches for bulb 1 (k): 2
Enter the connected switch indices for bulb 1 (comma-separated): 1,2
Enter the required parity for bulb 1 (0 for even, 1 for odd): 1
Enter the number of connected switches for bulb 2 (k): 1
Enter the connected switch indices for bulb 2 (comma-separated): 3
Enter the required parity for bulb 2 (0 for even, 1 for odd): 0
Total valid combinations: 2
```

## Conclusion

The Bulb-Switch Combination Calculator is a simple yet powerful tool for determining valid configurations of switches to light up bulbs based on user-defined criteria. Feel free to extend the functionality by adding more features or dependencies as needed.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and examples to help users effectively utilize the software.