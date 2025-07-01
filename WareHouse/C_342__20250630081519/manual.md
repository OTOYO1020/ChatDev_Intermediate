Here’s a detailed user manual for the character replacement application, formatted in Markdown:

```markdown
# Character Replacement Application

This application allows users to perform character replacements in a given string based on specified operations. It reads a string and a series of character pairs, replacing occurrences of specified characters with new ones.

## Main Functions

- **Input Handling**: Reads the integer values for the length of the string and the number of operations, as well as the string itself and the character pairs for replacement.
- **Character Replacement**: Processes the string by replacing specified characters according to the provided operations.
- **Output Display**: Outputs the modified string after all replacements have been applied.

## Quick Install

To run the Character Replacement Application, you need to have Python installed on your machine. You can install the required dependencies using pip. 

```bash
pip install -r requirements.txt
```

Make sure to create a `requirements.txt` file with the necessary dependencies if you have any specific libraries to include.

## How to Use the Application

1. **Input Format**:
   - The first line should contain two integers, `N` (length of the string) and `Q` (number of operations).
   - The second line should contain the string `S` of length `N`.
   - The next `Q` lines should each contain a pair of characters `c_i` and `d_i`, separated by a space, where `c_i` is the character to be replaced and `d_i` is the character to replace it with.

2. **Running the Application**:
   - Save the provided code into three files: `main.py`, `input_handler.py`, and `output_display.py`.
   - Run the application using the command:
     ```bash
     python main.py
     ```

3. **Example Input**:
   ```
   5 2
   hello
   h y
   o a
   ```

   In this example:
   - The string `S` is "hello".
   - There are 2 operations: replace 'h' with 'y' and 'o' with 'a'.

4. **Expected Output**:
   ```
   yella
   ```

   After applying the operations, the modified string will be "yella".

## Error Handling

- The application checks for valid input:
  - `N` must be a positive integer and `Q` must be a non-negative integer.
  - The length of the string `S` must match `N`.
  - Each operation must consist of exactly two characters.

If any of these conditions are not met, the application will print an error message and terminate.

## Additional Notes

- Ensure that the input is provided in the correct format to avoid runtime errors.
- The application is designed to handle multiple character replacements efficiently.

For any further questions or support, please contact our support team.
```

This manual provides a comprehensive overview of the application, including installation instructions, usage guidelines, and error handling, ensuring that users can effectively utilize the character replacement functionality.