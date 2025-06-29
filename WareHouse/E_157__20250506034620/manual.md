Here's a detailed user manual for the string manipulation application, formatted in Markdown as requested:

```markdown
# String Manipulation Application

A powerful tool for managing strings and counting unique characters efficiently.

## Quick Install

To run the application, ensure you have Python installed on your machine. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

This application allows users to manipulate a string by updating characters and querying the number of unique characters within specified substrings. It is designed to handle multiple queries efficiently, making it suitable for applications that require dynamic string operations.

### Main Functions

1. **Update Character**: Change a character at a specified position in the string.
2. **Count Unique Characters**: Retrieve the number of unique characters in a substring defined by start and end positions.

## 📖 How to Use

### Step 1: Prepare Your Environment

Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### Step 2: Clone the Repository

Clone the repository containing the application files:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 3: Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

You can run the application by executing the following command in your terminal:

```bash
python main.py
```

### Step 5: Input Format

When prompted, input the following:

1. **N and Q**: The first line should contain two integers, N (length of the string) and Q (number of queries).
2. **String S**: The second line should contain the string of length N consisting of lowercase English letters.
3. **Queries**: For each query, input the following:
   - For **Type 1** (Update Character): Input `1 i_q c_q` where `i_q` is the position (1-based index) and `c_q` is the new character.
   - For **Type 2** (Count Unique Characters): Input `2 l_q r_q` where `l_q` is the start position and `r_q` is the end position (1-based index).

### Example Usage

```plaintext
Input:
5 3
abcde
1 2 z
2 1 5
1 1 a
2 1 3

Output:
4
```

### Explanation of Example

- The initial string is "abcde".
- The first query updates the character at position 2 to 'z', resulting in "azcde".
- The second query counts unique characters in the substring "azcde", which are 'a', 'z', 'c', 'd', 'e' (total 4).
- The third query updates the character at position 1 to 'a' (no change).
- The fourth query counts unique characters in the substring "azc", which are 'a', 'z', 'c' (total 3).

## 📚 Additional Information

For further details on how the application works, you can refer to the source code in `main.py` and `string_manager.py`. These files contain the logic for handling string updates and counting unique characters.

For any issues or feature requests, please reach out to our support team.

Happy string manipulation!
```

This manual provides a comprehensive guide for users to understand how to install, run, and utilize the string manipulation application effectively.