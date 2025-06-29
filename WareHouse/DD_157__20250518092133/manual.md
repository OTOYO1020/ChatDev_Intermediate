Here is the user manual for the Friendship Candidate Counter application, formatted in Markdown:

```markdown
# Friendship Candidate Counter

A Python application for counting potential friend candidates based on user friendships and blockships.

## Overview

The Friendship Candidate Counter allows users to input their friendships and blockships to determine how many potential friends each user has. The application processes the input data and applies specific conditions to identify friend candidates.

## Main Functions

- **count_friend_candidates(N: int, friendships: List[Tuple[int, int]], blockships: List[Tuple[int, int]]) -> List[int]**: 
  - This function takes the number of users, a list of friendships, and a list of blockships as input. It returns a list of counts representing the number of friend candidates for each user based on the defined conditions.

## Installation

To run the Friendship Candidate Counter, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies

The application requires no external libraries beyond the standard Python library. Ensure you have Python 3.x installed.

## How to Use

1. **Clone the Repository**: 
   Clone the repository containing the application files.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run the Application**: 
   Execute the main application file to start the program.

   ```bash
   python main.py
   ```

3. **Input Data**: 
   When prompted, enter the number of users (N), followed by the friendships and blockships in the specified format.

   - **Example Input**:
     ```
     Enter number of users (N): 4
     Enter friendships (e.g., 1,2; 2,3): 1,2; 2,3; 3,4
     Enter blockships (e.g., 1,3; 2,4): 1,3; 2,4
     ```

4. **View Results**: 
   After entering the data, the application will process the input and display the number of friend candidates for each user.

   - **Example Output**:
     ```
     Friend Candidates: [1, 1, 0, 0]
     ```

## Example Usage

To see how the application works, you can use the following example:

- **Input**:
  ```
  Enter number of users (N): 5
  Enter friendships (e.g., 1,2; 2,3): 1,2; 2,3; 3,4; 4,5
  Enter blockships (e.g., 1,3; 2,4): 1,3; 2,4
  ```

- **Output**:
  ```
  Friend Candidates: [1, 1, 1, 0, 0]
  ```

## Error Handling

The application includes basic error handling for invalid inputs. If you enter invalid user IDs or incorrect formats, the application will prompt you with an error message.

## Conclusion

The Friendship Candidate Counter is a straightforward tool for analyzing friendship dynamics among users. By following the instructions above, you can easily set up and use the application to explore potential friendships based on your input data.
```

This manual provides a comprehensive guide for users to understand the functionality of the application, how to install it, and how to use it effectively.