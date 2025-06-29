Here's a detailed user manual for the string validation software, formatted in Markdown as requested:

```markdown
# String Validation Tool

This software is designed to validate a specific string format based on predefined criteria. It checks for the presence and positioning of certain characters within the string.

## Main Functions

The primary function of this software is to validate a string of length 8 based on the following rules:

1. The string must contain exactly:
   - One 'K'
   - One 'Q'
   - Two 'R's
   - Two 'B's
   - Two 'N's

2. The software checks the positions of 'B' characters to ensure they do not share the same parity (both even or both odd).

3. The software verifies that the 'K' character is positioned between the two 'R' characters.

4. If all conditions are satisfied, the software returns 'VALID'. If any condition fails, it returns 'INVALID' with a specific error message.

## Installation

To run this software, you need to have Python installed on your machine. Follow the steps below to set up the environment:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   Create a `requirements.txt` file with the following content (if you plan to add dependencies in the future):
   ```
   # Placeholder for future dependencies
   ```

   Then, install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   You can run the application by executing the `main.py` file:
   ```bash
   python main.py
   ```

## How to Use

1. **Input the String**:
   When prompted, enter a string of exactly 8 characters consisting of the allowed characters: 'K', 'Q', 'R', 'B', and 'N'.

2. **Receive Validation Result**:
   After entering the string, the software will validate it based on the specified criteria and print either 'VALID' or 'INVALID' along with a message explaining the reason for invalidation if applicable.

### Example Usage

- **Valid Input**:
  ```
  Enter a string of length 8 consisting of exactly one 'K', one 'Q', two 'R's, two 'B's, and two 'N's: KQRBNRBN
  VALID
  ```

- **Invalid Input**:
  ```
  Enter a string of length 8 consisting of exactly one 'K', one 'Q', two 'R's, two 'B's, and two 'N's: KQRBBRNN
  INVALID: Both 'B' characters have the same parity.
  ```

## Conclusion

This String Validation Tool is a straightforward application that ensures input strings conform to specific character and positional requirements. For any further assistance or feature requests, please contact the development team.
```

This manual provides a comprehensive overview of the software, including its functionality, installation instructions, and usage guidelines.