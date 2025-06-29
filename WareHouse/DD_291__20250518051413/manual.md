Here's a detailed user manual for the Card Flip application, formatted in Markdown as requested:

```markdown
# Card Flip Application

The Card Flip application allows users to calculate the number of valid configurations of card flips based on given conditions. This application is designed to help users understand how different configurations of card flips can lead to valid outcomes based on the values of two lists.

## Main Functions

- **count_valid_flips(N: int, A: List[int], B: List[int]) -> int**: This function calculates the number of valid configurations of card flips. It takes an integer `N` representing the number of cards, and two lists `A` and `B` representing the values of the cards in two different states. The function returns the count of valid configurations where adjacent cards have different face-up values.

## Installation

To run the Card Flip application, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Environment Dependencies

The application uses the Tkinter library for the graphical user interface. Tkinter is included with most Python installations, but if you need to install it separately, you can do so using the following command:

```bash
pip install tk
```

## How to Use the Application

1. **Run the Application**: 
   - Navigate to the directory where `main.py` is located.
   - Run the following command in your terminal or command prompt:
     ```bash
     python main.py
     ```

2. **Input Format**:
   - The application will prompt you to enter three values in the following format:
     ```
     N;A1,A2,...;B1,B2,...
     ```
   - Where:
     - `N` is the number of cards (an integer between 1 and 100).
     - `A1, A2, ...` are the values of the cards in the first state (comma-separated integers).
     - `B1, B2, ...` are the values of the cards in the second state (comma-separated integers).

3. **Example Input**:
   - For example, if you have 3 cards with values in list A as [1, 2, 3] and in list B as [3, 2, 1], you would enter:
     ```
     3;1,2,3;3,2,1
     ```

4. **Calculate Valid Flips**:
   - After entering the input, click the "Calculate Valid Flips" button.
   - The application will process the input and display the number of valid configurations based on the provided values.

5. **Error Handling**:
   - If the input format is incorrect or if `N` does not match the lengths of lists `A` and `B`, an error message will be displayed. Ensure to follow the specified input format for successful execution.

## Conclusion

The Card Flip application is a simple yet powerful tool for exploring the combinations of card flips and their outcomes. By following the instructions above, users can easily install and run the application to calculate valid configurations based on their input.

For any further assistance or inquiries, please feel free to reach out to our support team.
```

This manual provides a comprehensive guide for users to understand the application, its functionality, installation process, and usage instructions.