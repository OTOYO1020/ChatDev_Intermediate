Here is the user manual for the Distance Calculator software, formatted in Markdown:

```markdown
# Distance Calculator

A simple application to calculate the distance between points represented by uppercase letters A-G.

## Main Functions

The Distance Calculator allows users to:
- Input two uppercase letters (A-G) representing points.
- Calculate the distance between these points based on predefined positions.
- Receive feedback on invalid inputs to ensure correct usage.

## Quick Install

To run the Distance Calculator, you need to have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

*Note: Ensure that you have a `requirements.txt` file that includes any necessary dependencies.*

## 🤔 What is this?

The Distance Calculator is designed to help users find the distance between two points defined by uppercase letters A through G. Each letter corresponds to a specific position, and the application calculates the absolute distance between these points based on their respective positions.

## How to Use

1. **Run the Application**: 
   Execute the main application file `main.py` in your terminal or command prompt.

   ```bash
   python main.py
   ```

2. **Input Points**:
   - You will be prompted to enter the first point (p). Type an uppercase letter (A-G) and press Enter.
   - If the input is invalid, you will be prompted to enter the point again until a valid input is provided.
   - Next, you will be prompted to enter the second point (q) in the same manner.

3. **View Results**:
   - After entering both points, the application will calculate and display the distance between the two points.

## Example Usage

```plaintext
Enter point p (A-G): A
Enter point q (A-G): C
Distance between A and C: 4
```

## Error Handling

- If you enter an invalid point (not an uppercase letter A-G), the application will notify you and ask for the input again.
- If both points are valid, the application will calculate the distance and display it.

## 📖 Documentation

For more detailed information about the code structure and functionality, please refer to the source code files:
- `main.py`: The main application file that handles user input and output.
- `distance_calculator.py`: The module that contains the logic for calculating distances.

Feel free to reach out for support or further inquiries regarding the Distance Calculator application.
```

This manual provides a comprehensive overview of the Distance Calculator software, including installation instructions, usage guidelines, and error handling information.