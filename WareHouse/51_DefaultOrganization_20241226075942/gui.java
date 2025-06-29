import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Timer;
import java.util.TimerTask;
/**
 * This class represents the graphical user interface (GUI) for the web application.
 * It contains the main window and handles user interactions.
 */
public class GUI extends JFrame {
    private JButton button;
    private JLabel label;
    private GameTimer gameTimer;
    private int currentPlayer = 1; // Variable to keep track of the current player
    public GUI() {
        // Set up the main window
        setTitle("Board Game Turn Timer");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        // Create the button
        button = new JButton("Start Turn");
        button.addActionListener(new ButtonClickListener());
        // Create the label
        label = new JLabel("Player 1's turn");
        // Add the button and label to the main window
        add(button);
        add(label);
    }
    /**
     * Displays the main window of the application.
     */
    public void start() {
        // Display the main window
        setVisible(true);
    }
    /**
     * Starts the timer with the specified time limit in seconds.
     *
     * @param seconds The time limit for each turn in seconds.
     */
    private void startTimer(int seconds) {
        gameTimer = new GameTimer(seconds, label);
        gameTimer.start();
    }
    /**
     * Switches to the next player and updates the label to display the current player.
     */
    private void switchPlayer() {
        currentPlayer = currentPlayer == 1 ? 2 : 1; // Switch to the next player
        label.setText("Player " + currentPlayer + "'s turn"); // Update the label to display the current player
    }
    /**
     * ActionListener implementation for the button click event.
     */
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            // Handle button click event
            label.setText("Button Clicked");
            startTimer(60); // Start the timer with a 60-second limit
        }
    }
}