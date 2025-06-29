import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface of the web application.
 * It contains the main window and handles user interactions.
 */
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    public GUI() {
        // Create the main window
        frame = new JFrame("Productivity Enhancer");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(new FlowLayout());
        // Create the label
        label = new JLabel("Hello World!");
        // Create the button
        button = new JButton("Click me");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                label.setText("Button clicked!");
            }
        });
        // Add components to the frame
        frame.add(label);
        frame.add(button);
    }
    public void start() {
        // Display the main window
        frame.setVisible(true);
    }
}