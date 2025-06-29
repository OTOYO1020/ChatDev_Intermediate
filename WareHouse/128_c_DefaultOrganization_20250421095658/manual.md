Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Bulb and Switch Control System

A Python application for managing the states of switches and bulbs based on user-defined connections and parity requirements.

## Overview

This application allows users to define a system of switches and bulbs, where each bulb can be connected to multiple switches. Users can specify the required parity (even or odd) of the number of switches that need to be turned on for each bulb to light up. The application calculates all possible combinations of switch states and determines how many combinations satisfy the conditions for all bulbs.

## Main Functions

- **Input Handling**: Read the number of switches (N) and bulbs (M) from the user.
- **Bulb Configuration**: Allow users to specify the connections of each bulb to the switches and the required parity for each bulb.
- **Combination Generation**: Generate all possible combinations of on/off states for the switches.
- **Validation**: Check each combination against the bulbs' requirements and count valid combinations.
- **Output**: Display the total number of valid combinations that light all bulbs.

## Installation

To run the application, ensure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Dependencies

This application requires the following Python packages:

- `itertools` (included in the Python standard library)

No additional installations are necessary for this package.

## How to Use the Application

1. **Clone the Repository**: If you have the source code, clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main script using Python.

   ```bash
   python main.py
   ```

3. **Input Data**: Follow the prompts to enter the number of switches (N) and bulbs (M). For each bulb, provide:
   - The number of connected switches.
   - The indices of the connected switches (comma-separated).
   - The required parity (0 for even, 1 for odd).

   Example input:
   ```
   Enter number of switches (N) and bulbs (M): 3 2
   Enter number of connected switches for Bulb 1: 2
   Enter the 2 connected switch indices (comma-separated): 1,2
   Enter the required parity (0 or 1) for Bulb 1: 1
   Enter number of connected switches for Bulb 2: 1
   Enter the 1 connected switch indices (comma-separated): 3
   Enter the required parity (0 or 1) for Bulb 2: 0
   ```

4. **View Results**: After entering the data, the application will calculate and display the total number of valid combinations that satisfy the conditions for all bulbs.

   Example output:
   ```
   Total valid combinations: 4
   ```

## Example Use Case

Consider a scenario where you have 3 switches and 2 bulbs:
- Bulb 1 is connected to switches 1 and 2 and requires an odd number of them to be on.
- Bulb 2 is connected to switch 3 and requires an even number of it to be on.

After entering the above configuration, the application will evaluate all possible switch states and determine how many configurations will light both bulbs.

## Conclusion

This application provides a flexible way to manage and evaluate the states of switches and bulbs based on user-defined criteria. It can be extended or modified to fit more complex scenarios as needed.

For any issues or feature requests, please contact the development team.
```

This manual provides a comprehensive guide for users to understand the application, its functionalities, and how to effectively use it.