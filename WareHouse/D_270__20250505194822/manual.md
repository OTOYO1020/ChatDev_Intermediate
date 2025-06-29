```markdown
# Stone Removal Game

Welcome to the Stone Removal Game! This application allows two players, Takahashi and Aoki, to take turns removing stones from a pile based on specified moves. The goal is to determine how many stones Takahashi can remove before the pile is empty.

## Main Functions

- **Input Handling**: The application prompts the user to enter the number of stones (N) and the number of possible moves (K), followed by the moves themselves.
- **Game Logic**: The game alternates turns between Takahashi and Aoki, where each player removes the maximum possible stones from the pile based on the available moves.
- **Output**: After the game concludes, the application displays the total number of stones removed by Takahashi.

## Installation

To run the Stone Removal Game, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the game files to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**: This application does not require any external libraries, so you can run it directly with Python.

## How to Use/Play the Game

1. **Run the Application**: Open your terminal or command prompt, navigate to the directory where the game files are located, and run the following command:
   ```bash
   python main.py
   ```

2. **Input the Number of Stones**: When prompted, enter the total number of stones (N). Ensure that it is a positive integer.

3. **Input the Number of Moves**: Next, enter the number of possible moves (K). This should also be a positive integer.

4. **Input the Moves**: Finally, input the sequence of possible moves separated by spaces. Ensure that the number of moves matches the value of K you entered earlier.

5. **View the Results**: After all inputs are provided, the game will execute, and you will see the total number of stones removed by Takahashi displayed on the screen.

## Example

```
Enter the number of stones (N): 10
Enter the number of possible moves (K): 3
Enter the possible moves separated by space: 3 5 7
Takahashi removed 10 stones.
```

## Conclusion

The Stone Removal Game is a simple yet engaging application that demonstrates basic game logic and user interaction in Python. Enjoy playing and testing your strategy against Aoki!

For any issues or feedback, please reach out to the development team.
```