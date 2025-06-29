import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
/**
 * This class represents the graphical user interface (GUI) of the application.
 * It contains the main window and handles user interactions.
 */
public class GUI extends JFrame {
    private JButton button;
    private JLabel label;
    public GUI() {
        // Set up the main window
        setTitle("Action Game");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        // Create the button
        button = new JButton("Click me");
        // Create the label
        label = new JLabel("Hello, World!");
        // Add the button and label to the main window
        add(button, BorderLayout.CENTER);
        add(label, BorderLayout.SOUTH);
        // Add an action listener to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle button click event
                label.setText("Button clicked");
            }
        });
    }
    /**
     * This method starts the application by making the main window visible.
     */
    public void start() {
        // Show the main window
        setVisible(true);
    }
}