Here's the `manual.md` file for the Player Assignment App, detailing its main functions, installation instructions, and usage guidelines.

```markdown
# Player Assignment App

A Python application for managing player assignments in competitive rounds.

## Quick Install

To run the Player Assignment App, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can set up the environment and install the required dependencies using pip:

```bash
pip install random
```

## 🤔 What is this?

The Player Assignment App is designed to facilitate the assignment of players to competitive rounds in a structured manner. It ensures that players do not face the same opponents more than once throughout the rounds, while also rotating player identifiers after each round.

### Main Features

- **Dynamic Player Assignment**: Automatically assigns players to matches while ensuring no player faces the same opponent more than once.
- **Player Rotation**: After each round, player identifiers are incremented, and if they exceed the total number of players, they wrap around to the beginning.
- **Customizable Rounds**: Users can specify the number of players (N) and the number of rounds (M) for the assignments.

## 📖 How to Use

1. **Run the Application**: 
   - Open a terminal or command prompt.
   - Navigate to the directory where `main.py` is located.
   - Run the application using the command:
     ```bash
     python main.py
     ```

2. **Input Parameters**:
   - When prompted, enter the number of players (N) as an integer.
   - Next, enter the number of rounds (M) as an integer.

3. **View Assignments**:
   - The application will output the assignments in the format `PlayerID vs OpponentID` for each match.

### Example Usage

```bash
$ python main.py
5
3
```

This input means there are 5 players and 3 rounds. The output will display the matchups for each round.

## 📄 Code Structure

- **main.py**: The main application file that handles player assignment logic and user interaction.
- **player.py**: A module containing the `Player` class, which manages player data and tracks opponents faced.

## 🛠️ Dependencies

The application primarily relies on Python's built-in libraries. Ensure you have Python 3.x installed to avoid compatibility issues.

## 🤝 Support

For any issues or feature requests, please reach out to our support team via the provided contact methods in the repository.

Happy Playing!
```

This manual provides a comprehensive overview of the Player Assignment App, ensuring users can easily understand how to install and utilize the software effectively.