# Arena Clash User Manual

## Introduction

Arena Clash is an action game developed in Java where players engage in intense battles against each other in various arenas. The objective of the game is to defeat opponents using a combination of skill, strategy, and teamwork. The game features customizable characters, dynamic environments, and different game modes such as team deathmatch and capture the flag.

This user manual provides detailed instructions on how to install the necessary dependencies and how to use/play Arena Clash.

## Installation

To install and run Arena Clash, please follow these steps:

1. Make sure you have Java Development Kit (JDK) installed on your system. If not, you can download it from the official Oracle website: [Java SE Downloads](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).

2. Download the Arena Clash source code from the provided repository.

3. Extract the downloaded source code to a directory of your choice.

4. Open a command prompt or terminal and navigate to the extracted directory.

5. Compile the Java source code by running the following command:

   ```
   javac Main.java
   ```

6. Once the compilation is successful, you can run the game by executing the following command:

   ```
   java Main
   ```

7. The game will start, and you will see the graphical user interface (GUI) window.

## Gameplay

Upon starting the game, you will be presented with the GUI window. The GUI window contains a button labeled "Click Me" and a label displaying "Hello World!".

To play the game, follow these steps:

1. Click the "Click Me" button to initiate an action.

2. The label will change to "Button Clicked".

3. The game logic will be executed in the background, simulating the battle between two characters in the chosen arena.

4. The game will continue until one of the characters' health reaches zero.

5. Once the battle is over, the game will display the winner or declare a draw.

6. You can close the game window at any time to exit the game.

## Customization

Arena Clash allows you to customize characters and arenas. To customize the game, you can modify the following files:

- `Character.java`: This file contains the `Character` class, which represents a player character in the game. You can modify the character's name, playstyle, health, attack, and defense attributes.

- `Arena.java`: This file contains the `Arena` class, which represents a battle arena in the game. You can modify the arena's name, width, and height attributes.

Make sure to recompile the Java source code after making any modifications using the `javac Main.java` command.

## Conclusion

Congratulations! You have successfully installed and played Arena Clash. Enjoy the intense battles and strive to become the ultimate champion!

If you encounter any issues or have any questions, please refer to the provided documentation or contact our support team for assistance.