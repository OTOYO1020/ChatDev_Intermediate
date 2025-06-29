/**
 * This is the main class that serves as the entry point for the application.
 * It initializes the GUI and starts the application.
 */
public class Main {
    public static void main(String[] args) {
        // Create an instance of the GameBoard class
        GameBoard gameBoard = new GameBoard();
        // Create an instance of the GUI class and pass the game board
        GUI gui = new GUI(gameBoard);
        // Start the application
        gui.start();
    }
}