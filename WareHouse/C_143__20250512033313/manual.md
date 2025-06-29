Here's the user manual for the Slime Counter application, formatted in Markdown as requested:

```markdown
# Slime Counter

A simple application for counting distinct slimes after fusion based on their colors.

## Quick Install

To run the Slime Counter application, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can set up the environment by installing the necessary dependencies. For this application, there are no external dependencies required beyond Python itself.

## 🤔 What is this?

The Slime Counter application allows users to input a string representing the colors of slimes. The application processes the input to count the number of distinct slimes after fusion, where slimes of the same color that are adjacent to each other are considered fused into one.

### Main Functions

- **count_fused_slimes(S: str) -> int**: This function takes a string `S` as input and returns the count of distinct slimes after fusion. It handles edge cases such as empty strings and single-character strings.

## 📖 How to Use

1. **Clone the Repository**: If you haven't already, clone the repository containing the Slime Counter application.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: Open a terminal and navigate to the directory where the `main.py` file is located. Run the application using the following command:

   ```bash
   python main.py
   ```

3. **Input Slime Colors**: When prompted, enter a string of characters representing the colors of the slimes. For example:

   ```
   Enter Slime Colors: RRGGBBYY
   ```

4. **View Results**: The application will output the number of distinct slimes after fusion. For the above input, the output will be:

   ```
   Distinct Slimes: 4
   ```

## 🧪 Testing the Function

You can test the `count_fused_slimes` function with various input cases to ensure its correctness. Here are some examples:

- Input: `""` (empty string) → Output: `0`
- Input: `"A"` (single character) → Output: `1`
- Input: `"AAABBBCCDA"` → Output: `5`
- Input: `"RGBRGBRGB"` → Output: `3`

## 📚 Additional Information

For more details on the implementation, you can review the source code in the `slime_counter.py` file. This file contains the logic for counting distinct slimes and handles various edge cases.

If you have any questions or need further assistance, feel free to reach out!

```

This manual provides a comprehensive overview of the Slime Counter application, including installation instructions, usage guidelines, and examples for testing the function. Let me know if you need any adjustments or additional information!