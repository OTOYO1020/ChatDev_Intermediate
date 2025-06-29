```markdown
# Amoeba Generation Distance Calculator

The Amoeba Generation Distance Calculator is a Python application designed to calculate the generation distances of amoebae based on their parent-child relationships. This software allows users to input the number of amoebae and their respective parent amoebae, and it outputs the generation distances for each amoeba.

## Main Functions

1. **Input Handling**: The application reads the number of amoebae (N) and their parent amoebae from standard input.
2. **Data Structure Initialization**: It initializes lists to store parent relationships and generation distances.
3. **Breadth-First Search (BFS)**: The application uses BFS to calculate the generation distance of each amoeba from the root amoeba (amoeba 1).
4. **Output Generation**: It prints the generation distances for amoebae from 1 to 2N + 1.

## Installation

To run the Amoeba Generation Distance Calculator, you need to install the required dependencies. Follow the steps below:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   pandas
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Software

### Running the Application

1. **Execute the Main Application**:
   Run the main application file using Python:
   ```bash
   python main.py
   ```

2. **Input the Number of Records**:
   When prompted, enter the integer value for N, which represents the number of amoebae.

3. **Input Parent Amoebae**:
   For each amoeba from 1 to N, you will be prompted to enter the parent amoeba. Ensure that the parent amoeba is within the valid range (1 to N). You have up to three attempts to enter a valid parent amoeba.

4. **View Results**:
   After entering all the data, the application will calculate and display the generation distances for amoebae 1 to 2N + 1 in a single line, separated by spaces.

### Example Usage

```plaintext
Enter the number of records: 3
Please enter the parent amoeba for amoeba 1 (valid range: 1 to 3): 1
Please enter the parent amoeba for amoeba 2 (valid range: 1 to 3): 1
Please enter the parent amoeba for amoeba 3 (valid range: 1 to 3): 2
0 1 1 2 2
```

## Additional Features

- **Excel Integration**: The software includes an Excel handler (`excel_handler.py`) that allows you to read amoeba data from an Excel file. You can modify the `ExcelHandler` class to customize how data is read.

## Conclusion

The Amoeba Generation Distance Calculator is a powerful tool for understanding the hierarchical relationships among amoebae. By following the instructions above, you can easily set up and run the application to calculate generation distances based on your input data.
```