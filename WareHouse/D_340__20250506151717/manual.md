```markdown
# Stage Time Calculator

The Stage Time Calculator is a user-friendly application designed to compute the minimum time required to clear multiple stages using two different actions. This manual provides an overview of the software's main functions, installation instructions, and usage guidelines.

## Main Functions

- **Input Stages**: Users can input the number of stages (N) and the time required for each action (A and B) to clear the stages.
- **Calculate Minimum Time**: The application calculates the minimum time required to reach the final stage (N) based on the provided inputs.
- **Output Results**: The results are displayed in a user-friendly interface, showing the minimum time or an error message if the input is invalid.

## Installation Instructions

To run the Stage Time Calculator, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Open your terminal or command prompt and run the following command to install the necessary libraries:
   ```bash
   pip install tkinter
   ```

3. **Download the Application Files**: Clone or download the application files (`main.py`, `input_frame.py`, `output_frame.py`) from the repository.

## How to Use the Application

1. **Run the Application**: Navigate to the directory where you saved the application files and run the following command:
   ```bash
   python main.py
   ```

2. **Input Data**:
   - Enter the number of stages (N) in the first input field.
   - In the second input field, enter the times for Action A as a comma-separated list (e.g., `2,3,1`).
   - In the third input field, enter the times for Action B as a comma-separated list (e.g., `4,2,3`).
   - In the fourth input field, enter the accessible stages (X) as a comma-separated list (e.g., `2,3,4`).

3. **Calculate Minimum Time**: Click the "Calculate" button to compute the minimum time required to reach stage N.

4. **View Results**: The result will be displayed below the input fields, showing either the minimum time in seconds or an error message if the input is invalid.

## Example Usage

- **Input**:
  - Number of Stages (N): `4`
  - Times for Action A: `2,3,1`
  - Times for Action B: `4,2,3`
  - Accessible Stages: `2,3,4`

- **Output**: 
  - Minimum time to reach stage 4: `5 seconds`

## Troubleshooting

- If you encounter any input errors, ensure that:
  - N is greater than 1.
  - The lengths of A, B, and X are exactly N-1.
  - All inputs are valid integers.

For further assistance, please refer to the code comments or reach out to the development team.

## Conclusion

The Stage Time Calculator is a powerful tool for calculating the minimum time to clear stages using different actions. With its intuitive interface and straightforward functionality, users can efficiently determine the best path to success in their stage-based challenges.
```