/**
 * This is the main class that serves as the entry point for the application.
 */
import javax.swing.JFrame;
import java.awt.BorderLayout;
public class Main {
    public static void main(String[] args) {
        // Create an instance of the JFrame class
        JFrame frame = new JFrame("Street Fighter");
        // Create an instance of the Game class
        Game game = new Game();
        // Add the game panel to the frame
        frame.add(game, BorderLayout.CENTER);
        // Set the frame size and close operation
        frame.setSize(800, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Make the frame visible
        frame.setVisible(true);
        // Start the game
        game.start();
    }
}