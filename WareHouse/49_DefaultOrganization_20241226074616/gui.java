import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the application.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    public GUI() {
        // Create the main frame
        frame = new JFrame("Board Game Score Comparison");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);
        // Create the button
        button = new JButton("Click Me");
        button.addActionListener(new ButtonClickListener());
        // Create the label
        label = new JLabel("Hello World!");
        // Add the button and label to the frame
        frame.getContentPane().setLayout(new FlowLayout());
        frame.getContentPane().add(button);
        frame.getContentPane().add(label);
    }
    /**
     * This method starts the GUI application.
     */
    public void start() {
        frame.setVisible(true);
    }
    /**
     * This class represents the action listener for the button.
     */
    private class ButtonClickListener implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            // Get the arrays of scores from the user input
            int[] scores1 = {1, 2, 3}; // Replace with actual user input
            int[] scores2 = {4, 5, 6}; // Replace with actual user input
            // Instantiate ScoreComparator class
            ScoreComparator scoreComparator = new ScoreComparator();
            // Call the compareScores method of the ScoreComparator object
            String comparisonResult = scoreComparator.compareScores(scores1, scores2);
            // Update the label with the comparison result
            label.setText(comparisonResult);
        }
    }
}