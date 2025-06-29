/**
 * This class represents the graphical user interface (GUI) of the application.
 * It contains the main window and handles user interactions.
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class GUI {
    private JFrame frame;
    private JButton button;
    private JLabel label;
    public GUI() {
        // Create the main window
        frame = new JFrame("Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        // Create the button
        button = new JButton("Click me");
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                updateLabelText("Button clicked");
            }
        });
        // Create the label
        label = new JLabel("Hello World");
        // Add the button and label to the frame
        frame.getContentPane().setLayout(new FlowLayout());
        frame.getContentPane().add(button);
        frame.getContentPane().add(label);
    }
    /**
     * This method starts the application by making the main window visible.
     */
    public void start() {
        // Show the main window
        frame.setVisible(true);
    }
    /**
     * This method updates the label text to the specified value.
     *
     * @param text The new text for the label
     */
    public void updateLabelText(String text) {
        label.setText(text);
    }
}