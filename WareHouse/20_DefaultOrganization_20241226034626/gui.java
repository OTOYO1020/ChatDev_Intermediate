import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the application.
 * It creates and manages the main window and its components.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    private Game game; // Reference to the game logic
    public GUI() {
        // Create the main window
        frame = new JFrame("Action Game");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        // Create the game canvas
        GameCanvas gameCanvas = new GameCanvas();
        gameCanvas.setPreferredSize(new Dimension(800, 500));
        // Create the buttons
        button = new JButton("Move");
        button.addActionListener(new ButtonClickListener());
        // Create the label
        label = new JLabel("Score: 0");
        // Add the components to the frame
        frame.getContentPane().setLayout(new BorderLayout());
        frame.getContentPane().add(gameCanvas, BorderLayout.CENTER);
        frame.getContentPane().add(button, BorderLayout.SOUTH);
        frame.getContentPane().add(label, BorderLayout.NORTH);
        // Create an instance of the Game class
        game = new Game(gameCanvas, label);
        // Add key listener to the game canvas
        gameCanvas.addKeyListener(new GameKeyListener(game));
        // Set the focus to the game canvas
        gameCanvas.setFocusable(true);
        gameCanvas.requestFocus();
        // Set the game instance in the game canvas
        gameCanvas.setGame(game);
    }
    public void start() {
        // Make the frame visible
        frame.setVisible(true);
        // Start the game
        game.start();
    }
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            // Handle button click event
            game.movePlayer();
        }
    }
}