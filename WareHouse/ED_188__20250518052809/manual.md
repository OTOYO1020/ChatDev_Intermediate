```markdown
# Gold Profit Calculator

The Gold Profit Calculator is a software application designed to help users determine the maximum profit that can be achieved from trading gold across different towns connected by roads. The application allows users to input the number of towns, the number of roads, the gold prices in each town, and the connections between towns, and then calculates the potential profit based on these inputs.

## Main Functions

1. **Input Fields**:
   - **Number of Towns (N)**: Enter the total number of towns.
   - **Number of Roads (M)**: Enter the total number of roads connecting the towns.
   - **Gold Prices**: Provide a comma-separated list of gold prices for each town.
   - **Roads**: Enter the roads connecting the towns in the format `town1,town2;...`.

2. **Calculate Profit**: 
   - Click the "Calculate Profit" button to compute the maximum profit based on the provided inputs.

3. **Result Display**: 
   - The application will display the maximum profit in a message box.

## Installation Guide

To run the Gold Profit Calculator, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: 
   - Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: 
   - Open your command line interface (CLI) and run the following command to install the required dependencies:
   ```bash
   pip install tkinter
   ```

3. **Download the Application Files**: 
   - Clone or download the repository containing the application files: `main.py`, `graph.py`, and `profit_calculator.py`.

## How to Use the Application

1. **Launch the Application**:
   - Run the `main.py` file using Python. You can do this by navigating to the directory containing the file in your CLI and executing:
   ```bash
   python main.py
   ```

2. **Input Data**:
   - Fill in the input fields:
     - Enter the number of towns (N).
     - Enter the number of roads (M).
     - Provide the gold prices as a comma-separated list (e.g., `100,200,150`).
     - Specify the roads in the format `town1,town2;town3,town4;...` (e.g., `1,2;2,3;1,3`).

3. **Calculate Profit**:
   - Click the "Calculate Profit" button to compute the maximum profit based on the inputs.

4. **View Results**:
   - A message box will appear displaying the maximum profit that can be achieved.

## Example Usage

- **Input**:
  - Number of Towns (N): `3`
  - Number of Roads (M): `3`
  - Gold Prices: `100,200,150`
  - Roads: `1,2;2,3;1,3`

- **Output**:
  - Maximum Profit: `100` (if the best trading strategy is applied).

## Troubleshooting

- Ensure that the number of gold prices matches the number of towns.
- Verify that the roads are entered in the correct format.
- If you encounter any errors, check the input values for correctness and format.

## Conclusion

The Gold Profit Calculator is a powerful tool for analyzing potential profits from gold trading across interconnected towns. With its user-friendly interface and straightforward calculations, users can easily determine the best trading strategies to maximize their profits.
```