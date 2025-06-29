import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.Timer;
import javax.swing.JOptionPane;
/**
 * This class represents the game logic of the application.
 */
public class Game {
    private JFrame frame;
    private JPanel panel;
    private JLabel label;
    private Timer timer;
    private int timeLeft;
    /**
     * Constructor to initialize the game.
     */
    public Game() {
        // Create the frame
        frame = new JFrame("Demolition Expert");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 600);
        // Create the panel
        panel = new JPanel();
        panel.setBackground(Color.WHITE);
        // Create the label
        label = new JLabel("Time left: 60 seconds");
        panel.add(label);
        // Create the timer
        timeLeft = 60;
        timer = new Timer(1000, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                timeLeft--;
                label.setText("Time left: " + timeLeft + " seconds");
                if (timeLeft <= 0) {
                    timer.stop();
                    JOptionPane.showMessageDialog(frame, "Game Over");
                }
            }
        });
        // Add the panel to the frame
        frame.add(panel, BorderLayout.CENTER);
        // Start the timer
        timer.start();
    }
    /**
     * Method to start the game.
     */
    public void start() {
        // Make the frame visible
        frame.setVisible(true);
    }
}