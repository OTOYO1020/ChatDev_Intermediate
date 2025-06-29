/**
 * This is the main class that contains the entry point of the application.
 * It initializes the game and starts the game loop.
 */
public class Main {
    public static void main(String[] args) {
        // Create an instance of the GameLogic class
        GameLogic gameLogic = new GameLogic();
        // Create an instance of the GUI class and pass the gameLogic instance
        GUI gui = new GUI(gameLogic);
        // Start the game
        gui.start();
    }
}