import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import feedback.FeedbackFormManager;
import feedback.FeedbackDataAnalyzer;
/**
 * This class represents the graphical user interface (GUI) for the web application.
 * It contains all the necessary components and handles user interactions.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    private FeedbackFormManager formManager;
    private FeedbackDataAnalyzer dataAnalyzer;
    public GUI(FeedbackFormManager formManager, FeedbackDataAnalyzer dataAnalyzer) {
        this.formManager = formManager;
        this.dataAnalyzer = dataAnalyzer;
        // Create the main frame
        frame = new JFrame("Web Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create the button
        button = new JButton("Click me!");
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                label.setText("Button clicked!");
            }
        });
        // Create the label
        label = new JLabel();
        // Add components to the frame
        frame.getContentPane().setLayout(new FlowLayout());
        frame.getContentPane().add(button);
        frame.getContentPane().add(label);
    }
    public void start() {
        // Make the frame visible
        frame.setVisible(true);
    }
}