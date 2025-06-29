Here's a detailed user manual for the software based on the provided code and requirements.

```markdown
# Switch and Bulb Management Application

This application allows users to manage a system of switches and bulbs, determining valid combinations of switch states that will light all connected bulbs based on their required parity.

## Main Functions

- **Input Handling**: The application prompts the user to input the number of switches and bulbs, as well as the connections between them and their required parities.
- **Switch Management**: The application calculates all possible combinations of switch states and checks which combinations successfully light all bulbs.
- **Output Display**: The application displays the total number of valid combinations where all bulbs are lit.

## Installation

To run the application, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

This application does not require any external libraries beyond the standard Python library. However, it is recommended to run it in a virtual environment to avoid conflicts with other projects.

1. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```
   
2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

## How to Use the Application

1. **Run the Application**:
   Navigate to the directory where the `main.py` file is located and run the following command:
   ```bash
   python main.py
   ```

2. **Input the Number of Switches and Bulbs**:
   - When prompted, enter the total number of switches (N).
   - Next, enter the total number of bulbs (M).

3. **Input Connection Information for Each Bulb**:
   For each bulb, you will be prompted to:
   - Enter the number of connected switches for that bulb.
   - Enter the indices of the connected switches (space-separated). Ensure that the indices are within the range of the total number of switches.
   - Enter the required parity for the bulb (0 or 1).

4. **View the Results**:
   After entering all the information, the application will calculate the valid combinations of switch states and display the total number of valid combinations where all bulbs are lit.

## Example Usage

```
Enter number of switches: 3
Enter number of bulbs: 2
Enter number of connected switches for bulb 1: 2
Enter connected switches for bulb 1 (space-separated, starting from 1): 1 2
Enter required parity for bulb 1 (0 or 1): 1
Enter number of connected switches for bulb 2: 1
Enter connected switches for bulb 2 (space-separated, starting from 1): 3
Enter required parity for bulb 2 (0 or 1): 0
```

The application will then output the number of valid combinations based on the input provided.

## Conclusion

This application provides a straightforward way to manage and analyze the states of switches and bulbs based on user-defined criteria. For any issues or further assistance, please refer to the code comments or reach out to the development team.
```

This manual provides a comprehensive guide for users to understand the application's functionality, installation process, and usage instructions.