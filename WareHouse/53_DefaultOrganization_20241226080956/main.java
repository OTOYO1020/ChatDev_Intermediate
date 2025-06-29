/**
 * This is the main class that initializes the application and sets up the GUI.
 */
import javax.swing.*;
public class Main {
    public static void main(String[] args) {
        // Create an instance of the GameBoard class
        GameBoard gameBoard = new GameBoard();
        // Create an instance of the GUI class and pass the gameBoard instance
        GUI gui = new GUI(gameBoard);
        // Set up the GUI
        gui.setup();
    }
}