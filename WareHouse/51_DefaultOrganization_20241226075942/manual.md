# Board Game Turn Timer User Manual

## Introduction

The Board Game Turn Timer is a software application developed in Java that provides a customizable timer for turn-based board games. It allows players to set a specific time limit for each turn and displays a countdown timer during gameplay. When the time is up, the software automatically moves to the next player.

## Installation

To use the Board Game Turn Timer, you need to have Java installed on your computer. You can download and install Java from the official website: [Java Download](https://www.java.com/en/download/)

Once Java is installed, you can proceed with the following steps to run the application:

1. Download the source code files from the provided repository.

2. Open a command prompt or terminal and navigate to the directory where you downloaded the source code files.

3. Compile the Java source code files using the following command:

   ```
   javac *.java
   ```

4. Run the application using the following command:

   ```
   java Main
   ```

   This will start the application and display the main window.

## Usage

The Board Game Turn Timer application provides a simple and intuitive user interface for setting up and managing the turn timer. Here's how you can use it:

1. Start the application by following the installation instructions.

2. The main window of the application will appear. It contains a button labeled "Start Turn" and a label displaying the current player's turn.

3. To start a turn, click on the "Start Turn" button. This will start the timer with a default time limit of 60 seconds.

4. The label will display the remaining time for the current turn. The timer will count down from the specified time limit.

5. When the time is up, the software will automatically move to the next player. The label will update to display the next player's turn.

6. To set a custom time limit for each turn, you can modify the code in the `ButtonClickListener` class in the `gui.java` file. Look for the line `startTimer(60);` and change the value `60` to your desired time limit in seconds.

7. You can customize the user interface and add additional features to the application by modifying the Java source code files.

## Dependencies

The Board Game Turn Timer application has the following dependencies:

- Java Development Kit (JDK): The application requires Java to be installed on your computer. You can download and install Java from the official website: [Java Download](https://www.java.com/en/download/)

## Conclusion

The Board Game Turn Timer is a simple and easy-to-use software application for managing turn-based board games. It provides a customizable timer that helps players keep track of their turns and ensures a fair gameplay experience. By following the installation and usage instructions provided in this user manual, you can easily set up and use the application for your board game sessions.