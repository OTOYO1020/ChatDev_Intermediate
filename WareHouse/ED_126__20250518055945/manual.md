Here's the `manual.md` file for the software, detailing the main functions, installation instructions, and usage guidelines.

```markdown
# Minimum Cost to Determine Cards

This software provides a solution to calculate the minimum cost required to determine card values based on specified conditions. It utilizes a greedy approach and union-find data structure to efficiently manage and evaluate parity conditions.

## Main Functions

- **Input Handling**: The software allows users to input the number of cards (N), the number of conditions (M), and the conditions themselves in a user-friendly manner.
- **Calculation Logic**: The core function `minimum_cost_to_determine_cards(N, M, conditions)` processes the input and calculates the minimum number of magic uses required to satisfy all conditions.
- **Output Display**: The results are presented clearly, indicating either the minimum cost or an error message if conditions cannot be satisfied.

## Installation Instructions

To run this software, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository**:
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
   # Add any required libraries here
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use the Software

### Console Application

1. **Run the Application**:
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input Values**:
   - Enter the number of cards (N).
   - Enter the number of conditions (M).
   - Input conditions in the format `X Y Z` (one per line). Type `done` when finished.

3. **View Results**:
   The application will calculate and display the minimum cost required to determine the card values based on the provided conditions.

### GUI Application

1. **Run the GUI Application**:
   Execute the main application file:
   ```bash
   python main.py
   ```

2. **Input Values**:
   - Fill in the number of cards (N) and the number of conditions (M) in the respective fields.
   - Enter conditions in the format `X Y Z` separated by commas in the conditions field.

3. **Calculate**:
   Click the "Calculate" button to process the input and display the result.

## Error Handling

- The software includes error handling for invalid inputs, such as non-integer values or conditions that exceed the specified limits.
- If the conditions cannot be satisfied, an appropriate error message will be displayed.

## Future Enhancements

This software is designed with potential future enhancements in mind. Libraries like NumPy or Pandas may be integrated to improve performance and functionality.

For any issues or feature requests, please reach out to our support team.

```

This manual provides a comprehensive overview of the software, ensuring users can easily understand how to install and utilize it effectively.