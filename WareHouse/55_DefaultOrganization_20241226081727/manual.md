# Board Game Turn Order Randomizer User Manual

## Introduction

The Board Game Turn Order Randomizer is a software application developed in Java that ensures fair gameplay by randomizing the turn order for board games. It eliminates any bias or advantage associated with a predetermined turn order, creating a balanced gaming experience. This user manual provides detailed instructions on how to install and use the software.

## Installation

To use the Board Game Turn Order Randomizer, you need to have Java installed on your system. Follow these steps to install Java:

1. Visit the Oracle website (https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) and download the Java Development Kit (JDK) for your operating system.
2. Run the installer and follow the on-screen instructions to complete the installation.

## Dependencies

The Board Game Turn Order Randomizer has the following dependencies:

- javax.swing-api 1.0.0

To install the dependencies, follow these steps:

1. Create a new file named `requirements.txt`.
2. Add the following line to the `requirements.txt` file:

```
javax.swing-api==1.0.0
```

3. Save the `requirements.txt` file.

To install the dependencies, open a terminal or command prompt and navigate to the directory where the `requirements.txt` file is located. Run the following command:

```
pip install -r requirements.txt
```

## Usage

To use the Board Game Turn Order Randomizer, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the Java files (`main.java`, `gui.java`, `controller.java`, `data.java`) are located.
3. Compile the Java files by running the following command:

```
javac *.java
```

4. Run the application by executing the following command:

```
java Main
```

5. The application window will open. Enter the number of players and their names in the input field separated by commas (e.g., "4, Player1, Player2, Player3, Player4").
6. Click the "Submit" button.
7. The turn order will be displayed in the text area below.

## Example

Here is an example of how to use the Board Game Turn Order Randomizer:

1. Open a terminal or command prompt.
2. Navigate to the directory where the Java files (`main.java`, `gui.java`, `controller.java`, `data.java`) are located.
3. Compile the Java files by running the following command:

```
javac *.java
```

4. Run the application by executing the following command:

```
java Main
```

5. The application window will open. Enter the number of players and their names in the input field separated by commas (e.g., "4, Player1, Player2, Player3, Player4").
6. Click the "Submit" button.
7. The turn order will be displayed in the text area below.

## Conclusion

The Board Game Turn Order Randomizer is a simple and easy-to-use software application that ensures fair gameplay by randomizing the turn order for board games. By following the installation and usage instructions provided in this user manual, you can easily incorporate it into your board game sessions and create a balanced gaming experience. Enjoy playing!