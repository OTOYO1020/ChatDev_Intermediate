Here is the user manual for the rope cycle counting application, formatted in Markdown:

```markdown
# Rope Cycle Counting Application

This application is designed to manage rope connections and count cycles formed by these connections. It allows users to tie ends of ropes together based on specified colors and determine whether the resulting structure forms cycles or not.

## Main Functions

- **Tie Ends**: Connect two ends of ropes with specified colors, ensuring that no end with the same color is tied multiple times.
- **Count Cycles and Non-Cycles**: After processing all operations, the application counts the number of connected groups of ropes that form cycles and those that do not.

## Installation

To run the application, you need to have Python installed on your machine. You can install the required dependencies using pip. Open your terminal and run the following command:

```bash
pip install -r requirements.txt
```

Make sure to create a `requirements.txt` file with the necessary dependencies if you have any specific libraries to include.

## How to Use the Application

1. **Run the Application**: Start the application by executing the `main.py` file. You can do this from your terminal:

    ```bash
    python main.py
    ```

2. **Input the Number of Ropes and Operations**:
    - When prompted, enter the number of ropes (N) as an integer.
    - Enter the number of operations (M) as an integer.

3. **Enter Operations**:
    - For each operation, input the details in the format: `end1 color1 end2 color2`.
    - For example, to tie end 0 with color 'red' to end 1 with color 'blue', you would enter:
      ```
      0 red 1 blue
      ```

4. **View Results**:
    - After entering all operations, the application will process the connections and output the number of cycles and non-cycles in the format:
      ```
      Number of cycles: X, Number of non-cycles: Y
      ```

## Edge Cases

- If the number of operations (M) is 0, the application will automatically return:
  ```
  Number of cycles: 0, Number of non-cycles: N
  ```

## Example Usage

```plaintext
Enter the number of ropes (N): 5
Enter the number of operations (M): 3
Enter operation (end1 color1 end2 color2): 0 red 1 blue
Enter operation (end1 color1 end2 color2): 1 blue 2 green
Enter operation (end1 color1 end2 color2): 2 green 0 red
Number of cycles: 1, Number of non-cycles: 0
```

## Conclusion

This application provides a simple yet effective way to manage rope connections and analyze their structure for cycles. It is a useful tool for anyone needing to visualize and understand the relationships between different ends of ropes based on color connections.
```

This manual provides a comprehensive overview of the application, including its main functions, installation instructions, usage guidelines, and example interactions. Let me know if you need any further modifications or additional information!