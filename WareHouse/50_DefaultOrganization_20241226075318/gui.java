import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) for the application.
 * It creates the main window and handles user interactions.
 */
public class GUI extends JFrame {
    private JButton button;
    private JLabel label;
    private ScorePredictor scorePredictor; // Added ScorePredictor instance
    public GUI() {
        // Set up the main window
        setTitle("Application");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());
        // Create the button
        button = new JButton("Click Me");
        // Create the label
        label = new JLabel("Hello World");
        // Add the button and label to the main window
        add(button);
        add(label);
        // Add an action listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                int gameType = 1; // Replace with actual game type
                int numberOfPlayers = 4; // Replace with actual number of players
                String playerStrategies = "strategy1, strategy2, strategy3"; // Replace with actual player strategies
                // Call the predictScore method from ScorePredictor class to get the predicted score
                int predictedScore = scorePredictor.predictScore(gameType, numberOfPlayers, playerStrategies);
                // Update the label with the predicted score
                label.setText("Predicted Score: " + predictedScore);
            }
        });
        // Create an instance of the ScorePredictor class
        scorePredictor = new ScorePredictor();
    }
    public void start() {
        // Make the main window visible
        setVisible(true);
    }
}