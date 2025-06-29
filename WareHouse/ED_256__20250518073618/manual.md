Here's a detailed user manual for the software, formatted in Markdown as requested:

```markdown
# Frustration Calculator

A Python application designed to calculate the minimum possible sum of frustration based on dislikes among a group of people.

## Overview

The Frustration Calculator allows users to input a number of people and their dislike relationships, along with associated frustration costs. The application then computes the optimal order of giving candies to minimize total frustration.

## Main Functions

- **Input Handling**: The application reads the number of people and their dislikes from user input.
- **Frustration Calculation**: Using a graph-based approach, the application calculates the minimum frustration based on the dislikes provided.
- **Output**: Displays the minimum frustration sum to the user.

## Installation

To run the Frustration Calculator, ensure you have Python installed on your machine. Follow these steps to set up the environment:

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   You may need to install the required libraries. Use the following command:
   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, ensure you have the following libraries:
   - `collections`
   - `heapq`
   - `typing`

3. **Run the Application**:
   Execute the main application file:
   ```bash
   python main.py
   ```

## How to Use

1. **Start the Application**:
   Run the `main.py` file as described above. The application will prompt you for input.

2. **Input the Number of People**:
   Enter the total number of people (N). For example:
   ```
   Enter number of people (N): 5
   ```

3. **Input the Dislikes**:
   Enter the dislikes in the format: `person1,person2,cost;...`. For example:
   ```
   Enter dislikes (format: person1,person2,cost;...): 0,1,10;1,2,20;0,2,30
   ```

   Each dislike should be separated by a semicolon, and each dislike entry should consist of two people and the associated cost.

4. **View the Result**:
   After entering the dislikes, the application will calculate and display the minimum frustration:
   ```
   Minimum Frustration: 30
   ```

## Example Usage

Here’s an example of how to use the application:

1. Start the application:
   ```
   python main.py
   ```

2. Input:
   ```
   Enter number of people (N): 3
   Enter dislikes (format: person1,person2,cost;...): 0,1,5;1,2,10;0,2,15
   ```

3. Output:
   ```
   Minimum Frustration: 15
   ```

## Testing

The application has been designed to handle up to 200,000 people efficiently. You can test the function with various cases to validate correctness and performance.

## Conclusion

The Frustration Calculator is a powerful tool for determining optimal candy distribution among a group of people based on their dislikes. By following the instructions above, users can easily set up and utilize the application to minimize frustration in various scenarios.
```

This manual provides a comprehensive guide for users to understand the functionality, installation process, and usage of the Frustration Calculator application.