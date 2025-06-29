Here’s a detailed user manual for the Light Bulb Switches application, formatted in Markdown as requested:

```markdown
# Light Bulb Switches Application

The Light Bulb Switches application allows users to determine the number of valid combinations of switch states that can light all connected bulbs based on specified conditions. This application is designed to help users understand the relationship between switches and bulbs through a simple interface.

## Main Functions

- **Input Parsing**: The application prompts the user to input the number of switches and bulbs, as well as the connections between them.
- **Count Valid Combinations**: The core functionality of the application calculates the number of valid combinations of switch states that light all bulbs according to their respective conditions.
- **User-Friendly Interface**: The application provides clear prompts and error messages to guide the user through the input process.

## Installation

To run the Light Bulb Switches application, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.6 or higher installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Dependencies**: Open your terminal or command prompt and run the following command to install the necessary dependencies:

   ```bash
   pip install typing
   ```

   Note: The `typing` module is included in Python 3.5 and later, so you may not need to install it separately if you're using a compatible version.

## How to Use the Application

1. **Run the Application**: Navigate to the directory where the application files (`main.py` and `light_bulb_logic.py`) are located. Run the application using the following command:

   ```bash
   python main.py
   ```

2. **Input the Number of Switches and Bulbs**: When prompted, enter the number of switches (N) and the number of bulbs (M). For example:

   ```
   Enter the number of switches (N): 3
   Enter the number of bulbs (M): 2
   ```

3. **Enter Connections**: Provide the connections for each bulb in the specified format. Each connection should list the switch indices followed by the required parity (0 or 1). Use a semicolon (;) to separate multiple connections. For example:

   ```
   Enter connections (format: switch1,switch2,...,parity; switch1,switch2,...,parity): 0,1,0; 1,2,1
   ```

   - In this example, the first bulb is connected to switches 0 and 1 and requires an even number of switches to be on (parity 0). The second bulb is connected to switches 1 and 2 and requires an odd number of switches to be on (parity 1).

4. **View Results**: After entering the connections, the application will calculate and display the number of valid combinations that light all bulbs:

   ```
   Valid combinations: 4
   ```

## Error Handling

The application includes error handling for various input scenarios, such as:

- Ensuring that the list of switches is not empty.
- Validating that the parity value is either 0 or 1.
- Providing clear messages for invalid input formats.

## Conclusion

The Light Bulb Switches application is a powerful tool for exploring the relationships between switches and bulbs. By following the instructions above, users can easily set up and run the application to find valid combinations that meet their specified conditions.

For any further assistance or feedback, please reach out to the support team.
```

This manual provides a comprehensive overview of the Light Bulb Switches application, including installation instructions, usage guidelines, and error handling. It is designed to be user-friendly and informative for potential users.