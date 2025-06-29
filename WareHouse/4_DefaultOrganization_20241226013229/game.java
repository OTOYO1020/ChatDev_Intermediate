import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the game logic and handles user interactions.
 */
public class Game {
    private JFrame frame;
    private JPanel panel;
    private JButton button;
    private JLabel label;
    public Game() {
        // Set up the main window
        frame = new JFrame("Action Game");
        frame.setSize(800, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Create the panel
        panel = new JPanel();
        panel.setLayout(new BorderLayout());
        // Create the button
        button = new JButton("Click me");
        // Create the label
        label = new JLabel("Hello, World!");
        // Add the button and label to the panel
        panel.add(button, BorderLayout.CENTER);
        panel.add(label, BorderLayout.SOUTH);
        // Add an action listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                label.setText("Button clicked");
            }
        });
        // Add the panel to the frame
        frame.add(panel);
    }
    /**
     * This method starts the game by making the main window visible.
     */
    public void start() {
        // Show the main window
        frame.setVisible(true);
    }
}