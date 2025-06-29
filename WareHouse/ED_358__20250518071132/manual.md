Here's a detailed user manual for the software that implements the `count_valid_strings` function. This manual provides an introduction to the main functions, installation instructions, and usage guidelines.

```markdown
# String Counter

A Python application for counting valid strings based on specified constraints for each uppercase English letter.

## Main Functions

The main function of this application is `count_valid_strings(K: int, C: List[int]) -> int`, which counts the number of valid strings of lengths from 1 to K, given constraints on the occurrences of each letter (A-Z). 

### Key Features:
- **Input Validation**: Ensures that the input values for K and C are within specified ranges.
- **Counting Logic**: Utilizes combinatorial mathematics to calculate valid string combinations based on the constraints provided.
- **Modular Arithmetic**: Applies modulus 998244353 to keep results manageable and prevent overflow.
- **Edge Case Handling**: Correctly handles cases where all constraints are zero, returning only the count for empty strings.

## Installation

To run the application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

This application requires no additional dependencies beyond the standard Python library. However, ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: If you have the source code, clone it to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Execute the main application file.
   ```bash
   python main.py
   ```

3. **Input Parameters**:
   - When prompted, enter the integer K (1-1000) which represents the maximum length of valid strings.
   - Enter the list of integers C (comma-separated, 0-1000) representing the maximum occurrences allowed for each letter from A to Z. Ensure that you provide exactly 26 integers.

   Example Input:
   ```
   Enter K (1-1000): 5
   Enter C (comma-separated, 0-1000): 1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
   ```

4. **Output**: The application will output the number of valid strings based on the provided constraints.
   ```
   Number of valid strings: <result>
   ```

## Example Usage

To see the application in action, consider the following example:

- Input:
  ```
  K = 3
  C = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ```
- Output:
  ```
  Number of valid strings: 19
  ```

## Troubleshooting

- **Input Error**: If you enter invalid values, the application will provide an error message indicating the nature of the error (e.g., out of range, incorrect number of integers).
- **ValueError**: Ensure that you are entering integers only. Non-integer inputs will raise a ValueError.

## Conclusion

This application is designed to help users count valid strings based on specific constraints for each letter. By following the installation and usage instructions, you can easily run the application and explore its capabilities.
```

This manual provides a comprehensive overview of the software, ensuring users can effectively install and utilize the application.