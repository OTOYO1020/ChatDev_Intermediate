Here is the user manual for the Bulb Switch application, formatted in Markdown:

```markdown
# Bulb Switch Application

A simple application to determine the number of valid combinations of switch states that can light up all connected bulbs based on user-defined conditions.

## Quick Install

To run the Bulb Switch application, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can install any required dependencies using pip. Open your terminal or command prompt and run:

```bash
pip install -r requirements.txt
```

*Note: If you don't have a `requirements.txt` file, the application currently does not have external dependencies beyond Python's standard library.*

## 🤔 What is this?

The Bulb Switch application allows users to define a set of switches and bulbs, where each bulb can be lit based on the state of its connected switches. Users can specify the number of switches and bulbs, the connections between them, and the required parity for each bulb to be lit.

### Main Functions

- **Read Input:** The application prompts the user to enter the number of switches (N) and bulbs (M).
- **Define Bulb Conditions:** For each bulb, users can specify:
  - The number of switches connected to the bulb.
  - The specific switches that control the bulb.
  - The required parity (0 or 1) for the bulb to be lit.
- **Count Valid Combinations:** The application calculates and displays the total number of valid combinations of switch states that can light all bulbs according to the defined conditions.

## 📖 How to Use

1. **Run the Application:**
   To start the application, navigate to the directory containing `main.py` and run the following command in your terminal:

   ```bash
   python main.py
   ```

2. **Input Data:**
   - When prompted, enter the number of switches (N) and bulbs (M) separated by a space.
   - For each bulb, you will be prompted to:
     - Enter the number of switches connected to that bulb.
     - Enter the specific switch numbers (space-separated).
     - Enter the required parity (0 or 1) for the bulb to be lit.

3. **View Results:**
   After entering all the required data, the application will calculate and display the total number of valid combinations of switch states that can light all bulbs.

## Example Usage

```
Enter number of switches (N) and bulbs (M): 3 2
Enter number of switches for bulb 1: 2
Enter 2 switch numbers for bulb 1 (space-separated): 1 2
Enter required parity for bulb 1 (0 or 1): 1
Enter number of switches for bulb 2: 1
Enter 1 switch numbers for bulb 2 (space-separated): 3
Enter required parity for bulb 2 (0 or 1): 0
Total valid combinations: 2
```

## Support

If you encounter any issues or have questions about the Bulb Switch application, please reach out to our support team at support@chatdev.com.

Thank you for using the Bulb Switch application!
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and example interactions to help users effectively utilize the software.